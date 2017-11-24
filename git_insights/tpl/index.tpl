{% set active = "summary" %}
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>NXP git Insights</title>
    <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
</head>
<body>
    <div class="container-fluid">
    <div class="row-fluid">

        <div class="span12">
            <!-- <div class="page-header"> -->
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
            <div id="git_diff_stat"><pre>{{git_diff_stat}}</pre></div>

        </div>
    </div>
</div>
<div>

</div>
</body>
</html>