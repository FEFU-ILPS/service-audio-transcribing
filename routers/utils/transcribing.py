import torch
from numpy import ndarray

from models import model_manager


def transcribe_audio(audio_input: ndarray, sample_rate: int, model_lang: str) -> list[str]:
    """Извлекает транскрипцию речи из аудиофайла.

    Args:
        audio_input (ndarray): Аудиофайл в виде Numpy array.
        sample_rate (int): Частота дискретизации аудиофайла.
        model_lang (str): Язык модели.

    Returns:
        list[str]: Транскрипция распознанной речи.
    """
    processor, model = model_manager.get_model(model_lang)

    input_values = processor(
        audio_input, return_tensors="pt", sampling_rate=sample_rate
    ).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription
