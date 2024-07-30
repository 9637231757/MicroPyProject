from cafe import Cafee

class User:

     def searchProduct(self):
        search_name = input("Enter product name to search: ")
        with open("data.txt", "r") as fp:
            for c in fp:
                sep_text = c.split(',')
                if sep_text[0] == search_name:
                    print("name: ", sep_text[0])
                    print("price: ", sep_text[1])
                    print("quantity: ", sep_text[2])
                    print('----------')
                    break
            else:
                print("Product not found.")
    
    
     def displayMenu(self):
        with open("data.txt", "r") as fp:
            for c in fp:
                sep_text = c.split(',')
                print("name: ", sep_text[0])
                print("price: ", sep_text[1])
                print("quantity: ", sep_text[2])
                print('----------')
    
      
     def placeOrder(self):
        order_name = input("Enter product name to order: ")
        order_quantity = int(input("Enter quantity to order: "))
        with open("data.txt", "r") as fp:
            for c in fp:
                sep_text = c.split(',')
                if sep_text[0] == order_name:
                    if int(sep_text[2]) >= order_quantity:
                        print("Order placed successfully.")
                        print("Total cost: ", int(sep_text[1]) * order_quantity)
                    else:
                  
                     print("we are out of stock🥲")  
       


     def check_offer(self):
       order_name = input("Enter product name to check offers: ")
       with open("data.txt", "r") as fp:
        for c in fp:
            sep_text = c.split(',')
            if sep_text[0] == order_name:
                if int(sep_text[2]) >= 2:
                    print("Buy 2 get 1 free offer available 😄")
                else:
                    print("No offers available for this product 😢")  


            
     def pay_bill(self):
            with open("data.txt", "r") as fp:
                product_name = input("Enter the product name: ")
                quantity = int(input("Enter the quantity: "))
                for line in fp:
                    sep_text = line.split(',')
                
                    if sep_text[0] == product_name:
                        # calculate total price
                        total_price = float(sep_text[1]) * quantity
                        print("Price: ", sep_text[1])
                        print("Total Price: ", total_price)
                        break
                            
                        
     def customer_rating(self):
            rating = input("Please rate our service out of 5: ")
            rating = int(rating)
            if rating >= 1 and rating <= 5:
                print("Thank you for your rating 😄")
            else:
                print("Invalid rating. Please rate between 1 and 5.")               
                            











         
              

     


        



   

     

