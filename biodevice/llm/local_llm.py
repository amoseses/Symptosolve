from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path):
        self.model = Llama(
            model_path=str(model_path),
            n_ctx=4096,
            n_threads=4,
            verbose=False,
        )

    def generate(self, prompt):
        response = self.model(
            prompt,
            max_tokens=300,
            temperature=0.2,
            stop=["</s>"],
        )
        return response["choices"][0]["text"].strip()
