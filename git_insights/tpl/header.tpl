{% block header %}
<div id="header_block">
    <h3><img src="./img/nxp_logo_small.png">Git Weekly Report</h3>
    <!-- </div>            -->
    <ul class="breadcrumb">
        <li >
            <a class="{% if active == "general" %}active{% endif %}" href="./general.html">general info</a> <span class="divider">/</span>
        </li>
        <li >
            <a class="{% if active == "summary" %}active{% endif %}" href="./index.html">summary report</a> <span class="divider">/</span>
        </li>
        <li >
            <a class="{% if active == "detail" %}active{% endif %}" href="./detail.html">detail report</a>
        </li>
    </ul>
</div>
{% endblock %}