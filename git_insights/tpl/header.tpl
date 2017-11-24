{% block header %}
<div id="header_block">
    <h3><img src="./img/nxp_logo_small.png">git Insights</h3>
    <!-- </div>            -->
    <ul class="breadcrumb">
        <li class="active">
            <a href="#">commits</a> <span class="divider">/</span>
        </li>
        <li class="{% if active == "summary" %}active{% endif %}">
            <a href="#git_diff_stat">summary</a> <span class="divider">/</span>
        </li>
        <li class="{% if active == "diff" %}active{% endif %}">
            <a href="">diff</a>
        </li>
    </ul>
</div>
{% endblock %}