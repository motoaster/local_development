FROM python:3.9-slim

# アプリケーションディレクトリを作成する
WORKDIR /usr/src/app

# pipでインストールしたいモジュールをrequirements.txtに記述しておいて、
# コンテナ内でpipにインストールさせる
# requirements.txtの書き方は[pip freeze]コマンドから参考に出来る
# pipのアップデート
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y vim less

COPY . /usr/src/app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

# RUN pip install fastapi uvicorn
WORKDIR /usr/src/python
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
