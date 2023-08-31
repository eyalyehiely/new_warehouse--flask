import pickle
from classes import Equipment
import datetime
#equipment
#saving equipment data
def save_equipment_data(list_to_save):
    with ("equipment.pickle",'wb')as f:
        f = pickle.dump(list_to_save,f)
    

#loading equipment data
def load_equipment_data():
    with ("equipment.pickle",'rb')as f:
        equipment_list = pickle.load()
        return equipment_list
    

#create

def add_equipment(name,serial_num,date,quantity,add_by):
    equipment1 = Equipment(name = name, serial_num = serial_num, date = date,quantity = quantity,add_by = add_by)
    return equipment1
    