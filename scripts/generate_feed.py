#!/usr/bin/env python3
"""Generate feed.xml (Atom 1.0) from articles/index.json."""

import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "articles", "index.json")
FEED = os.path.join(ROOT, "feed.xml")
SITE = "https://tiboitel.github.io"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def build_feed():
    with open(INDEX) as f:
        articles = json.load(f)

    feed_updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if articles:
        feed_updated = articles[0]["date"] + "T00:00:00Z"

    ns = "http://www.w3.org/2005/Atom"
    ET.register_namespace("", ns)

    feed = ET.Element(f"{{{ns}}}feed")
    ET.SubElement(feed, f"{{{ns}}}title").text = "Timothee Boitelle — Blog"
    ET.SubElement(feed, f"{{{ns}}}link", href=SITE)
    ET.SubElement(feed, f"{{{ns}}}id").text = SITE + "/"
    ET.SubElement(feed, f"{{{ns}}}updated").text = feed_updated
    author = ET.SubElement(feed, f"{{{ns}}}author")
    ET.SubElement(author, f"{{{ns}}}name").text = "Timothee Boitelle"
    ET.SubElement(feed, f"{{{ns}}}generator").text = "generate_feed.py"

    for a in articles:
        slug = a["slug"]
        title = a["title"]
        date = a["date"]
        summary = a.get("summary", "")
        url = f"{SITE}/article.html?slug={slug}"
        entry_id = f"tag:tiboitel.github.io,{date}:/{slug}"

        entry = ET.SubElement(feed, f"{{{ns}}}entry")
        ET.SubElement(entry, f"{{{ns}}}title").text = title
        ET.SubElement(entry, f"{{{ns}}}link", href=url)
        ET.SubElement(entry, f"{{{ns}}}id").text = entry_id
        ET.SubElement(entry, f"{{{ns}}}published").text = date + "T00:00:00Z"
        ET.SubElement(entry, f"{{{ns}}}updated").text = date + "T00:00:00Z"

        if summary:
            content = ET.SubElement(entry, f"{{{ns}}}content", type="html")
            content.text = f"<p>{escape_html(summary)}</p>"

            ET.SubElement(entry, f"{{{ns}}}summary").text = summary

    tree = ET.ElementTree(feed)
    ET.indent(tree, space="  ")
    tree.write(FEED, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {FEED} ({len(articles)} entries)")

if __name__ == "__main__":
    build_feed()
