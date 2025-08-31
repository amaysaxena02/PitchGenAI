from models.model_loader import load_model
from utils.prompt_templates import PITCH_TEMPLATE

# Load the Phi-3 Mini 4K model
model = load_model()

def generate_pitch(startup_info: dict) -> str:
    prompt = PITCH_TEMPLATE.format(
        name=startup_info.get("name", ""),
        problem=startup_info.get("problem", ""),
        solution=startup_info.get("solution", ""),
        market=startup_info.get("market", ""),
        business_model=startup_info.get("business_model", ""),
        tone=startup_info.get("tone", "formal")
    )
    with model.chat_session() as session:
        response = session.generate(prompt, max_tokens=1024)
    return response
