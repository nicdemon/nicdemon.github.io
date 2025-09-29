#!/usr/bin/env python3
import argparse
import json
import sys
from yaml import safe_load
from pathlib import Path
import pandas as pd
from feedgen.feed import FeedGenerator
import unist as u
import os

POSTS = []
CHILDREN_POSTS = []
DEFAULTS = {
    "category": "",
    "tag": ""
}

parentDir = Path(__file__).parent.parent

postCardsDirective = {
    "name": "bloglist",
    "doc": "A list of blog posts",
    "arg": {},
    "options": {
        "category": {
            "type": "str",
            "doc": "The category of posts to include"
        },
        "tag": {
            "type": "str",
            "doc": "The tag of posts to include"
        }
    }
}

PLUGIN_SPEC = {
    "name": "Blog posts list",
    "directives": [postCardsDirective]
}

def get_posts(category, tag):

    # Aggregate all posts from the markdown files
    for file in parentDir.rglob("posts/**/*.md"):
        text = file.read_text()
        try:
            _, meta, content = text.split("---", 2)
        except Exception:
            print(f"Skipping file with error: {file}", file=sys.stderr)
            continue
        
        # Load in YAML metadata
        meta = safe_load(meta)
        meta["path"] = file.relative_to(parentDir).with_suffix("")
        if "title" not in meta:
            lines = text.splitlines()
            for i in lines:
                if i.strip().startswith("#"):
                    meta["title"] = i.replace("#", "").strip()
                    break

        # Summarize content
        skip_lines = ["#", "--", "%", "++"]
        content = "\n".join(i for i in content.splitlines() if not any(i.startswith(char) for char in skip_lines))
        N_WORDS = 50
        words = " ".join(content.split(" ")[:N_WORDS])
        if not "author" in meta or not meta["author"]:
            meta["author"] = "Nicolas de Montigny"
        meta["content"] = meta.get("description", words)
        POSTS.append(meta)

    POSTS = pd.DataFrame(POSTS)
    if len(category) > 0:
        POSTS = POSTS[POSTS["category"] == category]
    if len(tag) > 0:
        POSTS = POSTS[POSTS["tag"] == tag]
    POSTS["date"] = pd.to_datetime(POSTS["date"]).dt.tz_localize("America/Toronto")
    POSTS = POSTS.dropna(subset=["date"])
    POSTS = POSTS.sort_values("date", ascending=False)

    # Define card visual for POSTS by category
    for x, row in POSTS.iterrows():
        CHILDREN_POSTS.append(
            {
                "type": "card",
                "url": row['path'],
                "children":[
                    {
                        "type": "cardTitle",
                        "children": [u.text(row["title"])]
                    },
                    {
                        "type": "paragraph",
                        "children": [u.text(row['content'])]
                    },
                    # {
                    #     "type": "footer",
                    #     "children": [
                    #         u.strong([u.text("Date: ")]), u.text(f"{row['date']:%B %d, %Y} | "),
                    #         u.strong([u.text("Author: ")]), u.text(f"{row['author']}"),
                    #     ]
                    # },
                ]
            }
        )

def declare_result(content):
    """Declare result as JSON to stdout

    :param content: content to declare as the result
    """
    # Format result and write to stdout
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)

def run_directive(name, data):
    """Execute a directive with the given name and data

    :param name: name of the directive to run
    :param data: data of the directive to run
    """
    assert name == "bloglist"
    opt = data["node"].get("options",{})
    category = opt.get("category", DEFAULTS["category"])
    tag = opt.get("tag", DEFAULTS["tag"])
    CHILDREN_POSTS = get_posts(category, tag)
    return[{"type":"bloglist", "children": CHILDREN_POSTS}]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        declare_result(run_directive(args.directive, data))
    elif args.transform:
        raise NotImplementedError
    elif args.role:
        raise NotImplementedError
    else:
        declare_result(PLUGIN_SPEC)