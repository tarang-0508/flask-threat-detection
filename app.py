from flask import Flask, request
import logging
import sys

app = Flask(__name__)

# ✅ Log to stdout so Azure can capture it via AppServiceAppLogs
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/')
def home():
    logging.info("Homepage accessed")
    return "App is running!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    ip = request.remote_addr or "Unknown"

    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # ✅ Log login attempts — this is the message KQL will look for
        logging.info(f"Login attempt from IP: {ip}, Username: {username}")

        if username == 'student' and password == 'CollegePassword#2345':
            return "Login successful"
        else:
            return "Login failed", 401

    return """
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
