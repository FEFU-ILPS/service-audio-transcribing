FROM python:3.12-slim

RUN apt-get update && apt-get install -y espeak-ng \
    wget unzip --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV PHONEMIZER_ESPEAK_LIBRARY="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1"
ENV PHONEMIZER_ESPEAK_PATH="/usr/lib/x86_64-linux-gnu/"    

WORKDIR /voice_model_service

COPY requirements.txt /voice_model_service/

RUN pip install --no-cache-dir gdown \
    && gdown --folder https://drive.google.com/drive/folders/1XwMw0lZaVJ2VU3uKs2Os07g3bGieNuMb?usp=sharing -O /voice_model_service/voice_model

RUN pip install -r requirements.txt --no-cache-dir --timeout=900 \
    && rm -rf /root/.cache/pip

COPY . /voice_model_service/

RUN find /voice_model_service -type d -name "pycache" -exec rm -r {} + \
    && find /voice_model_service -type f -name "*.pyc" -exec rm -f {} + \
    && rm -rf /tmp/*

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]