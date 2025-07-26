---
layout: page
title: Websites
permalink: /web-ui
---
<!-- Posts preprocessing -->
{% assign ordered_posts = site.posts | sort: 'date' | reverse %}
{% assign web = ordered_posts | where: "category", "web" %}

{% include category.html content = web %}

<script>
    /* Modal reactivity */
    
    // Get elements in variables
    var btn = document.getElementsByClassName("button");
    var modals = document.getElementsByClassName("modal");
    var spans = document.getElementsByClassName("close");

    // For loop to make buttons reactive
    for (let i in btn){
        // Open modal on button click
        btn[i].onclick = function(){
          modals[i].style.display = "block";
        }
        // Close modal on click (x)
        spans[i].onclick = function(){
          modals[i].style.display = "none";
        }
    }
</script>