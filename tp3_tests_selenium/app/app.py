from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
USERS = {'admin': 'password123'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            error = "Tous les champs sont requis."
        elif USERS.get(username) == password:
            return redirect(url_for('dashboard'))
        else:
            error = "Identifiants incorrects."

    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
