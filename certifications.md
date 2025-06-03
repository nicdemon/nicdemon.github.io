---
layout: page
title: Certifications
permalink: /certifications
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' %}
<!-- Google Cloud Platform -->
{% assign GCP = ordered_posts | where: "category", "badges" | where: "tags", "GCP" %}
{% assign GCP_skills = GCP | where: "tags", "skill" %}
{% assign GCP_certifications = GCP | where: "tags", "certification" %}
<!-- Microsoft learn -->
{% assign microsoft = ordered_posts | where: "category", "badges" | where: "tags", "microsoft" %}
{% assign microsoft_course = microsoft | where: "tags", "course" %}
{% assign microsoft_lp = microsoft | where: "tags", "learning-path" %}
<!-- AWS -->
<!-- Kaggle -->
{% assign kaggle = ordered_posts | where: "category", "badges" | where: "tags", "kaggle" %}
<!-- Digital Research Alliance of Canada -->
{% assign CCDB = ordered_posts | where: "category", "badges" | where: "tags", "CCDB" %}
<!-- AFI U -->
{% assign AFI-U = ordered_posts | where: "category", "badges" | where: "tags", "AFI-U" %}

## Google Cloud Platform
<!-- Learning paths -> Skill badges -> Completion badge -->
Training done on [Google Cloud Skill Boost](https://www.cloudskillsboost.google/paths).

Certifications are obtained when completing specific learning paths while the skill badges are obtained when completing challenge courses where previously learned concepts are used to complete the scenario. On this platform, course completion badges also exist for when a hands-on course is completed but are not shown here as they are required to get certifications.
### Certifications
{% include badges-embed.html content = GCP_certifications %}
### Skill badges
{% include badges-embed.html content = GCP_skills %}

## Microsoft Learn
<!-- Examen -> Course -> Learning paths -> Modules -->
Training done on [Microsoft Learn](https://learn.microsoft.com/en-us/).

Certifications are awarded when a course is fully completed and the exam is passed successfully. Courses are collections of learning paths aimed to prepare for a certification exam.
The learning path trophies are obtained when completing all modules from a learning path. On this platform, badges are obtained when completing a learning module but they are not shown here as they are required to get learning path trophies.
### Courses
{% include certificates.html content = microsoft_course %}
### Learning path trophies
{% include certificates.html content = microsoft_lp %}

<!-- ## Amazon Web Services -->

## Kaggle
Training done on [Kaggle Learn](https://www.kaggle.com/learn).

Certificates are awarded when both theoritical and applied parts of a course have been completed
{% include certificates.html content = kaggle %}

## Digital Research Alliance of Canada
These certifications were acquired by following courses hosted by the different instances of the [Digital Research Alliance of Canada](https://www.alliancecan.ca/en).
{% include certificates.html content = CCDB %}

<script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>

## AFI-U
These certifications were acquired by following courses given by [AFI U](https://www.afiexpertise.com/).
{% include certificates.html content = AFI-U %}