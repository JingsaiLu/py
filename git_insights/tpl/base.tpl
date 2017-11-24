<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{% block title %}NXP git Insights{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
</head>
<body>
    {% include 'header.tpl' %}
    <div class="container-fluid">
        <div class="row-fluid">
            <div class="span12">
                <div id="content">{% block main %}{% endblock %}</div>
            </div>
        </div>
    </div>
    
    {% include 'footer.tpl' %}
</body>
</html>