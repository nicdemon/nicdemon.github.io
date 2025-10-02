#!/usr/bin/env python3
import os
import sys
import json
import argparse
import unist as u
import pandas as pd
from pathlib import Path
from yaml import safe_load

POSTS = []
N_WORDS = 50
DEFAULTS = {
    "category": "",
    "tag": ""
}

parentDir = Path(__file__).parent.parent

PLUGIN_SPEC = {
    "name": "Blog posts list",
    "directives": [{
        "name": "bloglist",
        "doc": "A list of blog posts",
        "arg": {},
        "options": {
            "category": {
                "type": "string",
                "doc": "The category of posts to include"
            },
            "tag": {
                "type": "string",
                "doc": "The tag of posts to include"
            }
        }
    }]
}

def get_posts(category, tag):
    """
    Fetch posts by category and tag in the YAML header
    """
    # Aggregate posts
    posts = []
    for file in parentDir.rglob(f'posts/{category}/*.md'):
        text = file.read_text()
        try:
            _, meta, content = text.split("---", 2)
        except:
            print(f"Skipping file with error: {file}", file=sys.stderr)
            continue
        
        # Load YAML metadata
        meta = safe_load(meta)
        if meta['tag'] == tag:
            meta["path"] = file.relative_to(parentDir).with_suffix("")
            if "title" not in meta:
                lines = text.splitlines()
                for line in lines:
                    if line.strip().startswith("#"):
                        meta["title"] = line.replace("#", "").strip()
                        break

            # Summarize content
            skip_lines = ["#", "--", "%", "++"]
            content = "\n".join(i for i in content.splitlines() if not any(i.startswith(char) for char in skip_lines))
            words = " ".join(content.split(" ")[:N_WORDS])
            meta["author"] = "Nicolas de Montigny"
            meta["content"] = meta.get("description", words)
            posts.append(meta)

    # Define posts dict
    posts = pd.DataFrame(posts)
    posts["date"] = pd.to_datetime(posts["date"]).dt.tz_localize("America/Toronto")
    posts = posts.dropna(subset=["date"])
    posts = posts.sort_values("date", ascending=False)
    return get_children_posts(posts)

def get_children_posts(posts):
    """
    Fetch posts by tag from a list of posts filtered by category
    """
    CHILDREN_POSTS = []
    for x, row in posts.iterrows():
        CHILDREN_POSTS.append({
            "type": "card",
            "url": f"/{row['path'].with_suffix("")}",
            "children": [
                {
                    "type": "cardTitle",
                    "children": [u.text(row["title"])]
                },
                {
                    "type": "paragraph",
                    "children": [u.text(row['Summary'])] # [u.text(row['content'])]
                },
                {
                    "type": "footer",
                    "children": [
                        u.strong([u.text("Date: ")]), u.text(f"{row['date']:%B %d, %Y}")
                    ]
                }
            ]
        })
    return [u.grid([1,1,2,2], CHILDREN_POSTS)]

def run_directive(name, data):
    """
    Execute a directive with the given name and data

    :param name: name of the directive to run
    :param data: data of the directive to run
    """
    assert name == "bloglist"

    # bloglist = {}
    opt = data["node"].get("options",{})
    category = opt.get("category", DEFAULTS["category"])
    tag = opt.get("tag", DEFAULTS["tag"])
    CHILDREN_POSTS = get_posts(category, tag)

    return CHILDREN_POSTS

def declare_result(content):
    """
    Declare result as JSON to stdout

    :param content: content to declare as the result
    """
    # Format result and write to stdout
    json.dump(content, sys.stdout, indent=2)
    # Successfully exit
    raise SystemExit(0)

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