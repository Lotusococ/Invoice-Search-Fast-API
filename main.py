import os
import socket
import uvicorn
from typing import Optional
from pydantic import BaseModel

# FastAPI imports
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder  
from helper.helper import helper

# Component imports
from invoiceSearch.invoiceSearchExcelAPI import invoiceSearchExcelAPI
from invoiceSearch.invoiceSearchWebAPI import invoiceSearchWebAPI
from sendLog.sendLog import sendLog

# # GET LOCAL ENVIRONMENT VARIABLE
# # Uncomment for local development
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World From Fast API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/api/helper")
async def request_helper():
    return helper()

class SearchRequest(BaseModel):
    userId: Optional[str] = None
    invoice_number: list[str]

@app.post("/api/invoicesearch_webapi")
async def requestInvoiceSearchWebAPI(request_body: SearchRequest):
    return await invoiceSearchWebAPI(request_body.userId, request_body.invoice_number)

@app.post("/api/invoicesearch_excelapi")
async def requestInvoiceSearchExcelAPI(request_body: SearchRequest):
    return await invoiceSearchExcelAPI(request_body.userId, request_body.invoice_number)

class LogRequest(BaseModel):
    userId: Optional[str] = None
    message: str
    level: str
    timeStamp: str
    environment: str
    service: str
    version: Optional[str] = None

@app.post("/api/sendlog")
async def request_send_log(request: Request, log_data: LogRequest):
    hostname = socket.gethostname()

    session_id = getattr(request.state, "session_id", None)  

    ip_address = request.client.host

    user_agent = request.headers.get("User-Agent")

    log_data_encoded = jsonable_encoder(log_data)
    log_data_encoded.update({  
        'hostname': hostname,  
        'sessionId': session_id,
        'ipAddress': ip_address,  
        'userAgent': user_agent,  
    })
    
    response = await sendLog(log_data_encoded)
    return response

if __name__ == "__main__":
    debug_mode = os.getenv("DEBUG", False).lower() == True  
    log_level = "debug" if debug_mode else "info"  
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=debug_mode, log_level=log_level)  
