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
{% include category.html content = metagenomics %}

## Transcriptomics
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