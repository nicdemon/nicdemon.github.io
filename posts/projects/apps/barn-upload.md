---
date: 2024-06-05
---

# McGill barn video uploads

## A desktop interface for uploading videos from the barn

:::{margin}
### Team:
* 
:::

:::{figure} img/narvalUpload-UI.png
:label: narvalUpload
:alt: A screenshot of the uploader interface
:align: center

A screenshot of the uploader interface
:::

### 🎯 Project objective
Enable biologists to upload data to the remote storage from the barn using secure and fast protocols.

### 📋 Project description
This project was to create a simple desktop app form to upload folders to the remote file storage server from the experiment barn.

Leveraging the `rsync` linux command from a Windows Subsystem Linux (WSL) instance the software uploaded data over SSH.

Using a desktop GUI eases the use by biologists gathering data in the barn. 

### 🎨 Design & implementation decisions
* `rsync` protocol for data transfer over SSH
* Automated remote actions on the storage server
* Python 3 interface compiled into Windows binaries

### 🧾 Key takeaway
* GUI building
* Remote connections in Python 3
* Windows and WSL interoperability scripting

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Design & build the GUI
* Backend operations

:::

:::{card}

### 🛠 Tools:
* Windows Subsystem Linux (WSL)
* rsync
* Python
* PySimpleGUI
* auto-py-to-exe
:::

::::

{button}`Github repository <https://github.com/WELL-E-chair/windows-utils/tree/main/rsync>`