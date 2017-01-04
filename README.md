# keyword-exraction-webservice
Very simple keyword extraction web service for Japanese language, using MeCab and pytermextract.
MeCabとpytermextracを使用した、超低機能なキーワード抽出Webサービスです。というか、pytermextractの簡単なラッパーです。

## Requirements
- Python3
- MeCab (0.996)
- [pytermextract](http://gensen.dl.itc.u-tokyo.ac.jp/pytermextract/)
pytermextractはPyPIに登録されていないため、別途インストールが必要です。

## Installations

Python3, MeCab, pytermextractのインストール後、

```
pip install -r packages_requirements.txt
```

## Get started
kews.pyを実行してください。ウェブサーバーが立ち上がります。

http://localhost:5000/ にアクセスして、テキストを入力して試すことができます。
出力形式はhtmlかjsonのどちらかを選択できます。

ブラウザ以外からの使用も可能で。以下はcurlでアクセスする場合の例です。

```
curl -d type=json&text=(ここにテキスト) http://localhost:5000/
```

実際の使い方としては、マイクロサービス的に呼び出すことを想定しています。JavaからPerlかPythonを呼ぶのが面倒だったので作りました。

## API
ルート(/)が唯一のリソースです。以下2つのパラメーターのみサポートしています。

### type
出力フォーマットを指定します。'html'または’json’。デフォルトは’html’です。
### text
キーワード抽出対象のテキストを指定します。

## LICENSE

[MIT LICENSE](https://github.com/nalls/keyword-exraction-webservice/blob/master/LICENSE)

## Author

[nalls](https://github.com/nalls)
