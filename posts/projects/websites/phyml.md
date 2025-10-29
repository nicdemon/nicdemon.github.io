---
date: 2020-05-05
---

# DESS PhyML project

## PhyML dynamic website implementation

:::{margin}
### Team:
* Abdellatif El Ghizi
* Latifa Mohammadi
* Wanlin Li
:::

:::{figure} img/phyml-web.png
:label: phyml
:alt: Phyml web app landing
:align: center

The PhyML dynamic web app main page
:::

### 🎯 Project objective
Project for a class from the DESS in Bioinformatics

### 📋 Project description
The project consisted of two parts:
1. Create python classes and scripts to use the PhyML linux CLI precompiled binaries
2. Build a web interface for running the PhyML python classes previously created

The web interface enabled the user to run the PhyML binaries via a form and consult the runs history with their results.

### 🎨 Design & implementation decisions
* Python 3 classes for using the PhyML CLI tools
* The web frontend interface uses HTML, JavaScript JQuery, and Bootstrap CSS
* The web backend leverages a Flask server and an SQLite3 database

### 🧾 Key takeaway
* Python 3 classes for CLI tools
* Web design front and back ends

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Backend development
* PhyML python execution class
* Database python interaction class
:::

:::{card}

### 🛠 Tools:
* Python
* Javascript
* JQuery
* HTMl
* Bootstrap CSS
* Flask
* SQLite3
* PhyML
:::

::::

{button}`Github repository <https://github.com/nicdemon/phyml/tree/flask>`