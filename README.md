# Аккустическая модель
Сервис, который принимает аудиофайл в формате wav с частотой дискритизации 16 кГц и выдает фонетическую транскрипцию данного файла
## Локальный запуск
Чтобы запустить локально необходимо:
1. Установить все файлы с [диска](https://drive.google.com/drive/folders/1XwMw0lZaVJ2VU3uKs2Os07g3bGieNuMb?usp=sharing)
2. Извлечь файлы по пути ~/voice_model_service/voice_model
3. Установить [Espeak-ng](https://github.com/espeak-ng/espeak-ng/releases)
    - установить перменную среды: PHONEMIZER_ESPEAK_PATH: путь до папки с файлом libespeak-ng
    - установить перменную среды: PHONEMIZER_ESPEAK_LIBRARY: путь до файла libespeak-ng
4. в терминале прописать команды:
    - python -m venv venv
    - pip install -r requierments.txt
## Запуск в докере
Чтобы запустить сервис в контейнере достаточно собрать образ из [докерфайла](/voice_model_service/Dockerfile)