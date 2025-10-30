---
date: 2020-07-04
---
# Armillaria sinapina article

## A First Insight into North American Plant Pathogenic Fungi Armillaria sinapina Transcriptome

:::{margin}
### Team:
* Dre Narimene Fradj
* Dre Natacha Mérindol
* Dre Fatima Awwad
* Pr Yacine Boumghar
* Pr Hugo Germain
* Pre Isabel Desgagné-Penix
:::

### 🎯 Project objective
Follow-up project of the [*Inonotus Obliquus* article](2019-09-04-inonotus-obliquus.md) on *Armillaria Sinapina*.

The study is similar to the first one and aimed to:
1. Produce similar results for another fungi sequencing experimentation
2. Extend the results previously produced to increase significativity

### 📋 Project description
Working with RNA-Seq sequencing data, the project aimed to characterise the metabolic pathway leading to terpenoids molecules (eg., betulin, betulinic acid and inotodiol) production in *Armillaria sinapina* fungi. It also aimed to extend the analysis that was done on *Inonotus Obliquus* with other methods and databases to better characterize the metabolomic pathways.

As with Chaga, *Armillaria sinapina* was cultured in three environments to determine the optimal environment for terpenoids production. From these three cultures, RNA was extracted and sequenced to study their transcriptome.

To do so, reads were aligned to a consensus genome and were then assigned functions both using the Gene Ontology database and the KEGG database. This research project was part of Dre Narimene Fradj's PhD project and led to an article in IJMS.

### 🎨 Implementation decisions
* Statistical analysis and graphs were performed with R programming language.
* Usage of Gene Ontologies for mapping reads
* Extend reads mapping with KEGG pathways

### 🧾 Key takeaway
* First contact in working with sequencing data
* First experience in reads mapping and KEGG pathways analysis
* Reinforcement of statistical analysis and use of R programming language

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* RNA-seq data analysis between two culture mediums
* Data vizualisation and exploration
* Graphics and layouts
:::

:::{card}

### 🛠 Tools:
* R
* ggplot2
* tidyr
* plotly graphs
:::

::::

{button}`Article <https://doi.org/10.3390/biology9070153>`
{button}`Github repository <https://github.com/nicdemon/armillaria-sinapina.git>`