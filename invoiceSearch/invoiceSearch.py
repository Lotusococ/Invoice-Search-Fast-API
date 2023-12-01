import os
import requests
from fastapi import HTTPException
from concurrent.futures import ThreadPoolExecutor


# Invoice Search
def invoiceSearch(invoiceNum: list[str]):
    result = []

    baseUrl = os.environ.get("BASE_URL")
    invoiceCheck = os.environ.get("INVOICE_CHECK")
    invoiceName = os.environ.get("INVOICE_NAME")
    invoiceTradeName = os.environ.get("INVOICE_TRADENAME")
    invoiceAddress = os.environ.get("INVOICE_ADDRESS")
    invoiceId = os.environ.get("INVOICE_ID")

    try:
        if not all(
            [
                baseUrl,
                invoiceCheck,
                invoiceName,
                invoiceTradeName,
                invoiceAddress,
                invoiceId,
            ]
        ):
            raise HTTPException(
                status_code=500, detail="Environment variables are not properly set"
            )

        for index, num in enumerate(invoiceNum):
            urls = [
                f"{baseUrl}{invoiceCheck}{invoiceId}{num}",
                f"{baseUrl}{invoiceName}{invoiceId}{num}",
                f"{baseUrl}{invoiceTradeName}{invoiceId}{num}",
                f"{baseUrl}{invoiceAddress}{invoiceId}{num}",
            ]

            try:
                with ThreadPoolExecutor() as executor:
                    responses = list(executor.map(requests.get, urls))

                for response in responses:
                    response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx

                checkResponse, nameResponse, tradeNameResponse, addressResponse = [
                    res.text for res in responses
                ]

                result.append(
                    {
                        "key": str(index + 1),
                        "invoiceNumber": num,
                        "invoiceCheck": checkResponse,
                        "invoiceName": nameResponse,
                        "invoiceTradeName": tradeNameResponse,
                        "invoiceAddress": addressResponse,
                    }
                )
            except requests.exceptions.RequestException as e:
                raise HTTPException(status_code=500, detail=f"There was an error: {e}")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was an error: {e}")
