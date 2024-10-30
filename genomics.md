---
layout: page
title: Genomics
permalink: /genomics
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' | reverse %}
{% assign metagenomics = ordered_posts | where: "category", "genomics" | where: "tags", "metagenomics" %}
{% assign transcriptomics = ordered_posts | where: "category", "genomics" | where: "tags", "transcriptomics" %}

## Metagenomics
Metagenomics projects aim to caracterize the content of a microbial community found in a given environment. These communities can be found in multiple environments such as human gut, soil, plant root system, oceanic water, etc. Often, these communities are caracterized by determining the bacterial species present in one or more sample as well as their abundance. Multiple DNA sequencing technologies can be used to extract DNA present in a sample and computational methods for caracterizing the communities are often specialized to the sequencing technology of DNA extraction method used (16S rRNA or Whole Genome Shotgun).
{% include category.html content = metagenomics %}

## Transcriptomics
Transcriptomics aim to analyse the expression of genes in a given sample taken from one or more individuals. These analysis can be run on RNA or DNA depending on the research interest and the sequencing technology used. For each sequencing types, certain methods exist for processing and analyzing data.
{% include category.html content = transcriptomics %}

<script>
    var coll = document.getElementsByClassName("collapsible");
    var i;
    
    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
          content.style.maxHeight = null;
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
        }
      });
    }
</script>