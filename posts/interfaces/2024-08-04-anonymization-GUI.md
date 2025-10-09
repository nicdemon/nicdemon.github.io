---
date: 2024-08-04
category: interfaces
tag: gui
---

# Barn preprocessing & upload

## A preprocessing and uploading app for barn data in an edge computing setting

:::{margin}
### Team:
* François Gonothi Toure
:::

:::{figure} ../../img/flet-UI.png
:label: preprocessing
:alt: A screenshot of the preprocessing and upload app
:align: center

A screenshot of the preprocessing and upload app
:::

A more advanced version of the [McGill barn video uploads app](/posts/interfaces/2024-06-05-rsync-GUI.md).

This desktop app form preprocesses the video data on-site (a barn) before uploading video files to the WELL-E file storage server. On-site preprocessing consists of multiple operations such as anonymization of barn staff, video trimming, video encryption, etc. to reduce the size of files transferred and to keep security at a maximum.

This app uses [Globus endpoint](https://docs.globus.org/api/transfer/endpoints_and_collections/) to transfer data efficiently as well as private packages to run preprocessing operations locally.

::::{grid} 1 1 2 2

:::{card}

### Contribution:
* Design & build the GUI
* Database design and implementation
* Backend usage of code from other private packages
* Automate preprocessing operations depending on the information filled in the form
* Automate metadata gathering and remote database update depending on the information filled in the form
:::

:::{card}

### Tools:
* Python
* Flet
* SQLite3
* PyTorch
* YOLOv7
* OpenCV
* Pandas
* Seaborn
* Globus endpoints
:::

::::

{button}`Github repository <https://github.com/WELL-E-chair/linux-utils/tree/main/anonymization-GUI>`