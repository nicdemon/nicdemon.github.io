---
date: 2020-03-27
---
# DESS Metagenomic analysis

## Metagenome data analysis remake from a reference article

:::{margin}
### Team:
* Abdellatif El Ghizi
:::

### 🎯 Project objective
This is a session project for two classes at UQAM during the DESS in bioinformatics.
* Bioinformatics structures
* Bioinformatics in health sciences


### 📋 Project description
An article was chosen to fetch data from and was then analyzed using an alternate pipeline to familiarize with CLI genomic analysis tools and recreate results obtained in the original article.

The original article analyzed the microbiota of a key human population in HIV resistance. Therefore the project started with the data provided with the researchers for this article.

### 🎨 Implementation decisions
* Tests we done using the [Metawrap pipeline](https://github.com/bxlab/metaWRAP).
* Microbiota analysis was done using the [Mothur pipeline](https://mothur.org/).
* Computing resources from the [Canadian Numerical Research Alliance](https://docs.alliancecan.ca/wiki/Technical_documentation) were used.
* Characterization of microbiota populations using taxonomic trees

### 🧾 Key takeaway
* Exploration of metagenomic data analysis
* Exploration of taxonomic trees generation methods

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Retrieve the raw sequencing data
* Quality control of the data
* Curate the data according to QC
* Run the Mothur analysis pipeline on the data
* Run the MetaWrap analysis pipeline on the data
* Use HPC an server from the Digital Research Alliance of Canada for the analysis
* Assemble genomes present in the sequencing data
* Plot the results of the analysis
:::

:::{card}

### 🛠 Tools:
* Mothur pipeline
* MetaWrap pipeline
* Béluga HPC cluster (Digital Research Alliance of Canada)
* Kraken
* R
* Bash
:::

::::

{button}`Original article <https://doi.org/10.1371/journal.pone.0213975>`
