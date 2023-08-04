FROM python:3.10
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Run bot.py
CMD ["python3", "bot.py"]
