from main import (
    delete_product,
    get_all_products,
    create_product,
    get_product_by_id,
    update_product,
    delete_product
)

if __name__ == '__main__':
    print("""
                                Добро пожаловать на авторынок Carbazar,

                                введите команду которую хотите совершить: """)
    while True:
        command = input("""                            

                                1 - Создать объявление
                                2 - Удалить объявление по ID
                                3 - Найти объявление по ID
                                4 - Изменить объявление по ID
                                5 - Список всех объявлений
                                6 - Выход из программы
                                """)
        if command == '6':
            print('До свидания! С уважением Carbazar.')   
            break    
        if command == '1':
            create_product()
        if command == '2':
            delete_product()
        if command == '3':
            get_product_by_id()
        if command == '4':
            update_product()
        if command == '5':
            answer = get_all_products()
            print(answer)
            
                
        else:
            print('Вы ввели неверную команду ')                    
                             




    
    
    
    
    
    
    
    
    
    
    
    
    
    
   


