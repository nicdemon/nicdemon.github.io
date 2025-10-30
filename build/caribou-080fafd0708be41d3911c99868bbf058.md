---
date: 2024-01-14
---
# Master's thesis research project

## Design of a machine learning approach for bacterial microorganisms detection in metagenomic sequencing without alignment procedures

:::{margin}
### Team:
* Dr Amine M. Remita
* Pr Steven W. Kembel (co-director)
* Pr Abdoulaye Baniré Diallo (co-director)
:::

:::{figure} ../../../img/projects/caribou-algo.png
:label: caribou-workflow
:alt: Workflow view of the Caribou pipeline
:align: center

The Caribou pipeline workflow
:::

### 🎯 Project objective
Prior to the project, it was observed that metagenomic sequencing studies often wield results based on a fraction of the data collected from the biological samples. Also, few methods for metagenomic sequencing reads were based on machine learning (ML) methods. Moreover, previous projects in the Diallo laboratory were led to leverage ML methods to classify viral sequencing reads without alignment procedures.

Building on this, the present research project aimed to design and develop a method for classifying bacterial sequencing reads by leveraging ML methods without alignment procedures, and try to valorise a maximum number of reads produced from the original sample. This project was led for my master's thesis.

### 📋 Project description
To achieve the goal, a pipeline made of four modules was designed.
1. Data preparation and ingestion
2. Bacterial reads extraction
3. Bacterial reads classification
4. Results output for biological analysis

For both ML steps, multiple models using different methods were used. All models were trained, validated, tested and performances were compared to others trained for the same task in an effort to provide a default method to use in the pipeline as well as optimise the classification performances.

### 🎨 Design decisions
* Python 3 programming language
* Data ingestion and management using [Ray](https://docs.ray.io/en/master/) for parallelization and [Pandas](https://pandas.pydata.org/) for subset operations 
* Machine learning models using [Scikit-Learn](https://scikit-learn.org/stable/index.html) and [Keras](https://keras.io/)
* Machine learning parallel training and inferencing using [Ray](https://docs.ray.io/en/master/)
* Synthetic data generation using [InSilicoSeq](https://github.com/HadrienG/InSilicoSeq)
* Computationnaly demanding operations ran on [Canadian Numerical Research Alliance](https://docs.alliancecan.ca/wiki/Technical_documentation) clusters

### 🧾 Key takeaway
* ML pipeline design
* Biological data knowledge
* Parallel computing & Ml training

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Design
* Implementation & development
* Model training, validation & testing
* Pipeline testing
:::

:::{card}

### 🛠 Tools:
* Python
* Tensorflow
* Keras
* Scikit-Learn
* Ray
* Pandas
* Numpy
* PyArrow
* Biopython
* InSilicoSeq
:::

::::

{button}`Thesis (in french) <https://archipel.uqam.ca/18182/>`
{button}`Github repository <https://github.com/bioinfoUQAM/Caribou>`
