def strange_function(n):
    if(n % 2 == 0):
        return True
    
print(strange_function(2))
print(strange_function(1))

print(type(strange_function(1)))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

