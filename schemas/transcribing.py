from typing import Annotated

from pydantic import BaseModel, Field

from .examples import TRANSCRIPTIONS_EXAMPLE


class TranscribingResponse(BaseModel):
    """Данные, отправляемые после транскрибирования речи из файла."""

    transcription: Annotated[str, Field(examples=TRANSCRIPTIONS_EXAMPLE)]
