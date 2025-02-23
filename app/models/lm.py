from pydantic import BaseModel, Field
from typing import Annotated, List


class Transcription(BaseModel):
    # TODO: Более простая транскрипция, например слова.
    transcription: Annotated[List[str], Field(examples=["d ɑːɹ k"])]
