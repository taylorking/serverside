def sum(*args): 
    sum = 0 
    for i in range(0, len(args)):
        sum+=args[i]
    return sum
def mean(*args):
    sum = 0 
    for i in range(0, len(args)): 
        sum+=args[i]
    return sum / len(args)
def median(*args):
    my_args = list(args)
    return (my_args[len(my_args) // 2]) 
def standard_deviation(*args): 
    # Not totally sure this is correct.. I googled it
    args = list(args)
    results = 0 
    for i in range(0,len(args) - 1):
        results += (args[i +1] - args[i]) ** 2
    return results / len(args)
