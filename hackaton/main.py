import json
from json.decoder import JSONDecodeError
from settings import DB
from datetime import datetime


def get_all_products() -> list[dict]:
    
    with open(DB) as file:
        try:
            return json.load(file)
        except JSONDecodeError:
            return []
            



def create_product():
    id_ = datetime.now().strftime('%H%M%S')
    product = {
        'id': id_,
        'title': input('Введите название '),
        "price": int(input('Введите цену ')),
        "create_date": datetime.now().strftime('%d.%m.%Y %H:%M'),
        "change_date": datetime.now().strftime('%d.%m.%Y %H:%M'),
        "discription": input('Введите описание '),
    }
    json_product: list = get_all_products()
    json_product.append(product) 
    with open(DB, 'w') as file:
        json.dump(json_product, file, indent=4)         


def update_product():
    id_ = input('Введите id ')
    product = get_all_products()
    for obj in product:
        if obj['id'] == id_:
            obj['title'] = input('Введите название ') or obj['title']
            obj['price'] = int(input('Введите цену ')) or obj['price']
            obj['description'] = input('Введите описание ') or obj['description']
            break
    with open(DB, 'w') as file:
        json.dump(product, file, indent=4)



def delete_product():
    id_ = input('Введите id ')
    product = get_all_products()
    for obj in product:
        if obj['id'] == id_:
            product.remove(obj)
            break
    with open(DB, 'w') as file:
        json.dump(product, file, indent=4)  
             

def get_product_by_id():
    id_ = input('Введите id ')
    for obj in get_all_products():
        if obj['id'] == id_:
            return obj
    return 'Not found'




