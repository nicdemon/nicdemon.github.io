---
layout: page
title: Certifications
permalink: /certifications
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' %}
<!-- Google Cloud Platform -->
{% assign GCP = ordered_posts | where: "category", "badges" | where: "tags", "GCP" %}
{% assign GCP_badges = GCP | where: "tags", "badge" %}
{% assign GCP_certifications = GCP | where: "tags", "certification" %}
<!-- Digital Research Alliance of Canada -->
{% assign CCDB = ordered_posts | where: "category", "badges" | where: "tags", "CCDB" %}

## Google Cloud Platform
### Learning paths
{% include badges.html content = GCP_certifications %}
### Course badges
{% include badges.html content = GCP_badges %}

## Digital Research Alliance of Canada
{% include certificates.html content = CCDB %}

<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>