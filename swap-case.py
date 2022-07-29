



def swap_case(s):

    string_c = "" 
    
    for string in s.split():
        case = ""
        for x in string:
            if x.islower() or x in ['.', '"', "?","'" ] or x.isnumeric():
                case += x.upper()
            elif x.isupper()  or x in  ['.', '"', "?","'" ] or x.isnumeric():
                case += x.lower()
        string_c += case + " "
    return string_c
# def swap_case(s):
#     return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)