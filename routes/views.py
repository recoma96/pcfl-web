from uuid import uuid4
import os

from werkzeug.datastructures.file_storage import FileStorage
from flask import Blueprint, render_template, request
from pcfl import pcfl_by_file


blueprint = Blueprint("view", __name__)

@blueprint.get("/")
def index():
    return render_template("index.html")


@blueprint.post("/result")
def result():
    midi_file: FileStorage = request.files["midiFile"]
    serial_number = ''.join((str(uuid4()).split('-')))[:10]

    inupt_root = f"tmp/{serial_number}-input.mid"
    output_root = f"tmp/{serial_number}-output.mid"

    with open(inupt_root, "wb") as f:
        stream = midi_file.stream
        while block := stream.read(300):
            f.write(block)

    pcfl_by_file(inupt_root, output_root)

    os.remove(inupt_root)

    return render_template("result.html", data={"serialNumber": serial_number})
