{% set active = "general" %}

{% extends "base.tpl" %}  

{% block title %}Week commits{% endblock %}  

{% block main %}
<div id="main_block">
    <div id="general" style="width: 60%; margin: 0 auto;">
        <div>
            <table class="table" style="border:1px solid #ddd">
                <tbody>
                    <tr>
                        <td>Tool version:</td><td>{{general_info.git_version}} </td>
                    </tr>
                    <tr>
                        <td>Date of report:</td><td>{{general_info.gen_date}} </td>
                    </tr>
                    <tr>
                        <td>Git repo:</td><td>{{general_info.git_remote}} </td>
                    </tr>
                    <tr>
                        <td>Git repo path:</td><td>{{general_info.repo_path}} </td>
                    </tr>
                    <tr>
                        <td>Git repo branch:</td><td>{{general_info.repo_branch}} </td>
                    </tr>
                    <tr>
                        <td>Report path:</td><td>{{general_info.output_path}} </td>
                    </tr>
                    <tr>
                        <td>Repo total commits:</td><td>{{general_info.total_commits}} </td>
                    </tr>
                    <tr>
                        <td>Repo total authors:</td><td>{{general_info.total_authors}} </td>
                    </tr>                    
                </tbody>

                
            </table>
            
                       
        </div>

    </div>

</div>

{% endblock %}  