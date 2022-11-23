FROM ubuntu:20.04
WORKDIR /One-armedBandits

RUN apt-get update -q \
    && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY . /One-armedBandits
RUN pip install -r requirements.txt --no-cache-dir

CMD ["bash", "run_app.sh"]
