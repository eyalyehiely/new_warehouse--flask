class Equipment:
    def __init__(self,name = 'def',serial_num = 'def',date='def',quantity='def',add_by = 'def'):
        self.name = name
        self.serial_num = serial_num
        self.date = date
        self.quantity = quantity
        self.add_by = add_by

    def __repr__(self,name,serial_num,date,quantity,add_by):
        return f"/nName:\t{name}\nSerial Number:\t{serial_num}\nDate:\t{date}\nQuantity:\t{quantity}\nAdded By:\t{add_by}\n"