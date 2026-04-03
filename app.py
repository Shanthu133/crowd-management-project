from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

count = 0

# 🔐 Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '1234':
            return redirect(url_for('home'))

    return render_template('login.html')


# 🏠 Home Page
@app.route('/home')
def home():
    return render_template('index.html')


# ℹ️ About Page
@app.route('/about')
def about():
    return render_template('about.html')


# 📊 Passenger Count + Ticket System
@app.route('/count', methods=['GET', 'POST'])
def counter():
    global count
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            count += 1
        elif action == 'ticket' and count > 0:
            count -= 1

    return render_template('count.html', count=count)


# ▶️ Run locally (NOT used by Render, but needed for your PC)
if __name__ == '__main__':
    app.run()