from llama_cpp import Llama

print("Loading model...")

llm = Llama(
    model_path="models/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf",
    n_ctx=4096,
    verbose=False,
)

print("Model loaded!")

response = llm.create_chat_completion(
    messages=[
        {
            "role": "user",
            "content": "Introduce yourself in one sentence."
        }
    ]
)

print(response["choices"][0]["message"]["content"])
