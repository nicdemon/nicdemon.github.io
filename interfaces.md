---
layout: page
title: Interfaces
permalink: /interfaces
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' | reverse %}
{% assign web = ordered_posts | where: "category", "web" %}

## Web applications
{% include card_list.html content=web %}
<!-- {% include card_list.html collection=site.data.interfaces.projects %} -->

## Desktop applications
