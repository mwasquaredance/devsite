# MWA Member Clubs

{% for club in clubs %}
## {{club.name}}

<div class="grid cards" markdown>

-   {% for feat in club.directory where feature=true %}**{{feat.role}}:** {{feat.name}} {% if feat.website %}({{feat.note}}){% endif %}

{% if feat.website %}
    :   ([{{feat.website}}](http://{{feat.website}}))
{% endif %}
{% endfor %}

-   {% if club.website %}[**{{club.website}}**](http://{{club.website}}){% endif %}

    **{{club.event}} {{club.days}},** {{club.time}}

{% if club.website %}
    :   {{club.months}}{% endif %}

    **{{club.hall}}**

    :   {{club.address}} {{club.city}}

    {% if club.website %}**Dark:** {{club.dark}}{% endif %}

</div>

[{{club.name}} Directory](/directory/#{{club.id}})

---
{% endfor %}

