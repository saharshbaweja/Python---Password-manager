from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
import os
import secrets
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'
db = SQLAlchemy(app)

# Key management
def load_key():
    return open("key.keyas", "rb").read()

def write_key():
    key = Fernet.generate_key()
    with open("key.keyas", "wb") as key_file:
        key_file.write(key)

# Generate and write a new key if it does not exist
if not os.path.exists("key.keyas"):
    write_key()
key = load_key()
fernet = Fernet(key)

# Database model
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

@app.route('/generate_password')
def generate_password_route():
    password = generate_password()
    return jsonify({'password': password})

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        pwd = request.form['password']
        encrypted_pwd = fernet.encrypt(pwd.encode()).decode()
        new_password = Password(name=name, password=encrypted_pwd)
        db.session.add(new_password)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/view')
def view():
    passwords = Password.query.all()
    decrypted_passwords = [(p.name, fernet.decrypt(p.password.encode()).decode()) for p in passwords]
    return render_template('view.html', passwords=decrypted_passwords)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)