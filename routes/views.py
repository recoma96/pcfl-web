from flask import Blueprint, render_template

blueprint = Blueprint("view", __name__)

@blueprint.get("/")
def indeX():
    return render_template("index.html")
