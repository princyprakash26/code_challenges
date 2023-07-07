
#count the vowels in string:

def function(txt):
    vowels = 0
    y = 0
    for char in txt.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowels += 1
        else:
            y += 1
    print(vowels)
function('asees')
