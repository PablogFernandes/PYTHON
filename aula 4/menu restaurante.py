def read_bank():
    # data sanitation 
    with open("estoque.csv", "r") as file:
        bank_data = file.read()
        stock_data = bank_data.split("\n")
        menu = stock_data [0].split(",")
        stock_quantity = stock_data[1].split(",")
        return menu, stock_quantity

menu_items = read_bank()[0]
menu_stock = read_bank()[1]

for position, itens in enumerate(menu_items):
    print(f"{position + 1} - {itens}")
request = int(input(">>> "))

menu_size = len(menu_items)

if request > menu_size or request < 1: 
    print("opção inválida")
    
#removing the input mask
request = request - 1 
menu_stock[request] = str(int(menu_stock[request]) - 1)
print(menu_stock)

with open("estoque.csv", "w") as file:
    file.write(','.join(menu_items))
    file.write("\n")
    file.write(','.join(menu_stock))