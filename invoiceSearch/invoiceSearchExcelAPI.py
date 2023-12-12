import os
import requests
from fastapi import HTTPException
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
from sendLog.sendLog import sendLogPrep


# Invoice Search
async def invoiceSearchExcelAPI(userId: Optional[str], invoiceNum: list[str]):
    result = []

    invoice_numbers_str = ", ".join(invoiceNum)
    await sendLogPrep(
        userId,
        f"Starting invoiceSearchExcelAPI. Invoice Numbers: {invoice_numbers_str}",
        "INFO",
        "invoiceSearchExcelAPI.py",
    )

    baseUrl = os.environ.get("BASE_URL")
    invoiceName = os.environ.get("INVOICE_NAME")
    invoiceAddress = os.environ.get("INVOICE_ADDRESS")
    invoiceId = os.environ.get("INVOICE_ID")

    try:
        if not all(
            [
                baseUrl,
                invoiceName,
                invoiceAddress,
                invoiceId,
            ]
        ):
            raise HTTPException(
                status_code=500, detail="Environment variables are not properly set"
            )

        for index, num in enumerate(invoiceNum):
            urls = [
                f"{baseUrl}{invoiceName}{invoiceId}{num}",
                f"{baseUrl}{invoiceAddress}{invoiceId}{num}",
            ]

            try:
                with ThreadPoolExecutor() as executor:
                    responses = list(executor.map(requests.get, urls))

                for response in responses:
                    response.raise_for_status()

                nameResponse, addressResponse = [
                    res.text for res in responses
                ]

                result.append(
                    {
                        "key": str(index + 1),
                        "invoiceNumber": num,
                        "invoiceName": nameResponse,
                        "invoiceAddress": addressResponse,
                    }
                )
            except Exception as e:
                await sendLogPrep(
                    userId,
                    f"There was an error: {e}",
                    "ERROR",
                    "invoiceSearchExcelAPI.py",
                )
                raise HTTPException(status_code=500, detail=f"There was an error: {e}")
        await sendLogPrep(
            userId,
            "Successfully completed invoiceSearchExcelAPI",
            "INFO",
            "invoiceSearchExcelAPI.py",
        )
        
        return result
    except Exception as e:
        await sendLogPrep(
            userId, f"There was an error: {e}", "ERROR", "invoiceSearchExcelAPI.py"
        )
        raise HTTPException(status_code=500, detail=f"There was an error: {e}")
