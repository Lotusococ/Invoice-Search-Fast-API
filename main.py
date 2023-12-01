from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from invoiceSearch.invoiceSearch import invoiceSearch

# # GET LOCAL ENVIRONMENT VARIABLE
# # Uncomment for local development
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def hello():
    return {"message": "Hello, Success!"}

class SearchRequest(BaseModel):
    invoice_number: list[str]

@app.post("/api/invoicesearch")
async def request_invoice_search(request_body: SearchRequest):
    res = invoiceSearch(request_body.invoice_number)
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True, log_level="debug")