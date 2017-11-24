{% extends "base.tpl" %}  

{% block title %}Week commits{% endblock %}  

{% block main %}
<div id="main_block">
    <h4>Recent week commits: {{git_list|length}}</h4>
    <table class="table" style="text-align: center;">
        <thead>
            <tr>
                <th>index</th>
                <th>hash</th>
                <th>time</th>
                <th>author</th>
                <th>title</th>
            </tr>
        </thead>
        <tbody>
            {% for item in git_list %}
            <tr>
                <td>{{loop.index}}</td>
                <td>{{item[0]}}</td>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
                <td>{{item[3]}}</td>
            </tr>    
            {% endfor %}
        </tbody>
    </table>
</div>

{% endblock %}  