---
layout: post
location: UQAM
title: Barn preprocessing & upload
image: /assets/img/flet-UI.png
category: gui
tag: 
description: A more advanced version of the <em>McGill barn video uploads app</em>. This desktop app form preprocesses the video data on-site (a barn) before uploading video files to the WELL-E file storage server. On-site preprocessing consists of multiple operations such as anonymization of barn staff, video trimming, video encryption, etc. to reduce the size of files transferred and to keep security at a maximum. This app uses <a href="https://docs.globus.org/api/transfer/endpoints_and_collections/" target="_blank">Globus endpoints</a> to transfer data efficiently as well as private packages to run preprocessing operations locally.
contributors: François Gonothi Toure
tasks: Design & build the GUI, Database design and implementation, Backend usage of code from other private packages, Automate preprocessing operations depending on the information filled in the form, Automate metadata gathering and remote database update depending on the information filled in the form
tools: Python, <a href="https://flet.dev/" target="_blank">Flet</a>, SQLite3, PyTorch, YOLOv7, OpenCV, Pandas, Seaborn
article: 
github: https://github.com/WELL-E-chair/linux-utils/tree/main/anonymization-GUI
website: 
---