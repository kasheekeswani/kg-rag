import json

INPUT_FILE = "data/pubchem.json"
OUTPUT_FILE = "data/triples1.json"


def convert():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    triples = []

    for item in data:
        drug = item.get("cmpdname")

        if not drug:
            continue

        # 1. Synonyms
        synonyms = item.get("cmpdsynonym", [])
        for syn in synonyms[:10]:
            triples.append({
                "subject": drug,
                "predicate": "has synonym",
                "object": syn
            })

        # 2. Molecular weight
        mw = item.get("mw")
        if mw:
            triples.append({
                "subject": drug,
                "predicate": "has molecular weight",
                "object": str(mw)
            })

        # 3. IUPAC
        iupac = item.get("iupacname")
        if iupac:
            triples.append({
                "subject": drug,
                "predicate": "has IUPAC name",
                "object": iupac
            })

        # 4. Classification
        annotations = item.get("annotation", [])
        for ann in annotations[:5]:
            label = ann.split(">")[-1].strip()

            if " - " in label:
                label = label.split(" - ", 1)[1]

            triples.append({
                "subject": drug,
                "predicate": "is a",
                "object": label
            })

    # Remove duplicates
    unique_triples = list({(t["subject"], t["predicate"], t["object"]) for t in triples})
    unique_triples = [
        {"subject": s, "predicate": p, "object": o}
        for (s, p, o) in unique_triples
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(unique_triples, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(unique_triples)} triples to {OUTPUT_FILE}")


if __name__ == "__main__":
    convert()