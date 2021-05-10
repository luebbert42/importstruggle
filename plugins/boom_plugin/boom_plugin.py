# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
import sys, os,logging
from pprint import pprint

""""
# I want to import TestAppBuilderBaseView, this was working in Airflow 1.x
# from boom_plugin.views.testview import TestAppBuilderBaseView

# Hack: add all subdirectories to path:

def add_all_subs_to_path():
    pypath = os.path.dirname(os.path.abspath(__file__))
    for dir_name in os.listdir(pypath):
      dir_path = os.path.join(pypath, dir_name)
      if os.path.isdir(dir_path):
        sys.path.insert(0, dir_path)
    pprint(sys.path)

add_all_subs_to_path()

# now I can import the file liek this, not satisfying (loosing the nmespaces)
from testview import TestAppBuilderBaseView
"""

###### it works if everything is in one file...  

from flask_appbuilder import expose, BaseView as AppBuilderBaseView
# Creating a flask appbuilder BaseView
class TestAppBuilderBaseView(AppBuilderBaseView):
    default_view = "test"

    @expose("/")
    def test(self):
        return self.render("test_plugin/test.html", content="Hello galaxy!")

######### ignore below, not interesting for the question ##############

# Creating a flask blueprint to integrate the templates and static folder
bp = Blueprint(
    "boom_plugin", __name__,
    template_folder='templates', # registers airflow/plugins/templates as a Jinja template folder
    static_folder='static',
    static_url_path='/static/boom_plugin')


v_appbuilder_view = TestAppBuilderBaseView()
v_appbuilder_package = {"name": "Boom View",
                        "category": "Boom Plugin",
                        "view": v_appbuilder_view}

# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "boom_plugin"
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package]