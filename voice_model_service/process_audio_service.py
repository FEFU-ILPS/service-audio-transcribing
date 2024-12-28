from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch


def process_audio(audio_input, sample_rate):
    local_path = "/voice_model_service/voice_model"
    processor = Wav2Vec2Processor.from_pretrained(local_path)
    model = Wav2Vec2ForCTC.from_pretrained(local_path)

    input_values = processor(audio_input, return_tensors="pt",
                             sampling_rate=sample_rate).input_values

    with torch.no_grad():
        logits = model(input_values).logits
 
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription
