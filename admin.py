from cafe import Cafee

class Admin:
    
    def addProduct(self):
        name = input("Product Name : ")
        price = int(input("product price : "))
        quantity = int(input("Quantity : "))
        c = Cafee(name,price,quantity)
        fp = open("data.txt", "a")
        fp. write(str(c))
        fp.close()

        with open("data.txt", "r") as fp:
            for c in fp:
                # print(e)
                sep_text = c.split(',')
                print("name: ",sep_text[0])
                print("price: ",sep_text[1])
                print("quantity: ",sep_text[2])
                print('product added sucessfully:👍')

    
    def displayMenu(self):
        with open("data.txt", "r") as fp:
            for c in fp:
                sep_text = c.split(',')
                print("name: ", sep_text[0])
                print("price: ", sep_text[1])
                print("quantity: ", sep_text[2])
                print('----------')


    def updateProduct(self):
        name = input("Enter product name to update: ")
        with open("data.txt", "r") as fp:
            lines = fp.readlines()
        with open("data.txt", "w") as fp:
            for line in lines:
                sep_text = line.split(',')
                if sep_text[0] == name:
                    name = input("Enter new product: ")
                    price = int(input("Enter new price: "))
                    quantity = int(input("Enter new quantity: "))
                    line = f"{name},{price},{quantity}\n"
                fp.write(line)
            

    def deleteProduct(self):
        name = input("Enter product name to delete: ")
        with open("data.txt", "r") as fp:
            lines = fp.readlines()
        with open("data.txt", "w") as fp:
            for line in lines:
                if name not in line:
                    fp.write(line)
        print("Product deleted successfully.")
            
    
    def searchProduct(self):
        search_name = input("Enter product name to search: ")
        with open("data.txt", "r") as fp:
            for c in fp:
                sep_text = c.split(',')
                if sep_text[0].strip() == search_name:
                    print("name: ", sep_text[0])
                    print("price: ", sep_text[1])
                    print("quantity: ", sep_text[2])
                    print('----------')
                    break
            else:
                print("Product not found.")

                