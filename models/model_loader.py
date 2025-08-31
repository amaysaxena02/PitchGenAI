from gpt4all import GPT4All
import os

MODEL_PATH = "D:/GitHub/PitchGenAI/models/Phi-3-mini-4k-instruct-q4.gguf"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. "
            "Please download Phi-3-mini-4k-instruct-q4.gguf and place it in the models/ folder."
        )
    # Load the model locally
    model = GPT4All(MODEL_PATH, allow_download=False)
    return model
