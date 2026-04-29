import subprocess
import re


def generate_answer(context, question):
    # -------------------------
    # 🚫 HARD STOP (no context → no answer)
    # -------------------------
    if not context or context.strip() == "" or "No relevant" in context:
        return "⚠️ Not found in knowledge graph."

    # -------------------------
    # 🔒 STRICT PROMPT (ANTI-HALLUCINATION)
    # -------------------------
    prompt = f"""
You are a strict Knowledge Graph assistant.

RULES (VERY IMPORTANT):
- Answer ONLY using the provided context
- DO NOT use any external or prior knowledge
- DO NOT guess or add information
- If the answer is not clearly in the context, say: "Not found in knowledge graph"
- Keep the answer factual and concise

Context:
{context}

Question:
{question}

Answer:
"""

    # -------------------------
    # 🧠 Run local LLM (Mistral via Ollama)
    # -------------------------
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # -------------------------
    # 🧹 Clean output
    # -------------------------
    output = result.stdout.decode("utf-8", errors="ignore")

    # remove non-ascii garbage
    output = re.sub(r"[^\x00-\x7F]+", " ", output)

    # normalize spaces
    output = re.sub(r"\s+", " ", output).strip()

    # -------------------------
    # 🚨 SAFETY FILTER (extra guard)
    # -------------------------
    if len(output) > 500:
        output = output[:500] + "..."

    return output