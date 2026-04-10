import subprocess

def generate_answer(context, question):
    prompt = f"""
You are a helpful assistant.

Use the context below to answer the question.

Context:
{context}

Question: {question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )

    return result.stdout.decode()