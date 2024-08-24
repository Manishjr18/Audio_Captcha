# # # from captcha.image import ImageCaptcha
# # # from gtts import gTTS
# # # import random
# # # from flask import Flask, request, render_template, jsonify, url_for
# # # import time
# # # import os
# # # import string 

# # # app = Flask(__name__)
# # # app.secret_key = 'your_secret_key'

# # # def generate_captcha():
# # #     captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
# # #     image = ImageCaptcha()
# # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # #     image_path = f'./static/images/{tstr}.png'
# # #     image.write(captcha_str, image_path)
# # #     return captcha_str, tstr

# # # def generate_audio(num):
# # #     tts = gTTS(text=" ".join(str(num)), lang='en')
# # #     audio_path = f'./static/audio/{num}.mp3'
# # #     tts.save(audio_path)
# # #     return audio_path

# # # @app.route("/", methods=["GET", "POST"])
# # # def index():
# # #     global num1, tstr
# # #     error = None
# # #     success = None

# # #     if request.method == "GET" or 'num1' not in globals():
# # #         num1, tstr = generate_captcha()
# # #         audio_path = generate_audio(num1)
# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # #     if request.method == "POST":
# # #         ip = request.form["ip"]
# # #         try:
# # #             if int(ip) == num1:
# # #                 success = "CAPTCHA passed successfully!"
# # #                 error = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #             else:
# # #                 error = "Invalid CAPTCHA. Please try again."
# # #                 success = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #         except:
# # #             error = "Invalid CAPTCHA. Please try again."
# # #             success = None
# # #             num1, tstr = generate_captcha()
# # #             audio_path = generate_audio(num1)

# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # # @app.route("/refresh-captcha", methods=["GET"])
# # # def refresh_captcha():
# # #     global num1, tstr
# # #     num1, tstr = generate_captcha()
# # #     audio_path = generate_audio(num1)
# # #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# # #     new_audio_url = url_for('static', filename='audio/' + str(num1) + '.mp3')
# # #     return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

# # # if __name__ == "__main__":
# # #     if not os.path.exists('./static/images'):
# # #         os.makedirs('./static/images')
# # #     if not os.path.exists('./static/audio'):
# # #         os.makedirs('./static/audio')
# # #     app.debug = True
# # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # # from captcha.image import ImageCaptcha
# # # from gtts import gTTS
# # # import random
# # # from flask import Flask, request, render_template, jsonify, url_for
# # # import time
# # # import os
# # # import string 

# # # app = Flask(__name__)
# # # app.secret_key = 'your_secret_key'

# # # def generate_captcha():
# # #     captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
# # #     image = ImageCaptcha()
# # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # #     image_path = f'./static/images/{tstr}.png'
# # #     image.write(captcha_str, image_path)
# # #     return captcha_str, tstr

# # # def generate_audio(captcha_str):
# # #     message = f"All alphabets are in small case. The captcha is: {' '.join(captcha_str)}"
# # #     tts = gTTS(text=message, lang='en')
# # #     audio_path = f'./static/audio/{captcha_str}.mp3'
# # #     tts.save(audio_path)
# # #     return audio_path

# # # @app.route("/", methods=["GET", "POST"])
# # # def index():
# # #     global num1, tstr
# # #     error = None
# # #     success = None

# # #     if request.method == "GET" or 'num1' not in globals():
# # #         num1, tstr = generate_captcha()
# # #         audio_path = generate_audio(num1)
# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # #     if request.method == "POST":
# # #         ip = request.form["ip"]
# # #         try:
# # #             if ip == num1:
# # #                 success = "CAPTCHA passed successfully!"
# # #                 error = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #             else:
# # #                 error = "Invalid CAPTCHA. Please try again."
# # #                 success = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #         except:
# # #             error = "Invalid CAPTCHA. Please try again."
# # #             success = None
# # #             num1, tstr = generate_captcha()
# # #             audio_path = generate_audio(num1)

# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # # @app.route("/refresh-captcha", methods=["GET"])
# # # def refresh_captcha():
# # #     global num1, tstr
# # #     num1, tstr = generate_captcha()
# # #     audio_path = generate_audio(num1)
# # #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# # #     new_audio_url = url_for('static', filename='audio/' + num1 + '.mp3')
# # #     return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

# # # if __name__ == "__main__":
# # #     if not os.path.exists('./static/images'):
# # #         os.makedirs('./static/images')
# # #     if not os.path.exists('./static/audio'):
# # #         os.makedirs('./static/audio')
# # #     app.debug = True
# # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # # from captcha.image import ImageCaptcha
# # # from gtts import gTTS
# # # import random
# # # from flask import Flask, request, render_template, jsonify, url_for
# # # import time
# # # import os
# # # import string
# # # from pydub import AudioSegment
# # # from pydub.generators import WhiteNoise

# # # app = Flask(__name__)
# # # app.secret_key = 'your_secret_key'

# # # def generate_captcha():
# # #     captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
# # #     image = ImageCaptcha()
# # #     tstr = time.strftime("%Y%m%d-%H%M%S")
# # #     image_path = f'./static/images/{tstr}.png'
# # #     image.write(captcha_str, image_path)
# # #     return captcha_str, tstr

# # # def generate_audio(captcha_str):
# # #     message = f"All alphabets are in small case. The captcha is: {' '.join(captcha_str)}"
# # #     tts = gTTS(text=message, lang='en')
# # #     tts.save("temp.mp3")

# # #     # Load the TTS audio
# # #     tts_audio = AudioSegment.from_mp3("temp.mp3")

# # #     # Create white noise
# # #     noise = WhiteNoise().to_audio_segment(duration=tts_audio.duration_seconds * 1000)

# # #     # Mix the noise with TTS audio
# # #     mixed = tts_audio.overlay(noise - 30)  # Adjust noise level as needed (-30 dB here)

# # #     # Add delay at the beginning of the audio
# # #     delay = AudioSegment.silent(duration=3000)  # 3 seconds delay
# # #     final_audio = delay + mixed

# # #     # Save the final audio
# # #     audio_path = f'./static/audio/{captcha_str}.mp3'
# # #     final_audio.export(audio_path, format="mp3")

# # #     # Clean up temporary file
# # #     os.remove("temp.mp3")

# # #     return audio_path

# # # @app.route("/", methods=["GET", "POST"])
# # # def index():
# # #     global num1, tstr
# # #     error = None
# # #     success = None

# # #     if request.method == "GET" or 'num1' not in globals():
# # #         num1, tstr = generate_captcha()
# # #         audio_path = generate_audio(num1)
# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # #     if request.method == "POST":
# # #         ip = request.form["ip"]
# # #         try:
# # #             if ip == num1:
# # #                 success = "CAPTCHA passed successfully!"
# # #                 error = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #             else:
# # #                 error = "Invalid CAPTCHA. Please try again."
# # #                 success = None
# # #                 num1, tstr = generate_captcha()
# # #                 audio_path = generate_audio(num1)
# # #         except:
# # #             error = "Invalid CAPTCHA. Please try again."
# # #             success = None
# # #             num1, tstr = generate_captcha()
# # #             audio_path = generate_audio(num1)

# # #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # # @app.route("/refresh-captcha", methods=["GET"])
# # # def refresh_captcha():
# # #     global num1, tstr
# # #     num1, tstr = generate_captcha()
# # #     audio_path = generate_audio(num1)
# # #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# # #     new_audio_url = url_for('static', filename='audio/' + num1 + '.mp3')
# # #     return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

# # # if __name__ == "__main__":
# # #     if not os.path.exists('./static/images'):
# # #         os.makedirs('./static/images')
# # #     if not os.path.exists('./static/audio'):
# # #         os.makedirs('./static/audio')
# # #     app.debug = True
# # #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# # import os
# # from captcha.image import ImageCaptcha
# # from gtts import gTTS
# # import random
# # from flask import Flask, request, render_template, jsonify, url_for
# # import time
# # import string
# # from pydub import AudioSegment
# # from pydub.generators import WhiteNoise

# # app = Flask(__name__)
# # app.secret_key = 'your_secret_key'

# # # Explicitly set the path to FFmpeg
# # os.environ["FFMPEG_BINARY"] = "ffmpeg"
# # os.environ["FFPROBE_BINARY"] = "ffprobe"

# # def generate_captcha():
# #     captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
# #     image = ImageCaptcha()
# #     tstr = time.strftime("%Y%m%d-%H%M%S")
# #     image_path = f'./static/images/{tstr}.png'
# #     image.write(captcha_str, image_path)
# #     return captcha_str, tstr

# # def generate_audio(captcha_str):
# #     message = f"All alphabets are in small case. The captcha is: {' '.join(captcha_str)}"
# #     tts = gTTS(text=message, lang='en')
# #     tts.save("temp.mp3")

# #     tts_audio = AudioSegment.from_mp3("temp.mp3")
# #     noise = WhiteNoise().to_audio_segment(duration=len(tts_audio))
# #     combined = tts_audio.overlay(noise - 20)
# #     audio_path = f'./static/audio/{captcha_str}.mp3'
# #     combined.export(audio_path, format="mp3")

# #     os.remove("temp.mp3")
# #     return audio_path

# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     global num1, tstr
# #     error = None
# #     success = None

# #     if request.method == "GET" or 'num1' not in globals():
# #         num1, tstr = generate_captcha()
# #         audio_path = generate_audio(num1)
# #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# #     if request.method == "POST":
# #         ip = request.form["ip"]
# #         try:
# #             if ip == num1:
# #                 success = "CAPTCHA passed successfully!"
# #                 error = None
# #                 num1, tstr = generate_captcha()
# #                 audio_path = generate_audio(num1)
# #             else:
# #                 error = "Invalid CAPTCHA. Please try again."
# #                 success = None
# #                 num1, tstr = generate_captcha()
# #                 audio_path = generate_audio(num1)
# #         except:
# #             error = "Invalid CAPTCHA. Please try again."
# #             success = None
# #             num1, tstr = generate_captcha()
# #             audio_path = generate_audio(num1)

# #         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# # @app.route("/refresh-captcha", methods=["GET"])
# # def refresh_captcha():
# #     global num1, tstr
# #     num1, tstr = generate_captcha()
# #     audio_path = generate_audio(num1)
# #     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
# #     new_audio_url = url_for('static', filename='audio/' + num1 + '.mp3')
# #     return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

# # if __name__ == "__main__":
# #     if not os.path.exists('./static/images'):
# #         os.makedirs('./static/images')
# #     if not os.path.exists('./static/audio'):
# #         os.makedirs('./static/audio')
# #     app.debug = True
# #     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

# import os
# from captcha.image import ImageCaptcha
# from gtts import gTTS
# import random
# from flask import Flask, request, render_template, jsonify, url_for
# import time
# import string
# from pydub import AudioSegment
# from pydub.generators import WhiteNoise

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Explicitly set the path to FFmpeg
# os.environ["FFMPEG_BINARY"] = "ffmpeg"
# os.environ["FFPROBE_BINARY"] = "ffprobe"

# def generate_captcha():
#     captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
#     image = ImageCaptcha()
#     tstr = time.strftime("%Y%m%d-%H%M%S")
#     image_path = f'./static/images/{tstr}.png'
#     image.write(captcha_str, image_path)
#     return captcha_str, tstr

# def generate_audio(captcha_str):
#     # Create the initial message
#     initial_message = f"All alphabets are in small case. The captcha is: {' '.join(captcha_str)}"
#     tts = gTTS(text=initial_message, lang='en')
#     tts.save("temp.mp3")
    
#     # Load the initial audio
#     tts_audio = AudioSegment.from_mp3("temp.mp3")
    
#     # Define a minimal delay between each character
#     char_delay = 300  # milliseconds
#     character_segments = []
    
#     # Create TTS segments for each character
#     for char in captcha_str:
#         message = f"{char}"
#         tts_char = gTTS(text=message, lang='en')
#         tts_char.save(f"char_{char}.mp3")
        
#         char_audio = AudioSegment.from_mp3(f"char_{char}.mp3")
#         character_segments.append(char_audio)
#         character_segments.append(AudioSegment.silent(duration=char_delay))  # Add minimal delay

#         os.remove(f"char_{char}.mp3")

#     # Combine the initial audio with character segments
#     combined_audio = tts_audio
#     for segment in character_segments:
#         combined_audio += segment

#     # Add background noise
#     noise = WhiteNoise().to_audio_segment(duration=len(combined_audio))
#     noise = noise - 30  # Lower the volume of the noise
#     final_audio = noise.overlay(combined_audio)

#     # Export the final audio
#     audio_path = f'./static/audio/{captcha_str}.mp3'
#     final_audio.export(audio_path, format="mp3")
    
#     os.remove("temp.mp3")
#     return audio_path

# @app.route("/", methods=["GET", "POST"])
# def index():
#     global num1, tstr
#     error = None
#     success = None

#     if request.method == "GET" or 'num1' not in globals():
#         num1, tstr = generate_captcha()
#         audio_path = generate_audio(num1)
#         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

#     if request.method == "POST":
#         ip = request.form["ip"]
#         try:
#             if ip == num1:
#                 success = "CAPTCHA passed successfully!"
#                 error = None
#                 num1, tstr = generate_captcha()
#                 audio_path = generate_audio(num1)
#             else:
#                 error = "Invalid CAPTCHA. Please try again."
#                 success = None
#                 num1, tstr = generate_captcha()
#                 audio_path = generate_audio(num1)
#         except:
#             error = "Invalid CAPTCHA. Please try again."
#             success = None
#             num1, tstr = generate_captcha()
#             audio_path = generate_audio(num1)

#         return render_template('index.html', tstr=tstr, audio_path=audio_path, error=error, success=success)

# @app.route("/refresh-captcha", methods=["GET"])
# def refresh_captcha():
#     global num1, tstr
#     num1, tstr = generate_captcha()
#     audio_path = generate_audio(num1)
#     new_captcha_url = url_for('static', filename='images/' + tstr + '.png')
#     new_audio_url = url_for('static', filename='audio/' + num1 + '.mp3')
#     return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

# if __name__ == "__main__":
#     if not os.path.exists('./static/images'):
#         os.makedirs('./static/images')
#     if not os.path.exists('./static/audio'):
#         os.makedirs('./static/audio')
#     app.debug = True
#     app.run(host="0.0.0.0", threaded=True, use_reloader=True)

import os
from captcha.image import ImageCaptcha
from gtts import gTTS
import random
from flask import Flask, request, render_template, jsonify, url_for
import time
import string
from pydub import AudioSegment
from pydub.generators import WhiteNoise

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Explicitly set the path to FFmpeg
os.environ["FFMPEG_BINARY"] = "ffmpeg"
os.environ["FFPROBE_BINARY"] = "ffprobe"

def generate_captcha():
    captcha_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))  # Generates a 6-character captcha with lowercase letters and digits
    image = ImageCaptcha()
    tstr = time.strftime("%Y%m%d-%H%M%S")
    image_path = f'./static/images/{tstr}.png'
    image.write(captcha_str, image_path)
    return captcha_str, tstr

def generate_audio(captcha_str):
    # Create the initial message
    initial_message = f"All alphabets are in small case. The captcha is:"
    tts_initial = gTTS(text=initial_message, lang='en')
    tts_initial.save("temp_initial.mp3")
    
    # Load the initial audio
    initial_audio = AudioSegment.from_mp3("temp_initial.mp3")
    
    # Define a minimal delay between the initial message and CAPTCHA pronunciation
    delay_before_captcha = 1000  # milliseconds (1 second)

    # Create TTS segments for each character with a minimal delay
    char_delay = 300  # milliseconds
    character_segments = []
    
    for char in captcha_str:
        message = f"{char}"
        tts_char = gTTS(text=message, lang='en')
        tts_char.save(f"char_{char}.mp3")
        
        char_audio = AudioSegment.from_mp3(f"char_{char}.mp3")
        character_segments.append(char_audio)
        character_segments.append(AudioSegment.silent(duration=char_delay))  # Add minimal delay

        os.remove(f"char_{char}.mp3")

    # Combine the initial audio with a delay and character segments
    delay_audio = AudioSegment.silent(duration=delay_before_captcha)
    combined_audio = initial_audio + delay_audio
    for segment in character_segments:
        combined_audio += segment

    # Add background noise
    noise = WhiteNoise().to_audio_segment(duration=len(combined_audio))
    noise = noise - 30  # Lower the volume of the noise
    final_audio = noise.overlay(combined_audio)

    # Export the final audio
    audio_path = f'./static/audio/{captcha_str}.mp3'
    final_audio.export(audio_path, format="mp3")
    
    os.remove("temp_initial.mp3")
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
            if ip == num1:
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
    new_audio_url = url_for('static', filename='audio/' + num1 + '.mp3')
    return jsonify(new_captcha_url=new_captcha_url, new_audio_url=new_audio_url)

if __name__ == "__main__":
    if not os.path.exists('./static/images'):
        os.makedirs('./static/images')
    if not os.path.exists('./static/audio'):
        os.makedirs('./static/audio')
    app.debug = True
    app.run(host="0.0.0.0", threaded=True, use_reloader=True)
