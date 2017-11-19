# keyword-exraction-webservice (kews)

A very simple Keyword Extraction Web Service for Japanese language, using MeCab and pytermextract.

MeCabとpytermextracを使用した、超低機能なキーワード抽出Webサービスです。というか、pytermextractの簡単なラッパーです。TermExtractを使いたかったのですがPerlやPythonを呼ぶのが面倒だったので作りました。

## Requirements

- Python3
- MeCab (0.996)
- [pytermextract](http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/)

pytermextractはPyPIに登録されていないため、pipとは別にインストールが必要です。

以下はpipによりインストールできます。

- [Flask](http://flask.pocoo.org/)
- python-mecab

## Installation

1. Python3(及びpip), MeCab, pytermextractのインストールします。
1. `git clone` などでファイル一式をダウンロードします。
1. `pip install -r packages_requirements.txt` で必要なモジュールをインストールします。

## Get Started

kews.py を実行してください。ウェブサーバーが立ち上がります。

http://localhost:5000/ にアクセスして、テキストを入力して試すことができます。
出力形式は html か json のどちらかを選択できます。

ブラウザ以外からの使用も可能です。以下はcurlでアクセスする場合の例です。

```
curl -d type=json&text=(ここにテキスト) http://localhost:5000/
```

実際の使い方としては、マイクロサービス的に呼び出すことを想定しています。

## Alternative Installation & Usage

よりFlaskアプリっぽい方法で、インストールしてサーバー起動することもできます。
ただし、現在のところkewsはDB等に依存していないので、この方法をとるメリットはあまりありません。

1. Python3(及びpip), MeCab, pytermextractのインストールします。
1. `git clone` などでファイル一式をダウンロードします。
1. `cd keyword-exraction-webservice`
1. `pip install .`
1. `export FLASK_APP=kews`
1. `flask run`

## API
ルート(/)が唯一のエンドポイントです。メソッドはPOSTです。以下2つのパラメーターのみサポートしています。

### type

出力フォーマットを指定します。'html'または’json’。デフォルトは’html’です。

### text

キーワード抽出対象のテキストを指定します。

## TODO

- MeCab以外の解析器への対応
- store_df, store_lrへの対応

## LICENSE

[MIT LICENSE](https://github.com/nalls/keyword-exraction-webservice/blob/master/LICENSE)

## Author

[Shouki SAKAMOTO](https://github.com/shouki-s)
