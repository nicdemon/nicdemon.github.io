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