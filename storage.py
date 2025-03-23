products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Cena produktu:")
    product2 = {
        'name': product_name,
        'price': int(product_price)
    }

    products.append(product2)


def find_product():
    product_find = input("Zadej název produktu: ").lower()

    productFound = [product for product in products if product['name'].lower().startswith(product_find)]

    if productFound:
        print("Výsledek vyhledávání:")
        for product in productFound:
            print(f"Název: {product['name']}, Cena: {product['price']}$")
    else:
        print("Produkt nenalezen")


def total_price():
    price = 0
    for product in products:
        price += product ['price']
    return price


def lowest_price():
    lowest = products[0]
    lowest_price = lowest["price"]
    for product in products[1:]:
        if product["price"] < lowest_price:
            lowest_price = product["price"]
            lowest_products = [product]
        elif product["price"] == lowest_price:
            lowest_products.append(product)
    return lowest_products


def highest_price():
    highest = products[0]
    highest_products = [products[0]]
    highest_price = highest["price"]
    for product in products[1:]:
        if product["price"] > highest_price:
            highest_price = product["price"]
            highest_products = [product]
        elif product["price"] == highest_price:
            highest_products.append(product)
    return highest_products


def average_price():
    allProducts = sum(product['price'] for product in products)
    averagePrice = allProducts/len(products)
    return averagePrice


def edit_product():
    print(print_products())
    edit = int(input("Vyber pořadí produktu k úpravě: ")) - 1
    products[edit]["name"] = input("Nový název: ")
    products[edit]["price"] = int(input("Nová cena: "))


def lowest_first():
    for i in range(len(products) - 1, 0, -1):
        for j in range(i):
            if products[j]["price"] > products[j + 1]["price"]:
                temp = products[j]
                products[j] = products[j + 1]
                products[j + 1] = temp
    print_products()






def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledat produkt(y)")
    print("4. Cena všech produktů")
    print("5. Nejlevnější produkt(y)")
    print("6. Nejdražší produkt(y)")
    print("7. Průměrná cena")
    print("8. Upravit produkt")
    print("9. Seřadit od nejlevnějšího\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()


    elif choice == 3:
        print("Vyhledání produktu:")
        find_product()
        print("")
        menu()

    elif choice == 4:
        print("Celková cena všech produktů:")
        print(total_price())
        print("")
        menu()


    elif choice == 5:
        print("Nejlevnější produkt(y):")
        lowest_products = lowest_price()
        for product in lowest_products:
            print(f"Název: {product['name']}, Cena: {product['price']}$")
        print("")
        menu()


    elif choice == 6:
        print("Nejdražší produkt(y):")
        highest_products = highest_price()
        for product in highest_products:
            print(f"Název: {product['name']}, Cena: {product['price']}$")
        print("")
        menu()


    elif choice == 7:
        print("Průměrná cena:")
        print(average_price())
        print("")
        menu()


    elif choice == 8:
        print("Produkty pro úpravu:")
        edit_product()
        print("")
        menu()


    elif choice == 9:
        print("Seřadit od nejlevnějšího:")
        lowest_first()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
