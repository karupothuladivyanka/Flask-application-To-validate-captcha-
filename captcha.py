from flask import Flask, render_template, request, session, redirect, url_for
from captcha.image import ImageCaptcha
import random
import string
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure secret key in production

#Get the absolute path to the static folder
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Generate a CAPTCHA image and store the answer in the session
#necessary code upto 259
def generate_captcha():
    # Generate a random string for the CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    session['captcha_text'] = captcha_text

    # Generate the CAPTCHA image
    image_captcha = ImageCaptcha()
    image_file_path = f"static/{captcha_text}.png"
    image_captcha.write(captcha_text, image_file_path)

    return image_file_path

def generate_captcha():
    # Generate random CAPTCHA text
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    session['captcha_text'] = captcha_text

    # Generate CAPTCHA image and attempt to save it
    image_captcha = ImageCaptcha()
    image_file_path = os.path.join(STATIC_FOLDER, f"{captcha_text}.png")

    print(f"Attempting to save CAPTCHA image at: {image_file_path}")
    try:
        image_captcha.write(captcha_text, image_file_path)
        print(f"CAPTCHA image saved successfully at: {image_file_path}")
    except Exception as e:
        print(f"Error saving CAPTCHA image: {e}")
    
    # Return the relative path for use in the HTML template
    return f"static/{captcha_text}.png"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('captcha')
        if user_input == session.get('captcha_text'):
            # CAPTCHA is correct
            session.pop('captcha_text',None)  # Clear session after validation
            return "CAPTCHA validated successfully!"
        else:
            # CAPTCHA is incorrect
            return "Incorrect CAPTCHA. Please try again."

    # Generate a new CAPTCHA image
    captcha_image_path = generate_captcha()
    return render_template('index.html', captcha_image=captcha_image_path)

# Clean up CAPTCHA images after the response is sent
@app.after_request
def cleanup(response):
    captcha_text = session.get('captcha_text')
    if captcha_text:
        image_file_path = f"static/{captcha_text}.png"
        if os.path.exists(image_file_path):
            os.remove(image_file_path)
    return response

if __name__ == '__main__':
    app.run(debug=True)