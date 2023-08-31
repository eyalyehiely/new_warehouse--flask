from flask import Flask
from main import add_equipment
app =(__name__)

@app.route('/equipment')
def new_equipment():
    add_equipment(name,serial_num,date,quantity,add_by)

