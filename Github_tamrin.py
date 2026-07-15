#tamrin_1
def products():
    product_name=input("Enter product name: ")
    product_price=input("Enter product price: ")

    with open("products.txt","a") as file:
        file.write(f"{product_name},{product_price}\n")
        print("products saved")
products()

#tamrin_2
product_price=int(input("Enter your money: "))
product_list=[]
count=0
with open("products.txt","r") as file:
    my_list=file.readlines()
    print(my_list)
    for line in my_list:
        product_info=line.strip().split(",")
        product_list.append(product_info)
        if int(product_info[1])>product_price:
            print(product_info[0],product_info[1])
            count+=1
    print("number of products:",count)

#tamrin_3
count = 0
total = 0
with open("products.txt", "r") as file:
    my_list = file.readlines()
    max_price = 0
    min_price = 0
    max_product = ""
    min_product = ""
    for line in my_list:
        product_info = line.strip().split(",")

        product_name = product_info[0]
        price = int(product_info[1])
        count += 1
        total += price

        if count == 1:
            max_price = price
            min_price = price
            max_product = product_name
            min_product = product_name
        if price > max_price:
            max_price = price
            max_product = product_name
        if price < min_price:
            min_price = price
            min_product = product_name
average = total / count
print("Number of products:", count)
print("Total price:", total)
print("Average price:", average)
print("Most expensive product:", max_product, max_price)
print("Cheapest product:", min_product, min_price)

#tamrin_4
def sales():
    customer = input("Enter customer name: ")
    count = int(input("Enter number of products: "))
    total = 0

    with open("sales.txt", "a") as file:
        file.write(f"Customer : {customer}\n\n")

        for i in range(count):
            product_name = input("Enter product name: ")
            product_price = int(input("Enter product price: "))
            total += product_price

            file.write(f"{product_name} : {product_price}\n")

        file.write(f"\nTotal : {total}\n")
    print("Sale saved successfully")
sales()

