{% block header %}
<div id="header_block">
    <h3><img src="./img/nxp_logo_small.png">git Insights</h3>
    <!-- </div>            -->
    <ul class="breadcrumb">
        <li class="active">
            <a href="#">general info</a> <span class="divider">/</span>
        </li>
        <li class="{% if active == "summary" %}active{% endif %}">
            <a href="./summary.html">summary report</a> <span class="divider">/</span>
        </li>
        <li class="{% if active == "diff" %}active{% endif %}">
            <a href="./detail.html">detail report</a>
        </li>
    </ul>
</div>
{% endblock %}