from pydantic import BaseModel, Field


class TranscriptionDto(BaseModel):
    transcription: list[str] = Field(examples=["ʃ iː h æ d j ɚ d ɑːɹ k s uː t ɪ n ɡ ɹ iː s i w ɔː ʃ w ɑː ɾ ɚ ɔː l j iː ɹ"])
