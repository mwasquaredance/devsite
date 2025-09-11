# MWA Member Clubs

{% for club in clubs %}
## {{club.name}}

{% set featured = club.directory | selectattr('feature') | list %}
<div class="grid cards" markdown>

{% if featured %}
-   {% for person in club.directory if person.feature %}
    **{{person.role}}:** {{person.name}} {% if person.note %}({{person.note}}){% endif %}
    {% if person.website %}
    :   :material-open-in-new: [{{person.website}}](http://{{person.website}})
    {% endif %}
    {% endfor %}

{% endif %}
-   **{{club.event}} {{club.days}},** {{club.time}}{% if club.months %} — {{club.months}}{% endif %}

    {% if club.dark %}
    :   **Dark:** {{club.dark}}{% endif %}

    **{{club.hall}}**
    :   {{club.address}} {{club.city}}

    {% if club.website %}:material-open-in-new: [**{{club.website}}**](http://{{club.website}}){% endif %}

</div>

[{{club.name}} Directory](../council/directory.md#{{club.slug}})

---
{% endfor %}

