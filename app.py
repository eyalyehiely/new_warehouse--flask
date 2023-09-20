from flask import Flask,render_template,redirect,request,session,make_response,Response
import pickle
app = Flask(__name__)
app.secret_key = 'fghdfghdfgh'

#users
#-------------------------------------------------------------------------#
def save_users(table:list):
    with open('users.pickle','wb') as f:
        pickle.dump(table,f)
        

def upload_users():
    with open('users.pickle','rb') as f:
        users_table = pickle.load(f)
    return users_table

users = upload_users()
# cookies = request.cookies
# cookie_names = list(cookies.keys())

@app.route('/')
def home():
    for user in users:
        if session['username'] == user['username']:
            # cookie_names.append(session.get('username'))
            return render_template('home.html',username = user['username'])
    return redirect('/login')




@app.route('/login', methods = ["POST",'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    for user in users:
        if ((request.form['username'] == user['username']) and (request.form['password'] == user['password'])):
            session['username'] = request.form['username'] 
            return redirect('/')
    return redirect('/register')
        
        


@app.route('/register', methods = ["POST",'GET'])
def register():
    if users ==[]:
        users.append(dict(request.form))
        save_users(users)
        session['username'] = request.form['username'] 
        return redirect('/')

    if request.method == 'GET':
        return render_template('register.html')
    for user in users:
        if request.form['username'] != user['username']:
            users.append(dict(request.form))
            save_users(users)
            session['username'] = request.form['username'] 
            return redirect('/')
        else:
            return ("No valid user")
    
     

#items
#--------------------------------------------------------------------------------#
# def save_items(table:list):
#     with open('items.pickle','wb') as f:
#         pickle.dump(table,f)
        

# def upload_items():
#     with open('items.pickle','rb') as f:
#         items_table = pickle.load(f)
#     return items_table



# items= upload_items()



# @app.route('/items',methods = ['GET','POST'])
# def add_items():
#     item_name = request.form.get('item_name')
#     serial_number = request.form.get('serial_num')
#     quantity = request.form.get('quantity')
#     entrance_date = request.form.get('entrance_date')
#     added_by = request.form.get('added_by')
#     items.append(request.form)
#     save_items(items)
#     return render_template('items.html', item_name = item_name, serial_number = serial_number, quantity = quantity, entrance_date = entrance_date, added_by = added_by,items=items)

















#requests
#----------------------------------------------------------------------------------#
def save_requests(table:list):
    with open('requests.pickle','wb') as f:
        pickle.dump(table,f)
        

def upload_requests():
    with open('requests.pickle','rb') as f:
        requests_table = pickle.load(f)
    return requests_table


@app.route('/requests',methods = ['POST','GET'])
def requests():
   for user in users:
        if session.get('username') == user['username']:
            # cookie_names.append(session.get('username'))
            return render_template('requests.html',username = user['username'])
        else:
            return redirect('/login')





#Exit
#----------------------------------------------------------------------------------#
@app.route('/exit')
def exit():
    cookie = Response.delete_cookie(session['username'])
    return render_template('login.html', make_response('logging out'))

