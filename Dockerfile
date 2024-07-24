from python

RUN mkdir /django_app
WORKDIR /django_app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    curl firefox-esr ffmpeg                    \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/bin \
 && apt-get purge -y curl

RUN apt-get install -y ca-certificates && update-ca-certificates

COPY . .

RUN chmod a+x Docker/*.sh
