# Mid-Willamette Area Directory

## {{council.icon}} Area Officers 2025-2026 

{% for person in council.directory%}
???{% if person.role == "President" %}+{% endif %} example "{{person.role}} • {{person.name}}"
    <div class="grid" markdown>

    {% if person.phone %}:material-phone-classic: [{{person.phone}}](tel:+1{{person.phone}}){% endif %}

    {% if person.email %}:material-email-heart-outline: [{{person.email}}](mailto:{{person.email}}){% endif %}

    {% if person.address %}:material-map-marker: {{person.address}}, {{person.city}}{% endif %}

    {% if person.website %}:material-open-in-new: [{{person.website}}](http://{{person.website}}){% endif %}

    </div>
{% endfor %}

{% for club in clubs %}
## {{club.icon}} {{club.name}}

{% for person in club.directory%}
???{% if person.role == "President" %}+{% endif %} note "{{person.role}} • {{person.name}}"
    <div class="grid" markdown>

    {% if person.phone %}:material-phone-classic: [{{person.phone}}](tel:+1{{person.phone}}){% endif %}

    {% if person.email %}:material-email-heart-outline: [{{person.email}}](mailto:{{person.email}}){% endif %}

    {% if person.address %}:material-map-marker: {{person.address}}, {{person.city}}{% endif %}

    {% if person.website %}:material-open-in-new: [{{person.website}}](http://{{person.website}}){% endif %}

    </div>
{% endfor %}

{% endfor %}