if __name__ == '__main__':
    n = int(input())

    cities_set = set()
    for i in range(n):
        cities = input('')
        
        cities_set.add(cities.strip())
    

    print(len(cities_set))