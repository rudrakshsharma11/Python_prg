def billing(order, file):
    total = 0
    name = "Item"
    num = "Quantity"
    cost = "Price"
    total_sale = "Total price"
    file.write("\t\t......Mega Store.......\n\n")
    file.write(f'{name:{20}} {num:^50}{cost:^40}{total_sale:>10}' + '\n')


    for item, price in order.items():
        price[1] = float(price[1])
        tat_price = price[1] * price[0]
        file.write(f'{item:{20}} {price[0]:^50} {price[1]:^40} {tat_price:>10}' + '\n')
        total += tat_price

    file.write('\n' + 'Total = ' + format(total, '.2f') + '\n')
    file
    file.close()

    sold = {"Rice": [1, 30], "Sugar": [1, 50], "Sauses": [10, 10]}
    file = open('rd.txt', 'w')
    billing(sold, file)
