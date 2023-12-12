# Invoice Search Fast API
日本語版のREADME.mdは[こちら](/README.md)をご覧ください。  
English version of README.md is translated by OpenAI.  
<img src="assets/img/Invoice%20Search%20App-logo.png" width="50%">  

## Purpose of This Directory  
This directory is for an API that calls the Excel API or the National Tax Agency's Qualified Invoice Issuer Publication System Web-API in response to invoice numbers searched in the Invoice Search Web App, and then returns the search results to the Invoice Search Web App.  
Note that this directory is intended for deployment to Vercel, but it can also be deployed to other services such as Azure's App Service by adding files like `startup.txt`.  

## Features and Cautions  
In order to call the National Tax Agency's Qualified Invoice Issuer Publication System Web-API, it is necessary to set the destination URL and the application ID.  
Please note that an application to the National Tax Agency is required for the application ID, so please apply from [here]("https://www.invoice-kohyo.nta.go.jp/web-api/index.html").  
Additionally, we also support the use of the [ExcelAPI]("https://excelapi.org/docs/") that can be accessed without using the National Tax Agency's system.  
Please be mindful to avoid excessive access to these APIs as it may cause inconvenience to the National Tax Agency and the creators of ExcelAPI.  

## Environment Variables  
| Category                         | Key                          | Value                                                                            |
| -------------------------------- | ---------------------------- | -------------------------------------------------------------------------------- |
| General                          | `DEBUG`                      | true/ false                                                                      |
| General                          | `VERSION`                    | 1.0.0                                                                            |
| Qualified Invoice Issuer Web-API | `INVOICE_APP_ID`             | Your Application ID                                                              |
| Qualified Invoice Issuer Web-API | `INVOICE_API_URL`            | https://web-api.invoice-kohyo.nta.go.jp/1/valid?id={Your Application ID}&number= |
| ExcelAPI                         | `BASE_URL`                   | https://api.excelapi.org/company/                                                |
| ExcelAPI                         | `INVOICE_NAME`               | invoice_name                                                                     |
| ExcelAPI                         | `INVOICE_ADDRESS`            | invoice_address                                                                  |
| ExcelAPI                         | `INVOICE_ID`                 | ?id=                                                                             |
| Axiom                            | `AXIOM_INGEST_ENDPOINT`      | https://cloud.axiom.co/api/v1/datasets/{Axiom Dataset Name}/ingest               |
| Axiom                            | `AXIOM_API_TOKEN`            | Enter Axiom's API Token                                                          |
| Axiom                            | `AXIOM_DATASET`              | Enter Axiom's Dataset                                                            |
| Axiom                            | `AXIOM_ORG_ID`               | Enter Axiom's Organization ID                                                    |
| Firebase                         | `FIREBASE_APIKEY`            | Enter Firebase's API Key                                                         |
| Firebase                         | `FIREBASE_AUTHDOMAIN`        | Enter Firebase's Auth Domain                                                     |
| Firebase                         | `FIREBASE_PROJECTID`         | Enter Firebase's Project ID                                                      |
| Firebase                         | `FIREBASE_STORAGEBUCKET`     | Enter Firebase's Storage Bucket                                                  |
| Firebase                         | `FIREBASE_MESSAGINGSENDERID` | Enter Firebase's Messaging Sender ID                                             |
| Firebase                         | `FIREBASE_APPID`             | Enter Firebase's App ID                                                          |
| Firebase                         | `FIREBASE_MEASUREMENTID`     | Enter Firebase's Measurement ID                                                  |
  
## Sources of Information  
1. [National Tax Agency Qualified Invoice Issuer Publication Site](https://www.invoice-kohyo.nta.go.jp/index.html)  
2. [Excel API](https://excelapi.org/docs/)  
  
Please note that **the use of the National Tax Agency's Qualified Invoice Issuer Publication System Web-API is based on information obtained using the Web-API feature of the system, but the content of the service is not guaranteed by the National Tax Agency.**  
Furthermore, Excel API is operated by Hatolize LLC. For inquiries regarding Excel API, please contact them directly. Thank you for your cooperation.  

## LICENSE
MIT  
Copyright (c) 2023 Lotus
