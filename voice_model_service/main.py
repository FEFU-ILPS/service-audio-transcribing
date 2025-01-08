from fastapi import FastAPI, File, UploadFile
from process_audio_service import process_audio
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import soundfile as sf
import uvicorn

from model.transcription_dto import TranscriptionDto

app = FastAPI(
    title="voice-model-service",
    description="Service that transcribes user voice input"
)


@app.post(
    "/api/v1/transcribe/",
    tags=["transcription"],
    summary="Transcribe voice input",
    response_model=TranscriptionDto
)
async def transcribe(audio_file: UploadFile = File()):
    audio_input, sample_rate = sf.read(audio_file.file)
    transcription = process_audio(audio_input, sample_rate)
    response = jsonable_encoder(TranscriptionDto(transcription=transcription))
    return JSONResponse(response)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
