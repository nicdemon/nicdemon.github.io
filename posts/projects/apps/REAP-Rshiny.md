---
date: 2018-02-18
---

# REAP data visualization

## RShiny app for data visualization of REAP results

:::{margin}
### Team:
* Dre Johanne Poudrier
:::

:::{figure} img/REAP-demo-web.png
:label: reap-demo
:alt: The landing screen of the REAP demo Shiny app 
:align: center

The landing screen of the REAP demo Shiny app
:::

### 🎯 Project objective
Build an interactive interface for biologists to explore Rapid Extracellular Antigen Profiling (REAP) per patient and/or per molecule.

### 📋 Project description
Design and implement an interface for biologists to explore data in a visual way.

The interface allows biologists to explore the data in three panels.
1. Query molecules and visualize either expression per patient of the expression distribution in the whole population or selected individuals group
2. Vizualise and explore heatmaps for which antigen groups and patients populations were defined to be of interest by Dr Poudrier
3. Build custom heatmaps by selecting antigens and patients from both lists

### 🎨 Design & implementation decisions
* R programming language
* Interactive interface and deployment using RShiny
* Choice of graphs and visuals with end-users for optimal usability

### 🧾 Key takeaway
* RShiny
* Usefulness of interactive data exploration for clients

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Create original exploration graphs
* Design & develop RShiny application
* Ensure availability of application for users
* Design & add features upon user request
:::

:::{card}

### 🛠 Tools:
* R
* plotly
* ggplot2
* RShiny
* R tidyverse
:::

::::

{button}`Github repository <https://github.com/nicdemon/REAP-demo>`
{button}`Online demo app <https://nicdemon.shinyapps.io/REAP-demo/>`
