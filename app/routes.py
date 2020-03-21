from flask import render_template, flash, redirect, url_for, request, session, send_from_directory, Flask, request
from app import app
from werkzeug.utils import secure_filename
import os
from app.functions import get_images_names


ALLOWED_EXTENSIONS = set(['png', 'jpg'])


"""@app.route("/carusel")
def carusel():
    return render_template('carusel.html', img_dir='static/img/', images=[i for i in get_images_names('app/static/img')])
"""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/img", methods=['POST', 'GET'])
def img():
    if request.method == 'GET':
        return render_template('img.html', img_dir='static/img/', images=[i for i in get_images_names('app/static/img')])

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('img'))
