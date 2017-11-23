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
                <li>
                    <a href="#">主页</a> <span class="divider">/</span>
                </li>
                <li>
                    <a href="#">类目</a> <span class="divider">/</span>
                </li>
                <li class="active">
                    主题
                </li>
            </ul>
            <table class="table" style="text-align: center;">
                <thead>
                    <tr>
                        <th>hash</th>
                        <th>time</th>
                        <th>author</th>
                        <th>title</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>6731879</td>
                        <td>4 hours ago</td>
                        <td>kinsey</td>
                        <td>init git report project</td>
                    </tr>
                    {% for item in git_list %}
                    <tr>
                        <td>{{item[0]}}</td>
                        <td>{{item[1]}}</td>
                        <td>{{item[2]}}</td>
                        <td>{{item[3]}}</td>
                    </tr>    
                    {% endfor %}
                </tbody>
            </table>
            <code>ddddddddddddd</code>
            <section>deeeeeeeeeeeee</section>
            <pre>tttttttttttt
wwww
            swwwwwww
            </pre>
        </div>
    </div>
</div>
<div>

</div>
</body>
</html>