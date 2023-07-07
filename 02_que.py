
#sort a list

def sortlist(lists, argue):
    if argue == 'none':
        return lists
    elif argue =='asc':
        lists.sort()
        return lists
    else:
        return sorted(lists,reverse=True)

lists = [3,4,5,6,1,2]
argue = 'des'

x=sortlist(lists, argue)
print(x)