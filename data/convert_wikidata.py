import json

INPUT_FILE = "data/wikidata.json"
OUTPUT_FILE = "data/triples.json"

def convert():
    # Load data
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    triples = []

    # Your JSON is a LIST (not nested)
    for item in data:
        scientist = item.get("scientistLabel")
        field = item.get("fieldLabel")
        known_for = item.get("knownForLabel")

        # Add: scientist -> field
        if scientist and field:
            triples.append({
                "subject": scientist,
                "relation": "works_in",
                "object": field
            })

        # Add: scientist -> known_for
        if scientist and known_for:
            triples.append({
                "subject": scientist,
                "relation": "known_for",
                "object": known_for
            })

    # Remove duplicates
    unique_triples = [dict(t) for t in {tuple(d.items()) for d in triples}]

    # Save output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(unique_triples, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(unique_triples)} triples to {OUTPUT_FILE}")


if __name__ == "__main__":
    convert()