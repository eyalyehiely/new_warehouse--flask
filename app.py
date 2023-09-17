from flask import Flask,render_template,redirect,request,session
import pickle
app = Flask(__name__)
app.secret_key = 'fghdfghdfgh'

def save_users(table:list):
    with open('users.pickle','wb') as f:
        pickle.dump(table,f)
        

def upload_users():
    with open('users.pickle','rb') as f:
        users_table = pickle.load(f)
    return users_table

users = upload_users()

@app.route('/')
def home():
    for user in users:
        if session.get('username','No such user') == user['username']:
            return render_template('home.html',username = user['username'])
        else:
            return redirect('/login')




@app.route('/login', methods = ["POST",'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    for user in users:
        if ((request.form['username'] == user['username']) and (request.form['password'] == user['password'])):
            session['username'] = request.form['username'] 
            return redirect('/')
        else:
            return redirect('/register')
        


@app.route('/register', methods = ["POST",'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    for user in users:
        if request.form['username'] != user['username']:
            users.append(request.form)
            save_users(users)
            session['username'] = request.form['username'] 
            return redirect('/')
        else:
            return ("No valid user")
    
     


print(users)