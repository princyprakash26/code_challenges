#just the numbers

def just_num():
    num = []
    string = []
    lists = [-1,-6,-5,-6,-7,'hello','world']
    for word in lists:
        if isinstance(word, int):
            num.append(word)
            
        elif isinstance(word, str):
            string.append(word)

    print(num)
       

just_num()
