{% set active = "summary" %}

{% extends "base.tpl" %}  

{% block title %}Week commits{% endblock %}  

{% block main %}
<div id="main_block">
    <div id="commits">
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
                    <td>
                        <div id='commit_id' class="commit_id btn btn-success" title="Commit files"
                        data-container="body" data-toggle="popover" data-placement="right" data-html='true'
                        data-content="{{commits_stat[item[0]]}}">{{item[0]}}</div>
                        <div id='commit_files' class="commit_files">hhhh</div>
                    </td>
                    <td>{{item[1]}}</td>
                    <td>{{item[2]}}</td>
                    <td>{{item[3]}}</td>
                </tr>    
                {% endfor %}
            </tbody>
        </table>        
    </div>
    <div id="git_diff_stat">
        <h4>Recent week commit files</h4>
        <pre>{{git_weekly_diff}}</pre>
    </div>

<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script type="text/javascript" src="./js/common.js"></script>
</div>

{% endblock %}  
