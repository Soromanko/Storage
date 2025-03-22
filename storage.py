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
    for product in products:
        if product["price"] < lowest["price"]:
            lowest = product
    return lowest



def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledat produkt(y)")
    print("4. Cena všech produktů")
    print("5. Nejlevnější produkt\n")

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
        print("Nejlevnější produkt je:")
        print(lowest_price())
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
