import yaml
from flask import Flask, render_template
from pydantic import BaseModel


class Project(BaseModel):
    name: str
    authors: str
    description: str
    ready: bool = False


app = Flask(__name__)

with open('projects.yml', 'r') as yml_file:
    yml_content = yaml.safe_load(yml_file)
    projects = [Project(**project) for project in yml_content]


@app.route("/")
def index():
    return render_template('index.html', projects=projects)
