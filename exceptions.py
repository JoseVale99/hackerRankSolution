
if __name__ == '__main__':
    cases = int(input(''))

    for case in range(cases):
       
        a,b = input().split()
    
        try:
            result = int(a)//int(b)

        except ZeroDivisionError as e:
            print('Error Code:',e)
        
        except ValueError as e:
            print('Error Code:',e)
        else:
            print(result)
        
            
            
            
