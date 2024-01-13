import os
from flask import Blueprint, render_template, send_file


blueprint = Blueprint('api', __name__)


@blueprint.get("/download/<serial_number>")
def download(serial_number: str):
    full_root = f"tmp/{serial_number}-output.mid"
    if not os.path.exists(full_root):
        return render_template("404.html")

    return send_file(full_root, as_attachment=True, download_name="output.mid")
