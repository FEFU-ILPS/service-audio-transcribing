import soundfile as sf
import torch
from fastapi import APIRouter, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import Transcription
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

router = APIRouter()


def process_audio(audio_input, sample_rate) -> list[str]:
    local_path = "/voice_model_service/voice_model"
    processor = Wav2Vec2Processor.from_pretrained(local_path)
    model = Wav2Vec2ForCTC.from_pretrained(local_path)

    input_values = processor(
        audio_input, return_tensors="pt", sampling_rate=sample_rate
    ).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription


@router.post(
    "/{lang}/transcribe/",
    tags=["transcription"],
    summary="Transcribe voice input.",
    response_model=Transcription,
)
async def transcribe(lang: str, audio_file: UploadFile):
    audio_input, sample_rate = sf.read(audio_file.file)
    transcription = process_audio(audio_input, sample_rate)
    response = jsonable_encoder(Transcription(transcription=transcription))
    return JSONResponse(response)
