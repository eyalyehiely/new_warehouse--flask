#general
#-------------------------------------------------------------------------#  
from flask import Flask,render_template,redirect,request,session,make_response,Response
import pickle,sqlite3,datetime
app = Flask(__name__)
app.secret_key = 'fghdfghdfgh'
  
def query (sql):
    with sqlite3.connect('users.db') as conn:
        cur=conn.cursor()
        rows = cur.execute(sql)
        return list(rows)


def users_data():
    rows = (query(f"SELECT * FROM users "))
    table =[]
    for row in rows:
        table.append({'name':row[0],'username':row[1],'password':row[2],'email':row[3],'team':row[4]})
    return table
users_table = users_data()




def items_data():
    rows = (query(f"SELECT * FROM items "))
    table =[]
    for row in rows:
        table.append({'serial numner':row[0],'category':row[1],'item_name':row[2],'quantity':row[3],'added by':row[4],'entrance date':row[5],'updaating date':row[6]})
    return table
items_table = items_data()

#Users - login-register-homepage
#-------------------------------------------------------------------------#  
#homepage
@app.route('/')
def home():
    if session['username'] == None:
        return redirect('/login')
    
    for user in users_table:
        if session['username'] == user['username']:
            return render_template('home.html',username = session['username'])
    return redirect('/login')

#login
@app.route('/login', methods = ["POST",'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    for user in users_table:
        if ((request.form['username'] == user['username']) and (request.form['password'] == user['password'])):
            session['username'] = request.form['username'] 
            return redirect('/')
    return redirect('/register')
        
        

#register
@app.route('/register', methods = ["POST",'GET'])
def register():
    if users_table ==[]:
        query(f"INSERT INTO users VALUES('{request.form['name']}' ,'{request.form['username']}' , '{request.form['password']}' , '{request.form['phone']}' , '{request.form['email']}', '{request.form['team']}' )")
        session['username'] = request.form['username'] 
        return redirect('/')

    if request.method == 'GET':
        return render_template('register.html')
    
    for user in users_table:
        if request.form['username'] == user['username']:
            return ("No valid user")
    query(f"INSERT INTO users VALUES('{request.form['name']}' ,'{request.form['username']}' , '{request.form['password']}' , '{request.form['phone']}' , '{request.form['email']}', '{request.form['team']}' )")
    session['username'] = request.form['username'] 
    return redirect('/')
    
    
     

#items
#--------------------------------------------------------------------------------#
@app.route('/items',methods = ['GET','POST'])
def get_items():
    for item in items_table:
        if request.form['item_name'] == item['item_name']:
            query(f"UPDATE items SET quantity='{str(request.form['quantity'])+str(item['quantity'])}'")
            # updating date='{datetime.date.today()}

    query(f"INSERT INTO items VALUES('{request.form.get('serial_num')}', '{request.form.get('category')}', '{request.form.get('item_name')}', '{request.form.get('quantity')}', '{request.form.get('added_by')}','{request.form.get('entrance_date')}','{request.form.get('updating_date')}')")
    return render_template('items.html')







# def items_selsection():
#     for item in items:
#         if filter((lambda product: product['name']==request.form['name'], items)):
#             quantity = int(input('how many items?'))
#             item['quantity'] = item['quantity'] - quantity
#             save_items(items)






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
            return render_template('requests.html',items_selsection(),username = user['username'])
        else:
            return redirect('/login')





#Exit
#----------------------------------------------------------------------------------#
@app.route('/exit')
def exit():
    session['username']= None
    return redirect('/login')


