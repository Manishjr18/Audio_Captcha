# # # # # from captcha.image import ImageCaptcha
# # # # # import random
# # # # # from flask import Flask, request, redirect, url_for, render_template
# # # # # import time

# # # # # app = Flask(__name__)
# # # # # app.secret_key = 'your_secret_key'

# # # # # def captcha():
# # # # #     num = random.randint(100000, 999999)
# # # # #     image = ImageCaptcha()
# # # # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # # # #     image_path = f'./static/images/{tstr}.png'
# # # # #     image.write(str(num), image_path)
# # # # #     return num, tstr

# # # # # @app.route("/", methods=["GET", "POST"])
# # # # # def index():
# # # # #     global num1
# # # # #     error = None
# # # # #     success = None
# # # # #     if request.method == "GET":
# # # # #         num1, tstr = captcha()
# # # # #         return render_template('index.html', tstr=tstr, error=error, success=success)
# # # # #     elif request.method == "POST":
# # # # #         ip = request.form["ip"]
# # # # #         try:
# # # # #             if int(ip) == int(num1):
# # # # #                 success = "CAPTCHA passed successfully!"
# # # # #                 num1, tstr = captcha() 
# # # # #                 return render_template('index.html', tstr=tstr, error=error, success=success)
# # # # #             else:
# # # # #                 error = "Invalid CAPTCHA. Please try again."
# # # # #                 num1, tstr = captcha()
# # # # #                 return render_template('index.html', tstr=tstr, error=error, success=success)
# # # # #         except:
# # # # #             error = "Invalid CAPTCHA. Please try again."
# # # # #             num1, tstr = captcha()
# # # # #             return render_template('index.html', tstr=tstr, error=error, success=success)

# # # # # if __name__ == "__main__":
# # # # #     app.debug = True
# # # # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # # # from captcha.image import ImageCaptcha
# # # # import random
# # # # from flask import Flask, request, render_template
# # # # import time

# # # # app = Flask(__name__)
# # # # app.secret_key = 'your_secret_key'

# # # # # Function to generate a CAPTCHA
# # # # def generate_captcha():
# # # #     num = random.randint(100000, 999999)
# # # #     image = ImageCaptcha()
# # # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # # #     image_path = f'./static/images/{tstr}.png'
# # # #     image.write(str(num), image_path)
# # # #     return num, tstr

# # # # @app.route("/", methods=["GET", "POST"])
# # # # def index():
# # # #     global num1, tstr
# # # #     error = None
# # # #     success = None

# # # #     # Initialize CAPTCHA on GET request or if not previously set
# # # #     if request.method == "GET" or 'num1' not in globals():
# # # #         num1, tstr = generate_captcha()
# # # #         return render_template('index.html', tstr=tstr, error=error, success=success)

# # # #     # Handle form submission
# # # #     if request.method == "POST":
# # # #         ip = request.form["ip"]
# # # #         try:
# # # #             # Validate CAPTCHA
# # # #             if int(ip) == num1:
# # # #                 success = "CAPTCHA passed successfully!"
# # # #                 # Do not generate a new CAPTCHA
# # # #             else:
# # # #                 error = "Invalid CAPTCHA. Please try again."
# # # #                 num1, tstr = generate_captcha()  # Generate a new CAPTCHA on incorrect validation
# # # #         except:
# # # #             error = "Invalid CAPTCHA. Please try again."
# # # #             num1, tstr = generate_captcha()  # Generate a new CAPTCHA on incorrect validation

# # # #         return render_template('index.html', tstr=tstr, error=error, success=success)

# # # # if __name__ == "__main__":
# # # #     app.debug = True
# # # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # # from captcha.image import ImageCaptcha
# # # import random
# # # from flask import Flask, request, render_template, jsonify, url_for
# # # import time

# # # app = Flask(__name__)
# # # app.secret_key = 'your_secret_key'

# # # def generate_captcha():
# # #     num = random.randint(100000, 999999)
# # #     image = ImageCaptcha()
# # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # #     image_path = f'./static/images/{tstr}.png'
# # #     image.write(str(num), image_path)
# # #     return num, tstr

# # # @app.route("/", methods=["GET", "POST"])
# # # def index():
# # #     global num1, tstr
# # #     error = None
# # #     success = None

# # #     if request.method == "GET" or 'num1' not in globals():
# # #         num1, tstr = generate_captcha()
# # #         return render_template('index.html', tstr=tstr, error=error, success=success)

# # #     if request.method == "POST":
# # #         ip = request.form["ip"]
# # #         try:
# # #             if int(ip) == num1:
# # #                 success = "CAPTCHA passed successfully!"
# # #             else:
# # #                 error = "Invalid CAPTCHA. Please try again."
# # #                 num1, tstr = generate_captcha()
# # #         except:
# # #             error = "Invalid CAPTCHA. Please try again."
# # #             num1, tstr = generate_captcha()

# # #         return render_template('index.html', tstr=tstr, error=error, success=success)

# # # @app.route("/refresh-captcha", methods=["GET"])
# # # def refresh_captcha():
# # #     global num1, tstr
# # #     num1, tstr = generate_captcha()
# # #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# # #     return jsonify(new_captcha_url=new_captcha_url)

# # # if __name__ == "__main__":
# # #     app.debug = True
# # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # from captcha.image import ImageCaptcha
# # import random
# # from flask import Flask, request, render_template, jsonify, url_for
# # import time

# # app = Flask(__name__)
# # app.secret_key = 'your_secret_key'

# # def generate_captcha():
# #     num = random.randint(100000, 999999)
# #     image = ImageCaptcha()
# #     tstr = time.strftime("%Y%m%d-%H%M%S")
# #     image_path = f'./static/images/{tstr}.png'
# #     image.write(str(num), image_path)
# #     return num, tstr

# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     global num1, tstr
# #     error = None
# #     success = None

# #     if request.method == "GET" or 'num1' not in globals():
# #         num1, tstr = generate_captcha()
# #         return render_template('index.html', tstr=tstr, error=error, success=success)

# #     if request.method == "POST":
# #         ip = request.form["ip"]
# #         try:
# #             if int(ip) == num1:
# #                 success = "CAPTCHA passed successfully!"
# #             else:
# #                 error = "Invalid CAPTCHA. Please try again."
# #                 num1, tstr = generate_captcha()
# #         except:
# #             error = "Invalid CAPTCHA. Please try again."
# #             num1, tstr = generate_captcha()

# #         return render_template('index.html', tstr=tstr, error=error, success=success)

# # @app.route("/refresh-captcha", methods=["GET"])
# # def refresh_captcha():
# #     global num1, tstr
# #     num1, tstr = generate_captcha()
# #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# #     return jsonify(new_captcha_url=new_captcha_url)

# # if __name__ == "__main__":
# #     app.debug = True
# #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# from captcha.image import ImageCaptcha
# import random
# from flask import Flask, request, render_template, jsonify, url_for
# import time

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# def generate_captcha():
#     num = random.randint(100000, 999999)
#     image = ImageCaptcha()
#     tstr = time.strftime("%Y%m%d-%H%M%S")
#     image_path = f'./static/images/{tstr}.png'
#     image.write(str(num), image_path)
#     return num, tstr

# @app.route("/", methods=["GET", "POST"])
# def index():
#     global num1, tstr
#     error = None
#     success = None

#     if request.method == "GET" or 'num1' not in globals():
#         num1, tstr = generate_captcha()
#         return render_template('index.html', tstr=tstr, error=error, success=success)

#     if request.method == "POST":
#         ip = request.form["ip"]
#         try:
#             if int(ip) == num1:
#                 success = "CAPTCHA passed successfully!"
#                 error = None
#             else:
#                 error = "Invalid CAPTCHA. Please try again."
#                 success = None
#                 num1, tstr = generate_captcha()
#         except:
#             error = "Invalid CAPTCHA. Please try again."
#             success = None
#             num1, tstr = generate_captcha()

#         return render_template('index.html', tstr=tstr, error=error, success=success)

# @app.route("/refresh-captcha", methods=["GET"])
# def refresh_captcha():
#     global num1, tstr
#     num1, tstr = generate_captcha()
#     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
#     return jsonify(new_captcha_url=new_captcha_url)

# if __name__ == "__main__":
#     app.debug = True
#     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

from captcha.image import ImageCaptcha
from gtts import gTTS
import random
from flask import Flask, request, render_template, jsonify, url_for
import time
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_captcha():
    num = random.randint(100000, 999999)
    image = ImageCaptcha()
    tstr = time.strftime("%Y%m%d-%H%M%S")
    image_path = f'./static/images/{tstr}.png'
    image.write(str(num), image_path)
    return num, tstr

def generate_audio(num):
    tts = gTTS(text=" ".join(str(num)), lang='en')
    audio_path = f'./static/audio/{num}.mp3'
    tts.save(audio_path)
    return audio_path

@app.route("/", methods=["GET", "POST"])
def index():
    global num1, tstr
    error = None
    success = None

    if request.method == "GET" or 'num1' not in globals():
        num1, tstr = generate_captcha()
        audio_path = generate_audio(num1)
        return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

    if request.method == "POST":
        ip = request.form["ip"]
        try:
            if int(ip) == num1:
                success = "CAPTCHA passed successfully!"
                error = None
                num1, tstr = generate_captcha()
                audio_path = generate_audio(num1)
            else:
                error = "Invalid CAPTCHA. Please try again."
                success = None
                num1, tstr = generate_captcha()
                audio_path = generate_audio(num1)
        except:
            error = "Invalid CAPTCHA. Please try again."
            success = None
            num1, tstr = generate_captcha()
            audio_path = generate_audio(num1)

        return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

@app.route("/refresh-captcha", methods=["GET"])
def refresh_captcha():
    global num1, tstr
    num1, tstr = generate_captcha()
    audio_path = generate_audio(num1)
    new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
    new_audio_url = url_for('static', filename='audio/' + str(num1) + '.mp3')
    return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

if __name__ == "__main__":
    if not os.path.exists('./static/images'):
        os.makedirs('./static/images')
    if not os.path.exists('./static/audio'):
        os.makedirs('./static/audio')
    app.debug = True
    app.run(host="0.0.0.0", threaded=True, use_reloader=True)
