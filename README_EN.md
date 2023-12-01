# Invoice Search Fast API

日本語版のREADME.mdは[こちら](/README.md)をご覧ください。

## Purpose of this directory
The purpose of this directory is to provide an API for the Invoice Search Web App to call the National Tax Agency's Qualified Invoice Issuer Disclosure System Web API and return the search results to the Invoice Search Web App. <br/>
Please note that while this directory is intended for deployment to Vercel, it is also possible to deploy to Azure's App Service or other cloud services by adding startup.txt and other files.

## Features and Considerations
To call the National Tax Agency's Qualified Invoice Issuer Disclosure System Web API, you need to configure the URL and Application ID of the API endpoint. <br/>
Please note that you need to apply for an Application ID from the National Tax Agency, which can be done here. <br/>
In addition, this API also supports calling the ExcelAPI which can be accessed without using the Qualified Invoice Issuer Disclosure System Web API. <br/>
Please be aware that excessive access to these APIs may cause inconvenience to the National Tax Agency and the creators of ExcelAPI, so please avoid it.

## Environment Variables
| Category                                               | Key                 | Value                                                                    | 
| :----------------------------------------------------- | :------------------ | :----------------------------------------------------------------------- | 
| Qualified Invoice Issuer Disclosure System Web API	 | `INVOICE_APP_ID`    | //Your Application IDID                                                  | 
| Qualified Invoice Issuer Disclosure System Web API	 | `INVOICE_API_URL`   | https://web-api.invoice-kohyo.nta.go.jp/1/valid?id=KTQ3Rry292avR&number= | 
| ExcelAPI                                               | `BASE_URL`          | https://api.excelapi.org/company/                                        | 
| ExcelAPI                                               | `INVOICE_CHECK`     | invoice_check                                                            | 
| ExcelAPI                                               | `INVOICE_NAME`      | invoice_name                                                             | 
| ExcelAPI                                               | `INVOICE_TRADENAME` | invoice_tradename                                                        | 
| ExcelAPI                                               | `INVOICE_ADDRESS`   | invoice_address                                                          | 
| ExcelAPI                                               | `INVOICE_ID`        | ?id=                                                                     | 