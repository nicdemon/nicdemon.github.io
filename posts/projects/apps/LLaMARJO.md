---
date: 2024-05-06
---

# LLaMARJO webapp

## Livestock labeling Learning for Manual Analysis & Recognition as a Journal of Observations webapp

:::{margin}
### Team:
* Momar Aly Dom Fall
:::

:::{figure} img/LLaMARJO-UI.png
:label: llamarjo
:alt: An example screenshot of the LLaMARJO webapp
:align: center

An example screenshot of the LLaMARJO webapp
:::

### 🎯 Project objective
Ease the learning and evaluation process of behavior annotation in videos both for the teacher and the student.

### 📋 Project description
LLMARJO is a software that enables user-centric learning in the processes of behavior annotation.

The process for training in LLAMARJO is similar to machine learning, meaning that three datasets are defined per user for training, validating and testing their skills. The datasets were previously annotated by domain experts and annotations are supplied only for training data to the student.

After having created a learning course for the student, the teacher is there to provide feedback but doesn't need to accompany the student in the whole process. The learning process is handled by the student enabling them to learn, practice and get certified by the system at their own pace. Afterwards, the teacher only need to confirm the evaluations before accrediting the students for production tasks.

### 🎨 Design & implementation decisions
* AppSheet low code application development
* Text-to-Speech for audio description of the behaviors
* Google Drive video files storage

### 🧾 Key takeaway
* Learn to work in AppSheet
* Learn to work in an agile way
* Learn the importance of Proof-of-Concepts before scaling

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Global design
* Data preprocessing
* Database building
* Data storage in Google Drive
:::

:::{card}

### 🛠 Tools:
* Google AppSheet
* Python
* Pandas
* FFmpeg
* Google Drive API
* Youtube API
* Speech T5 by Microsoft from Hugging Face Hub
:::

::::

{button}`Github repository <https://github.com/WELL-E-chair/LLaMARJO>`