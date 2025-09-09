# MWA Member Clubs

{% for club in clubs %}
## {{club.name}}

<div class="grid cards" markdown>

-   {% for person in club.directory if person.feature %}**{{person.role}}:** {{person.name}} {% if person.note %}({{person.note}}){% endif %}

{% if person.website %}
    :   ([{{person.website}}](http://{{person.website}}))
{% endif %}
{% endfor %}

-   {% if club.website %}[**{{club.website}}**](http://{{club.website}}){% endif %}

    **{{club.event}} {{club.days}},** {{club.time}}

{% if club.months %}
    :   {{club.months}}{% endif %}

    **{{club.hall}}**

    :   {{club.address}} {{club.city}}

    {% if club.dark %}**Dark:** {{club.dark}}{% endif %}

</div>

[{{club.name}} Directory](/directory/#{{club.id}})

---
{% endfor %}

