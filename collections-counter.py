from collections import Counter

if __name__ == '__main__':
    
    n = int(input())
    
    number_shoes = input().split()
    customers = int(input())

    total = 0
    for customer in range(customers):
        numberShoes, price = input().split()

        if numberShoes in number_shoes and Counter(number_shoes).get(numberShoes)>0:
            number_shoes.remove(numberShoes) # -1 in stock
            total += int(price)
    print(total)
            
       


