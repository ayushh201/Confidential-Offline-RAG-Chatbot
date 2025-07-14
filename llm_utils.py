from gpt4all import GPT4All
from config import GGUF_MODEL_PATH

llm = None

def load_llm():
    """
    Loads the offline LLM (.gguf) model only once and returns it.
    Ensures model_path is valid and doesn't allow internet access.
    """
    global llm
    if llm is None:

        llm = GPT4All(
            model_name="Mistral-7B-Instruct-v0.1.Q4_K_M.gguf",  
            model_path=GGUF_MODEL_PATH, 
            allow_download=False 
        )
    return llm

def ask_llm(prompt):
    """
    Sends the prompt to the offline model and returns the generated response.
    """
    model = load_llm()
    return model.generate(prompt)

