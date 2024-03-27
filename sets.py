def remove_duplicates(ls):
    ls = set(ls)
    return(list(ls))
    
ls = [1,2,2,2,3,3,4,6]
print(ls)
ls = remove_duplicates(ls)
print(ls)