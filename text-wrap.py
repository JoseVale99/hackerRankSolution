import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
  
    word_list = wrapper.wrap(text=string)
  
    result =""
    for element in word_list:
        result += element+"\n"

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)