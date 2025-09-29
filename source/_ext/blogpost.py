from __future__ import annotations
import sys
from collections import defaultdict

import pandas as pd
from pathlib import Path
from docutils import nodes
from yaml import safe_load

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.application import Sphinx
from sphinx.domains import Domain, Index
from sphinx.util.nodes import make_refnode
from sphinx.directives import ObjectDescription
from sphinx.util.typing import ExtensionMetadata
from sphinx.util.docutils import SphinxDirective, SphinxRole

from docutils.parsers.rst import directives

from sphinx_design.cards import CardDirective


class BlogPostDirective(ObjectDescription):
    """A custom directive that describes a blog post"""

    has_content = True
    required_arguments = 2
    option_spec = {
        'category': directives.unchanged_required,
        'tags': directives.unchanged_required
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text = sig)
        return sig
    
    def add_target_and_index(self, name, sig, signode):
        signode['ids'].append(sig)
        if 'category' in self.options:
            category = self.options.get('category')
        if 'tags' in self.options:
            tags = self.options.get('tags')
        
        blogposts = self.env.get_domain('blogposts')
        blogposts.add_posts(sig, category, tags)

class CategoryIndex(Index):
    """A custom index that creates a blog posts matrix and filters to keep category"""

    name = 'category'
    localname = 'BlogPosts Category Index'
    shortname = 'categories'

    def generate(self, docnames = None):
        content = defaultdict(list)

        postsDict = {
            name: (dispname, typ, docname, anchor)
            for name, dispname, typ, docname, anchor, _ in self.domain.get_objects()
        }
        categories_bw = self.domain.data['category']

        # flip categories
        categories_fw = defaultdict(list)
        for post, categories in categories_bw.items():
            for category in categories:
                categories_fw[category].append(post)
        print(categories_fw)

        # convert mapping to required output
        for category, posts in categories_fw.items():
            for post in posts:
                dispname, typ, docname, anchor = postsDict[post]
                content[category].append((dispname, 0, docname, anchor, docname, '', typ))

        content = sorted(content.items())
        return content, True
    
class TagsIndex(Index):
    """A custom index that creates a blog posts matrix and filters to keep tags"""

    name = 'tags'
    localname = 'BlogPosts Tags Index'
    shortname = 'tags'

    def generate(self, docnames = None):
        content = defaultdict(list)

        postsDict = {
            name: (dispname, typ, docname, anchor)
            for name, dispname, typ, docname, anchor, _ in self.domain.get_objects()
        }
        tags_bw = self.domain.data['tags']

        # flip tags
        tags_fw = defaultdict(list)
        for post, tags in tags_bw.items():
            for tag in tags:
                tags_fw[tag].append(post)
        print(tags_fw)

        # convert mapping to required output
        for tag, posts in tags_fw.items():
            for post in posts:
                dispname, typ, docname, anchor = postsDict[post]
                content[tag].append((dispname, 0, docname, anchor, docname, '', typ))

        content = sorted(content.items())
        return content, True

class BlogPostDomain(Domain):
    """A domain for tying together the Directive and Index"""
    
    name = 'blogpost'
    label = 'BlogPost'
    roles = {'ref': XRefRole()}
    directives = {'blogpost': BlogPostDirective}
    indiced = {
        ''
    }




"""
class BlogPostRole(SphinxRole):
    """A role to generate the BlogPost List (inline list)"""
    
    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.inline(text=f'Hello {self.text}!')
        return [node], []

class BlogPostList():
    """A custom index that creates a posts by category / tag matrix"""



class BlogPost(SphinxDirective):
    """A directive to generate the BlogPost List (block list)"""

    has_content = True
    option_spec = {
        'category': directives.unchanged,
        'tags': directives.unchanged
    }

    POSTS = []
    CHILDREN_POSTS = []
    DEFAULTS = {
        "category": "",
        "tag": ""
    }
    N_WORDS = 50
    parentDir = Path(__file__).parent.parent

    def get_posts(self):
        category = None
        tags = None
        if 'category' in self.options:
            category = self.options.get('category')
        if 'tags' in self.options:
            tags = self.options.get('tags')
        for file in self.parentDir.rglob("posts/**/*.md"):
            text = file.read_text()
            try:
                _, meta, content = text.split("---", 2)
            except Exception:
                print(f"Skipping file with error: {file}", file=sys.stderr)
                continue
            
            # Load in YAML metadata
            meta = safe_load(meta)
            meta["path"] = file.relative_to(self.parentDir).with_suffix("")
            if "title" not in meta:
                lines = text.splitlines()
                for i in lines:
                    if i.strip().startswith("#"):
                        meta["title"] = i.replace("#", "").strip()
                        break

            # Summarize content
            skip_lines = ["#", "--", "%", "++"]
            content = "\n".join(i for i in content.splitlines() if not any(i.startswith(char) for char in skip_lines))
            words = " ".join(content.split(" ")[:self.N_WORDS])
            if not "author" in meta or not meta["author"]:
                meta["author"] = "Nicolas de Montigny"
            meta["content"] = meta.get("description", words)
            self.POSTS.append(meta)
        
        self.POSTS = pd.DataFrame(self.POSTS)
        if category:
            self.POSTS = self.POSTS[self.POSTS["category"] == category]
        if tags:
            self.POSTS = self.POSTS[self.POSTS["tags"] == tags]
        self.POSTS["date"] = pd.to_datetime(self.POSTS["date"]).dt.tz_localize("America/Toronto")
        self.POSTS = self.POSTS.dropna(subset=["date"])
        self.POSTS = self.POSTS.sort_values("date", ascending=False)

        #################################
        # For testing
        print(self.POSTS)
        self.POSTS = self.POSTS.to_dict()
        #################################

        # TODO: Define Card visual for posts

    def run(self) -> list[nodes.Node]:
        nodesList = []
        self.get_posts()
        nodesList.append(nodes.paragraph(text=self.POSTS))
        # if 'category' in self.options:
        #     catNode = nodes.paragraph(text=f'Category: {self.options.get('category')}')
        #     nodesList.append(catNode)
        # if 'tags' in self.options:
        #     tagNode = nodes.paragraph(text=f'Tags: {self.options.get('tags').split(', ')}')
        #     nodesList.append(tagNode)
        return nodesList
"""

def setup(app: Sphinx) -> ExtensionMetadata:
    # app.add_role('bloglist', BlogPostRole)
    # app.add_directive('bloglist', BlogPost)
    # app.add_directive('bloglist', BlogPostList)
    app.add_domain(BlogPostDomain)

    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }