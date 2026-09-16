---
date: 2026-09-16
---

# Notion monetary data BI

## Streamlit app for Notion data BI

:::{figure} ../../../img/projects/notion-bi.png
:label: notionBI
:alt: A screenshot of the Notion Dashboard web app
:align: center

A screenshot of the Notion Dashboard web app
:::

### 🎯 Project objective
Create a dashboard for tracking money usage and groups investments

### 📋 Project description
A Streamlit Dashboard using data from Notion in a local docker container.

It is used to get insight on money influx for a specific project.

### 🎨 Design & implementation decisions
* Streamlit for visuals and plots
* SQLite for data integration
* API requests to Notion to fetch data
* Docker container for local deployment

### 🧾 Key takeaway
* Integrate data from multiple Notion databases into a local SQLite database
* Making interactive dashboard with Streamlit to create a multipage BI app
* Practice local deployment in local Docker container

::::{grid} 1 1 2 2

:::{card}

### 👨‍💻 Contribution:
* Front-end & Backend
* Data ETL
* Data Analysis
* Deployment
:::

:::{card}

### 🛠 Tools:
* Python3
  * Pandas
  * SQLite3
  * Streamlit
* Notion
* Docker
:::

::::