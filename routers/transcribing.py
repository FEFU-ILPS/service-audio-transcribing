from enum import Enum
from typing import Annotated

import soundfile as sf
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from models import model_manager
from schemas import TranscribingResponse

from .utils.transcribing import transcribe_audio

router = APIRouter()


class ModelLang(Enum):
    ENGLISH = "english"


@router.post("/", summary="Транскрипция речи")
async def transcribe(
    lang: Annotated[ModelLang, Form(...)],
    file: Annotated[UploadFile, File(...)],
) -> TranscribingResponse:
    """Получает транскрипцию речи из аудиофайла и возвращает ее в виде текста."""
    if not model_manager.is_model_loaded(lang.value):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"The model for the language '{lang.value}' is not uploaded in the service.",
        )

    if not file.filename.lower().endswith(".wav"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file extension. Only files with the extension '.wav' are allowed.",
        )

    if file.content_type not in ["audio/wav", None]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid content type. Only audio/wav is allowed for WAV files.",
        )

    file_binarystream = file.file
    audio_input, sample_rate = sf.read(file_binarystream)

    transcription = transcribe_audio(audio_input, sample_rate, lang.value)

    return TranscribingResponse(transcription=transcription)
