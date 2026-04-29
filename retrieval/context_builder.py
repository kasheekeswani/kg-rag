def build_context(results):
    if not results:
        return "No relevant information found."

    context_lines = []

    for u, r, v in results:

        if r == "is_a":
            context_lines.append(f"{u} is a {v}.")

        elif r == "has_synonym":
            context_lines.append(f"{u} is also known as {v}.")

        elif r == "has_iupac_name":
            context_lines.append(f"The IUPAC name of {u} is {v}.")

        elif r == "has_molecular_weight":
            context_lines.append(f"{u} has a molecular weight of {v}.")

        else:
            # fallback (important)
            context_lines.append(f"{u} {r} {v}.")

    return "\n".join(context_lines)