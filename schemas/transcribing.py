from typing import Annotated
from pydantic import BaseModel, Field
from .examples import TRANSCRIPTION_EXAMPLE


class TranscribingResponse(BaseModel):
    """Данные, отправляемые после транскрибирования речи из файла."""

    transcription: Annotated[list[str], Field(examples=TRANSCRIPTION_EXAMPLE)]
