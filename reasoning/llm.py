from llama_cpp import Llama


class LocalLLM:
    def __init__(self, model_path: str):
        print("Loading Local LLM...")

        self.model = Llama(
            model_path=model_path,
            n_ctx=4096,
            verbose=False,
        )

        print("Local LLM Ready!")

    def generate(self, prompt: str) -> str:

        response = self.model.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        return response["choices"][0]["message"]["content"]