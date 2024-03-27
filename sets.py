def remove_duplicates(ls):
    ls = set(ls)
    return(list(ls))

def remove_dupl_loop(ls):
    result = []
    for e in ls:
        if e not in result:
            result.append(e)     
    return(result)

ls = [1,2,2,2,3,3,4,6]
print(ls)
print(remove_duplicates(ls))
print(remove_dupl_loop(ls))