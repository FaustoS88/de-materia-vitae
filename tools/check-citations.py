#!/usr/bin/env python3
"""
De Materia Vitae — Citation Check

Compares every cited PMID in the protocols and their translations with PubMed:
first author, year, journal and, when the line quotes one, the title.
Prints each line that differs and exits 1 if there is any. It fixes nothing.

Usage:
    python tools/check-citations.py
"""

import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["protocols", "translations/it", "translations/es"]
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="

# Common abbreviations used in the manual → PubMed's abbreviation
ABBREVIATIONS = {
    "nejm": "n engl j med",
    "pnas": "proc natl acad sci u s a",
    "jacc": "j am coll cardiol",
}


def norm(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    words = re.sub(r"[^a-z0-9]+", " ", text).split()
    return " ".join(words[1:] if words[:1] == ["the"] else words)


def cited_lines():
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).glob("*.md")):
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                pmid = re.search(r"PMID:?\s*(\d{6,9})", line)
                if not pmid:
                    continue
                if line.startswith("|"):
                    label = line.split("|")[1]
                elif re.match(r"\d+\.\s", line):
                    label = re.sub(r"^\d+\.\s+", "", line[: pmid.start()])
                else:
                    label = line[: pmid.start()]
                yield f"{folder}/{path.name}:{number}", pmid.group(1), label.strip()


def cited_author(label):
    # Vancouver style in prose ("Olds GR."), else the first name of the label ("Estruch et al., 2018")
    vancouver = re.search(r"([A-Z][\w'’-]+) [A-Z]{1,3}\.", label)
    if vancouver:
        return norm(vancouver.group(1))
    return norm(re.split(r"\s+et al|,|\s+&\s+|\s+and\s+", label)[0])


def differences(label, record):
    found = []
    first = record["authors"][0]["name"] if record.get("authors") else ""
    surname = norm(" ".join(first.split()[:-1]) or first)
    author = cited_author(label)
    if not author or author.split()[0] not in surname.split():
        found.append(f"author: cited {author!r}, PubMed {first!r}")
    years = re.findall(r"\b(?:19|20)\d\d\b", record.get("pubdate", "") + " " + record.get("epubdate", ""))
    year = re.search(r"\b(?:19|20)\d\d\b", label)
    if year and year.group(0) not in years:
        found.append(f"year: cited {year.group(0)}, PubMed {record.get('pubdate', '')!r}")
    journal = re.search(r"(?<!\*)\*([^*]+)\*(?!\*)", label)
    if journal:
        cited = norm(journal.group(1))
        if ABBREVIATIONS.get(cited, cited) not in (norm(record.get("source", "")), norm(record.get("fulljournalname", ""))):
            found.append(f"journal: cited {journal.group(1)!r}, PubMed {record.get('source', '')!r}")
    title = re.search(r"[\"“«]([^\"”»]+)[\"”»]", label)
    if title and norm(title.group(1)) != norm(record.get("title", "")):
        found.append(f"title: cited {title.group(1)!r}, PubMed {record.get('title', '')!r}")
    return found


def main():
    lines = list(cited_lines())
    ids = sorted({pmid for _, pmid, _ in lines})
    with urllib.request.urlopen(ESUMMARY + ",".join(ids), timeout=60) as response:
        records = json.load(response)["result"]

    wrong = 0
    for where, pmid, label in lines:
        record = records.get(pmid)
        found = ["not found on PubMed"] if not record or "error" in record else differences(label, record)
        if found:
            wrong += 1
            print(f"{where}  PMID {pmid}  {label}")
            for item in found:
                print(f"    {item}")

    print(f"\n{len(lines)} cited lines, {len(ids)} distinct PMIDs, {wrong} lines differ from PubMed")
    return 1 if wrong else 0


if __name__ == "__main__":
    sys.exit(main())
