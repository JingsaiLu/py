{% set active = "detail" %}

{% extends "base.tpl" %}  

{% block title %}Week commits{% endblock %}  

{% block main %}
<div id="main_block">

    <div id="git_diff_patch">
        <h4>Detail different changes in each commits</h4>
        <pre>{{git_diff_patch}}</pre>
        <!-- <textarea></textarea> -->
    </div>
</div>

{% endblock %}  