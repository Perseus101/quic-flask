import os
import json

import ARC

from flask import Flask, request
from werkzeug import secure_filename

app = Flask(__name__)
db = ARC.db.Database(host=os.environ["ARC_DB_HOST"])
flight = ARC.Flight(int(os.environ["ARC_FLIGHT"]), database=db)


@app.route("/health", methods=['GET'])
def health():
    return 'Ok'


@app.route("/debug", methods=['GET'])
def debug():
    return repr(flight)


@app.route("/image", methods=['POST'])
def image():
    meta = json.loads(request.form['meta'])
    file = request.files['file']
    file.save(secure_filename(file.filename))

    if meta['remote_id'] == None:
        image = ARC.Image(file.filename, database=db)
        image_type = meta['image_type']
        if image_type == "orig":
            flight.insert_image(image)
        elif image_type == "high":
            flight.insert_image(image, is_high_quality_jpg=True)
        elif image_type == "low":
            flight.insert_image(image, is_low_quality_jpg=True)
        flight.insert_image(image)
    return str(image.image_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
