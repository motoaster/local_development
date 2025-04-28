# イメージの取り込み
FROM php:8.3-fpm
EXPOSE 5173
# ミドルウェアをインストール
RUN apt-get update \
    && apt-get install -y \
    git \
    zip \
    unzip \
    vim \
    less \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
    libfontconfig1 \
    libxrender1
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install gd
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install pdo_mysql mysqli exif

# Node及びComporserインストール
RUN cd /usr/bin && curl -s http://getcomposer.org/installer | php && ln -s /usr/bin/composer.phar /usr/bin/composer

ENV NODE_VERSION=20.15.0
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version

# ローカルで用意していた各連携ファイルをコンテナ上に配置する
ADD php.ini /usr/local/etc/php/
WORKDIR /src
ADD . /src/storage
RUN chown -R www-data:www-data /src/storage

# Node及びConpose実施, Vueインストール実施
ENTRYPOINT [ "bash", "-c", "composer install; npm install; exec php-fpm; npm install vue @vitejs/plugin-vue; npm run build;"]
