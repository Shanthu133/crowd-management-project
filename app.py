from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

count = 0

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # simple login check
        if username == 'admin' and password == '1234':
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


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


if __name__ == '__main__':
    app.run(debug=True)