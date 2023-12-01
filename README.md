# Invoice Search Fast API

English version of README.md is on [here](/README_EN.md)

## 本ディレクトリの目的
本ディレクトリは、Invoice Search Web Appにて検索したインボイス番号に対して、国税庁の適格請求書発行事業者公表システムWeb-APIを呼び出し、検索結果をInvoice Search Web Appに返却するためのAPIです。<br/>
なお、本ディレクトリはVercelへのデプロイを目標として記載しておりますが、startup.txtなどを追加し、AzureのApp Serviceなどへのデプロイも可能です。

## 機能および留意点
国税庁の適格請求書発行事業者公表システムWeb-APIを呼び出すにあたり、呼び出し先のURLおよびアプリケーションIDの設定が必要です。<br/>
なお、アプリケーションIDに関しては国税庁への申請が必要のため、[こちら]("https://www.invoice-kohyo.nta.go.jp/web-api/index.html")より申請ください。<br/>
また、適格請求書発行事業者公表システムWeb-APIを使用せずに取得可能な[ExcelAPI]("https://excelapi.org/docs/")の呼び出しにも対応しております。<br/>
なお、各種APIへの大量アクセスは、国税庁およびExcelAPI作成者様に迷惑が掛かりますため、避けるようご留意いただけますようお願い致します。

## 環境変数
| カテゴリ                                | キー                | 値                                                                       | 
| :-------------------------------------- | :------------------ | :----------------------------------------------------------------------- | 
| 適格請求書発行事業者公表システムWeb-API  | `INVOICE_APP_ID`    | //自身のアプリケーションID                                               | 
| 適格請求書発行事業者公表システムWeb-API  | `INVOICE_API_URL`   | https://web-api.invoice-kohyo.nta.go.jp/1/valid?id=KTQ3Rry292avR&number= | 
| ExcelAPI                                | `BASE_URL`          | https://api.excelapi.org/company/                                        | 
| ExcelAPI                                | `INVOICE_CHECK`     | invoice_check                                                            | 
| ExcelAPI                                | `INVOICE_NAME`      | invoice_name                                                             | 
| ExcelAPI                                | `INVOICE_TRADENAME` | invoice_tradename                                                        | 
| ExcelAPI                                | `INVOICE_ADDRESS`   | invoice_address                                                          | 
| ExcelAPI                                | `INVOICE_ID`        | ?id=                                                                     | 