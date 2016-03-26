#!/Users/korbenk/octt/flask/lab1/bin/python

from User import User
import os.path
from flask import Flask, send_from_directory

# Setting static_folder=None disables built-in static handler.as
app = Flask(__name__, static_folder="/assets")
# Use folder called 'assets' sitting next to app.py module.
assets_folder = os.path.join(app.root_path, 'assets')

@app.route('/assets/<path:filename>')
def assets(filename):
    # Add custom handling here.
    # Send a file download response.
    return send_from_directory(assets_folder, filename)