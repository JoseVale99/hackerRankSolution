


from collections import OrderedDict


if __name__ == '__main__':
    n = int(input(''))
    

    product_dic = OrderedDict()
    veces = []
    for i in range(n):
        *name, price = input().split()
        if len(name) > 1:
            product_dic [name[0]+' '+name[1]] = price
            veces.append(str(name[0]+' '+name[1]))
        else:
            product_dic [name[0]] = price
            veces.append(str(name[0]))
    for name in product_dic:
        price = product_dic.get(name)
        if name in veces:
            product_dic[name] = int(price) * veces.count(name)
    

    for name,price in product_dic.items():
        print('{} {}'.format(name,price))
