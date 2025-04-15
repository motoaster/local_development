# local_test

## /docker ディレクトリ
DockerFile 関連格納
## /api ディレクトリ
python 関連格納  
FastApiのFW環境を構築
## /front ディレクトリ
php 関連格納  
laravelのFWの環境を構築  
「/front/public/」にVueに関連を格納  
Vue用に下記ファイルを修正  
front\vite.config.js  
front\resources\js\app.js  

## 構成
api側を外部インターフェースに見立てる。  
画面の表記はVueJS側で構成。CURDはRestApiの形式でバックエンド(Laravel)側に投げ処理を実施する形の構成としている。

## 起動時
・Gitから必要ソースを落とし込んだ後に下記コマンドを実施。  
※[node_modules]及び[vendor]の中身が大容量のためmount実施。  
※PCの基本スペックの問題でWSL2での構築としていない。こちらで動作が行えるかは別途確認が必要。
→ docker compose up -d --build ※初回ビルド込みで実施。  
→ docker compose up -d

・Viteを実行。Vite側で設定を付与しているためVuejs側の処理も起動。フロント込みの動作確認が実施できる。  
→ docker compose exec web-front npm run dev

・Localhostで動作確認→基本的にcompose.ymlを参照
Webサービス検証：http://localhost/
WebAPI検証：http://localhost:8080/docs
PHPMyAdmin：http://localhost:8001/

