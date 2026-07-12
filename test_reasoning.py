from reasoning.llm import LocalLLM

llm = LocalLLM(
    "models/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf"
)

answer = llm.generate(
    "Explain recursion in a para"
)

print(answer)