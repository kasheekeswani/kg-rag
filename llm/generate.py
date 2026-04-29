import subprocess
import re

def generate_answer(context, question):
    prompt = f"""
You are an intelligent assistant.

Use ONLY the context to answer the question clearly and in detail.
Combine multiple facts into a meaningful explanation.

Context:
{context}

Question: {question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # decode output
    output = result.stdout.decode("utf-8", errors="ignore")

    # remove weird characters
    output = re.sub(r"[^\x00-\x7F]+", " ", output)

    # clean whitespace
    return output.strip()