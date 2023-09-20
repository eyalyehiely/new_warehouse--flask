items = [
    {'id': 1,'category':'textile', 'name': 'static rope', 'quantity': 10},
    {'id': 2,'category':'textile', 'name': 'dynamic rope', 'quantity': 15},
    {'id': 3,'category':'metal', 'name': 'atc', 'quantity': 20},
    {'id': 4,'category':'metal', 'name': 'omer', 'quantity': 25},
    {'id': 5,'category':'textile', 'name': 'prusik', 'quantity': 30},
]

# Example: Filter products with a price less than 20
filtered_products = list(filter(lambda product: product['category']=='textile', items))

# Display the filtered products
print(filtered_products)



class Item:
    def __init__(self,serial_num='', name='', quantity=''):
        self.serial_num = serial_num
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return self.serial_num,self.name,self.quantity