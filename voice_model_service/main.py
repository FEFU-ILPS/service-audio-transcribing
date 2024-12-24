from fastapi import FastAPI, File, UploadFile
from process_audio_service import process_audio
from starlette.responses import JSONResponse
import soundfile as sf
import uvicorn

app = FastAPI()

@app.post("/api/v1/transcribe/")
async def transcribe(audio_file: UploadFile = File()) -> list[str]:
    audio_input, sample_rate = sf.read(audio_file.file)
    transcription = process_audio(audio_input, sample_rate)
    return JSONResponse({"transcription": transcription})

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
