import os
import socket
import datetime
from axiom.client import Client
from fastapi import Request
from fastapi.encoders import jsonable_encoder  
from typing import Optional

AXIOM_API_TOKEN = os.getenv("AXIOM_API_TOKEN")
AXIOM_ORG_ID = os.getenv("AXIOM_ORG_ID")
AXIOM_DATASET = os.getenv("AXIOM_DATASET")

async def sendLog(log_data: dict):
    client = Client(AXIOM_API_TOKEN, AXIOM_ORG_ID)
    response = client.ingest_events(
        dataset=AXIOM_DATASET,
        events=[log_data]
    )
    return response

async def sendLogPrep(userId: Optional[str], message: str, level: str, service: str):
    try:
        is_debug_mode = os.getenv("DEBUG", False).lower() == True  
        environment = "debug" if not is_debug_mode else "production"

        timeStamp = datetime.datetime.now().isoformat()
        hostname = socket.gethostname()
        
        log_data = {  
            'userId': userId,
            'message': message,
            'level': level,
            'timeStamp': timeStamp,
            'environment': environment,
            'hostname': hostname,
            'service': service,
            'version': os.getenv("VERSION"),
        }
        
        log_data_encoded = jsonable_encoder(log_data)
        await sendLog(log_data_encoded)
    except Exception as e:
        raise Exception(status_code=500, detail=f"There was an error: {e}")