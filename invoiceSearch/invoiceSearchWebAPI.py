import os
import requests
from typing import Optional
from datetime import datetime, timezone, timedelta

# FastAPI imports
from fastapi import HTTPException

# Component imports
from sendLog.sendLog import sendLogPrep


# Invoice Search
async def invoiceSearchWebAPI(userId: Optional[str], invoiceNum: list[str]):
    result = []

    invoice_numbers_str = ",".join(invoiceNum)
    await sendLogPrep(
        userId,
        f"Starting invoiceSearchWebAPI. Invoice Numbers: {invoice_numbers_str}",
        "INFO",
        "invoiceSearchWebAPI.py",
    )

    invoiceAppId = os.environ.get("INVOICE_APP_ID")
    invoiceApiUrl = os.environ.get("INVOICE_API_URL")
    JST = timezone(timedelta(hours=+9), "JST")
    now_jst = datetime.now(JST)
    date_str = now_jst.strftime("%Y-%m-%d")

    try:
        if not all(
            [
                invoiceAppId,
                invoiceApiUrl,
            ]
        ):
            raise HTTPException(
                status_code=500, detail="Environment variables are not properly set"
            )

        url = f"{invoiceApiUrl}{invoiceAppId}&number={invoice_numbers_str}&day={date_str}&type=21&history=0"

        response = requests.get(url)
        
        response.raise_for_status()
        data = response.json()

        key = 1
        for item in data.get("announcement", []):
            result.append(
                {
                    "key": str(key),
                    "invoiceNumber": item.get("registratedNumber", ""),
                    "invoiceName": item.get("name", ""),
                    "invoiceAddress": item.get("address", ""),
                }
            )
            key += 1

        await sendLogPrep(
            userId,
            "Successfully completed invoiceSearchWebAPI",
            "INFO",
            "invoiceSearchWebAPI.py",
        )
        
        return result
    except Exception as e:
        await sendLogPrep(
            userId, f"There was an error: {e}", "ERROR", "invoiceSearchWebAPI.py"
        )
        raise HTTPException(status_code=500, detail=f"There was an error: {e}")
