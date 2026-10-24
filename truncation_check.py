"""Show what the model actually reads after the 128-token cap.

Run:  python truncation_check.py
"""
import csv
from collections import defaultdict

from transformers import AutoTokenizer

MODEL = "distilbert-base-uncased"
MAX_LENGTH = 128

tokenizer = AutoTokenizer.from_pretrained(MODEL)

with open("labels.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

lengths = defaultdict(list)
for row in rows:
    n = len(tokenizer(row["text"])["input_ids"])
    lengths[row["label"]].append(n)

print(f"Posts longer than {MAX_LENGTH} tokens, by label:")
print("| Label | Posts | Truncated | Share | Median tokens |")
print("|---|---:|---:|---:|---:|")
for label, ns in sorted(lengths.items()):
    over = sum(n > MAX_LENGTH for n in ns)
    median = sorted(ns)[len(ns) // 2]
    print(f"| `{label}` | {len(ns)} | {over} | {over / len(ns):.0%} | {median} |")

print("\nDecoded inputs for the first truncated post of each label:\n")
seen = set()
for row in rows:
    if row["label"] in seen:
        continue
    ids = tokenizer(row["text"], truncation=True, max_length=MAX_LENGTH)["input_ids"]
    full = len(tokenizer(row["text"])["input_ids"])
    if full <= MAX_LENGTH:
        continue
    seen.add(row["label"])
    print(f"--- {row['label']} ({full} tokens, model sees {len(ids)})")
    print(tokenizer.decode(ids, skip_special_tokens=True))
    print()
