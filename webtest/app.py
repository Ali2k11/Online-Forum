from flask import Flask
from flask import Flask, redirect, render_template, request, session, url_for, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ienagineag i;eagne;aigneai;n'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Khankhan11!!",
    database="example1"
)
mycursor = mydb.cursor(buffered=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return (url_for('index.html'))
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        check = 'SELECT * FROM users WHERE user_name = %s AND user_password = %s'
        value = (username, password)
        mycursor.execute(check, value)
        check1 = mycursor.fetchone()
        mydb.commit()

    if check1:

        session['user_id'] = check1[0]

        return redirect(url_for('homepage'))

    else:
        
        return redirect(url_for('/', msg="incorrect Credientials"))

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect(url_for('home'))

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
    

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    sqlinsert = "insert into users (user_name, user_password, is_admin) values ( %s, %s,0)"
    valueinsert =(username, password)
    mycursor.execute(sqlinsert, valueinsert)
    mydb.commit()
    return render_template ('index.html')

@app.route('/topicpost', methods=['POST','GET'])
def topicpost():
    user_id = session['user_id']
    topictitle = request.form['topic_name']
    topicdescription = request.form['topic_description']
    insertdata = "insert into topic (topic_id, topic_name, topic_description, user_id ) values (0, %s, %s, %s)"
    valuei =(topictitle, topicdescription, user_id)
    mycursor.execute(insertdata, valuei)
    mydb.commit()
    return redirect(url_for('homepage'))

@app.route('/topics', methods=['GET'])
def topics():
    mycursor.execute=("select * from topic;")
    results = mycursor.fetchall()
    mydb.commit()
    return render_template(('homepage'), results = results)
