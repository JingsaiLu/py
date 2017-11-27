<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}NXP Git Weekly Report{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="./css/common.css">
</head>
<body>
    <div class="container-fluid">
        <div class="row-fluid">
            <div class="span12">
                {% include 'header.tpl' %}
                <div id="content">{% block main %}{% endblock %}</div>
            </div>
        </div>
    </div>
    
    {% include 'footer.tpl' %}
</body>
</html>