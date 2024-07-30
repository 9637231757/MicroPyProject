from admin import Admin
admin = Admin()

from user import User
user = User()

while True:
    print("WELCOME TO CAFETERIA")
    print('1. Admin section')
    print('2. User section')
    print('3. Exit')
    #choice = int(input('Enter your choice: '))
    #if choice == 1:

    choice = int(input('Enter your choice: '))
    if choice == 1:
        def admin_section():
            admin_id = input('Enter admin id: ')
            admin_pass = input('Enter admin password: ')
            if admin_id == 'admin' and admin_pass == 'admin':
                return 'login sucessfully!'
            else:
             return 'Invalid admin id or password!'
        print("------------------------------------------------------")     
        print(admin_section())  
        print("------------------------------------------------------")

        while True:
            print('1. Add item')
            print('2. Display menu')
            print('3. Update item')
            print('4. Delete item')
            print('5. Search item')
            print('8. Go back')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                admin.addProduct()
            elif choice == 2:
                admin.displayMenu()
            elif choice == 3:
                admin.updateProduct()
            elif choice == 4:
                admin.deleteProduct()
            elif choice == 5:
                admin.searchProduct()
            elif choice == 8:
                break

    elif choice == 2:
        while True:
            print('1. search menu')
            print('2. Display menu')
            print('3. Place order')
            print('4. check offer')
            print('5. pay bill')
            print('6. customer rating')
            
            choice = int(input('Enter your choice: '))
            if choice == 1:
                user.SearchMenu()
            elif choice == 2:
                user.displayMenu()    
            elif choice == 3:
                user.placeOrder()
            elif choice == 4:
                user.check_offer()    
            elif choice == 5:
                user.pay_bill()
            elif choice == 6:  
                user.customer_rating()  
                                
            break
    elif choice == 3:
        break