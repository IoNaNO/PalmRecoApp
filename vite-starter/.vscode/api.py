from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    left_images = data.get('left_images')
    right_images = data.get('right_images')

    # 这里你可以处理这些数据，例如保存到数据库或者进行其他处理
    # ...

    # 假设处理成功，返回一个成功的响应
    return jsonify({'code': 0, 'message': 'Register Success'})

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('/path/to/save', filename))
        # 这里你可以处理这个文件，例如进行图像识别
        # ...

        # 假设处理成功，返回一个成功的响应
        return jsonify({'result': 'Your result'})


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import base64
from PIL import Image
import io

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    left_images = data['left_images']

    for i, img_data in enumerate(left_images):
        img_bytes = base64.b64decode(img_data)
        img = Image.open(io.BytesIO(img_bytes))
        # 这里你可以处理这个图像，例如保存到文件
        img.save(f'left_image_{i}.jpg')

    # 假设处理成功，返回一个成功的响应
    return jsonify({'code': 0})

if __name__ == '__main__':
    app.run(debug=True)