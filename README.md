# Invoice Search Fast API
English version of README.md is on [here](/README_EN.md)  
<img src="assets/img/Invoice%20Search%20App-logo.png" width="50%">  

## 本ディレクトリの目的
本ディレクトリは、Invoice Search Web Appにて検索したインボイス番号に対して、Excel APIもしくは国税庁の適格請求書発行事業者公表システムWeb-APIを呼び出し、検索結果をInvoice Search Web Appに返却するためのAPIです。  
なお、本ディレクトリはVercelへのデプロイを目標として記載しておりますが、startup.txtなどを追加し、AzureのApp Serviceなどへのデプロイも可能です。

## 機能および留意点
国税庁の適格請求書発行事業者公表システムWeb-APIを呼び出すにあたり、呼び出し先のURLおよびアプリケーションIDの設定が必要です。  
なお、アプリケーションIDに関しては国税庁への申請が必要のため、[こちら]("https://www.invoice-kohyo.nta.go.jp/web-api/index.html")より申請ください。  
また、適格請求書発行事業者公表システムWeb-APIを使用せずに取得可能な[ExcelAPI]("https://excelapi.org/docs/")の呼び出しにも対応しております。  
なお、各種APIへの大量アクセスは、国税庁およびExcelAPI作成者様に迷惑が掛かりますため、避けるようご留意いただけますようお願い致します。

## 環境変数
| カテゴリ                                | キー                         | 値                                                                                    |
| --------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |
| 一般                                    | `DEBUG`                      | true/ false                                                                           |
| 一般                                    | `VERSION`                    | 1.0.0                                                                                 |
| 適格請求書発行事業者公表システムWeb-API | `INVOICE_APP_ID`             | 自身のアプリケーションID                                                              |
| 適格請求書発行事業者公表システムWeb-API | `INVOICE_API_URL`            | https://web-api.invoice-kohyo.nta.go.jp/1/valid?id={自身のアプリケーションID}&number= |
| ExcelAPI                                | `BASE_URL`                   | https://api.excelapi.org/company/                                                     |
| ExcelAPI                                | `INVOICE_NAME`               | invoice_name                                                                          |
| ExcelAPI                                | `INVOICE_ADDRESS`            | invoice_address                                                                       |
| ExcelAPI                                | `INVOICE_ID`                 | ?id=                                                                                  |
| Axiom                                   | `AXIOM_INGEST_ENDPOINT`      | https://cloud.axiom.co/api/v1/datasets/{Axiom Dataset名}/ingest                       |
| Axiom                                   | `AXIOM_API_TOKEN`            | AxiomのAPI Tokenを入力                                                                |
| Axiom                                   | `AXIOM_DATASET`              | AxiomのDatasetを入力                                                                  |
| Axiom                                   | `AXIOM_ORG_ID`               | AxiomのOrganization IDを入力                                                          |
| Firebase                                | `FIREBASE_APIKEY`            | FirebaseのAPI Keyを入力                                                               |
| Firebase                                | `FIREBASE_AUTHDOMAIN`        | FirebaseのAuth Domainを入力                                                           |
| Firebase                                | `FIREBASE_PROJECTID`         | FirebaseのProject IDを入力                                                            |
| Firebase                                | `FIREBASE_STORAGEBUCKET`     | FirebaseのStorage Bucketを入力                                                        |
| Firebase                                | `FIREBASE_MESSAGINGSENDERID` | FirebaseのMessaging Sender IDを入力                                                   |
| Firebase                                | `FIREBASE_APPID`             | FirebaseのApp IDを入力                                                                |
| Firebase                                | `FIREBASE_MEASUREMENTID`     | FirebaseのMeasurement IDを入力                                                        |

## 情報取得元明示
1. [国税庁　適格請求書発行事業者公表サイト](https://www.invoice-kohyo.nta.go.jp/index.html)
2. [Excel API](https://excelapi.org/docs/)

なお、国税庁　適格請求書発行事業者公表システムWeb-APIの使用にあたり、**このサービスは、国税庁適格請求書発行事業者公表システムのWeb-API機能を利用して取得した情報をもとに作成しているが、サービスの内容は国税庁によって保証されたものではない**ことをご留意ください。  
また、Excel APIは合同会社ハトライズ様にて運営されております。Excel APIに関するお問い合わせに関しましては、そちらにお問い合わせいただきますよう、宜しくお願い致します。

## ライセンス
MIT  
Copyright (c) 2023-2024 Lotus
