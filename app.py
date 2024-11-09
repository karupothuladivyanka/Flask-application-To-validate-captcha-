
'''
from flask import *
app=Flask(__name__)
@app.route('/admin')
def admin():
    return 'this is admin'
@app.route('/student')
def student():
    return 'this is student'
@app.route('/staff')
def staff():
    return 'this is staff'
@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return 'this is admin'
    if name=='student':
        return 'this is student'
    if name=='staff':
        return 'this is staff'
if __name__=='__main__':
    app.run()
'''



#for login and registration code
'''

from flask import Flask
app = Flask(__name__)
@app.route('/login', methods =['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.args.get('username')
        password = request.args.get('password')
        msg = 'Logged in successfully !'
        return render_template('login.html', msg = msg)
    else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
if __name__=='__main__':
     app.run(debug=True)
'''



#for captcha
'''

from flask import Flask,render_template 
  
app = Flask(__name__) 
  
@app.route('/') 
def index(): 
    return render_template('form.html') 
    
if __name__ == "__main__": 
    app.run(debug=True) 


from flask import Flask, render_template 
from pymongo import MongoClient 
  
app = Flask(__name__) 

# Database Config 
# If your mongodb runs on a different port 
# change 27017 to that port number 
mongoClient = MongoClient('localhost', 27017) 
  
@app.route('/') 
def index(): 
    return render_template('form.html') 
  
if __name__ == "__main__": 
    app.run(debug=True)   




import uuid 
from flask import Flask, render_template 
from flask_sessionstore import Session 
from flask_session_captcha import FlaskSessionCaptcha 
from pymongo import MongoClient 
  
app = Flask(__name__) 
  
# Database Config 
# If your mongodb runs on a different port 
# change 27017 to that port number 
mongoClient = MongoClient('localhost', 27017) 
  
# Captcha Configuration 
app.config["SECRET_KEY"] = uuid.uuid4() 
app.config['CAPTCHA_ENABLE'] = True
  
# Set 5 as character length in captcha 
app.config['CAPTCHA_LENGTH'] = 5
  
# Set the captcha height and width 
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient 
app.config['SESSION_TYPE'] = 'mongodb'
  
# Enables server session 
Session(app) 
  
# Initialize FlaskSessionCaptcha 
captcha = FlaskSessionCaptcha(app) 
  
@app.route('/') 
def index(): 
    return render_template('form.html') 
  
if __name__ == "__main__": 
    app.run(debug=True) 



import uuid 
import logging 
from flask import Flask, render_template 
from flask_sessionstore import Session 
from flask_session_captcha import FlaskSessionCaptcha 
from pymongo import MongoClient 
  
app = Flask(__name__) 
  
# Database Config 
# If your mongodb runs on a different port 
# change 27017 to that port number 
mongoClient = MongoClient('localhost', 27017) 
  
# Captcha Configuration 
app.config["SECRET_KEY"] = uuid.uuid4() 
app.config['CAPTCHA_ENABLE'] = True
  
# Set 5 as character length in captcha 
app.config['CAPTCHA_LENGTH'] = 5
  
# Set the captcha height and width 
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient 
app.config['SESSION_TYPE'] = 'mongodb'
  
# Enables server session 
Session(app) 
  
# Initialize FlaskSessionCaptcha 
captcha = FlaskSessionCaptcha(app) 
  
@app.route('/') 
def index(): 
    return render_template('form.html') 
  
  
if __name__ == "__main__": 
    app.debug = True
    logging.getLogger().setLevel("DEBUG") 
    app.run()     




import uuid 
import logging 
from flask import Flask, request, render_template 
from flask_sessionstore import Session 
from flask_session_captcha import FlaskSessionCaptcha 
from pymongo import MongoClient 

app = Flask(__name__) 

# Database Config 
# If your mongodb runs on a different port 
# change 27017 to that port number 
mongoClient = MongoClient('localhost', 27017) 

# Captcha Configuration 
app.config["SECRET_KEY"] = uuid.uuid4() 
app.config['CAPTCHA_ENABLE'] = True

# Set 5 as character length in captcha 
app.config['CAPTCHA_LENGTH'] = 5

# Set the captcha height and width 
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
app.config['SESSION_MONGODB'] = mongoClient 
app.config['SESSION_TYPE'] = 'mongodb'

# Enables server session 
Session(app) 

# Initialize FlaskSessionCaptcha 
captcha = FlaskSessionCaptcha(app) 

@app.route('/', methods=['POST', 'GET']) 
def index(): 
	if request.method == "POST": 
		if captcha.validate(): 
			return "success"
		else: 
			return "fail"

	return render_template("form.html") 


if __name__ == "__main__": 
	app.debug = True
	logging.getLogger().setLevel("DEBUG") 
	app.run() 
'''





#captcha code


'''

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
'''






#live search using flask and jquery
from flask import Flask,render_template 
  
  
app = Flask(__name__) 
  
@app.route("/") 
def home(): 
    return render_template("index.html") 
  
  
if __name__ == "__main__": 
    app.run(debug=True)