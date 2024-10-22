---
layout: page
title: Certifications
permalink: /certifications
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' %}
{% assign GCP = ordered_posts | where: "category", "badges" | where: "tags", "GCP" %}
{% assign CCDB = ordered_posts | where: "category", "badges" | where: "tags", "CCDB" %}

## Google Cloud Platform
{% include badges.html content = GCP %}

## Digital Research Alliance of Canada
{% include certificates.html content = CCDB %}

<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>