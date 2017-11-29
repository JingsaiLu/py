{% set active = "general" %}

{% extends "base.tpl" %}  

{% block title %}Week commits{% endblock %}  

{% block main %}
<div id="main_block">
    <div id="general">
        <div>
            <dl>
                <dt>Tool version:</dt><dd>{{general_info.git_version}} </dd><br>
                <dt>Date of report:</dt><dd>{{general_info.gen_date}} </dd><br>
                <dt>Git repo:</dt><dd>{{general_info.git_remote}} </dd><br>
                <dt>Git repo path:</dt><dd>{{general_info.repo_path}} </dd><br>
                <dt>Git repo branch:</dt><dd>{{general_info.repo_branch}} </dd><br>
                <dt>Report path:</dt><dd>{{general_info.output_path}} </dd><br>
                <dt>Total commits:</dt><dd>{{general_info.total_commits}} </dd><br>
                <dt>Total author:</dt><dd>{{general_info.total_authors}} </dd><br>
            </dl>
            
                       
        </div>

    </div>

</div>

{% endblock %}  