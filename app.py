from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pickle
app = Flask(__name__)
model = pickle.load(open(r"D:\College Files\Flask Codes\IRIS\SVM.pickle",'rb'))
app.secret_key = '123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Malathi5*'
app.config['MYSQL_DB'] = 'iris'

mysql = MySQL(app)

#@app.route("/")
@app.route('/', methods=['Get','Post'])
def main():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        print("hello")
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            if account['password'] == password and account['username'] == username:
            # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                # Redirect to home page
                print("hello")
                return render_template('input.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

@app.route("/first", methods = ['post'])
def index():
    return render_template("input.html")

@app.route("/predict", methods=['post'])
def pred():
    features = [float(i) 
                for i in 
                (request.form.values())]
    pred = model.predict([features])
    if pred == ['Iris-setosa']:
        return render_template("iris_setosa.html",data=pred)
    elif pred == ['Iris-versicolor']:
        return render_template("iris_versicolor.html", data=pred)
    else:
        return render_template("iris_virginica.html", data=pred)


if __name__=='__main__':
    app.run(host='localhost',port=5000)



