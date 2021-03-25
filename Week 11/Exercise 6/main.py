from classes import Product
def insertProduct(dict1):
    name = input("Enter the new name: ")
    while name in dict1.keys():
        print("The product is already registered")      
        name = input("Enter the new name: ")
    if len(dict1) == 10:
        print("Cannot add product, dictionary is full")
    else:
        price = float(input("Enter the new price: "))
        stock = int(input("Enter the new stock: "))     
        product = Product(name, price, stock)
        dict1[name] = [product.price, product.stock]
        

def searchProduct(dict1):
    name = input("Enter the name of the product: ")
    if name not in dict1.keys():
        print("Product not found")
    else:
        values = dict1.get(name)
        product = Product(name,values[0], values[1])
        print("The price is", product.price)
        print("The stock is", product.stock)

def modifyProduct(dict1):
    name = input("Enter the name of the product: ")
    if name not in dict1.keys():
        print("Product not found")
    else:
        price = float(input("Enter the new price: "))
        stock = int(input("Enter the new stock: "))     
        dict1[name] = [price, stock]
    


# Program init
products = dict()  
choice = None
menu = '''
          MENU:
          1. Add a new product
          2. Search for a product
          3. Modify price and stock
          4. Exit
          '''
while choice != 4:
    print(menu)
    choice = int(input("Select your option: "))
    while choice not in range(1,5):
        print("INVALID CHOICE")
        choice = int(input("Select your option: "))
    if choice == 1: 
        insertProduct(products)
    elif choice == 2:
        searchProduct(products)
    elif choice == 3:
        modifyProduct(products)
print("See you soon!")
        


