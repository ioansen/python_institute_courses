def my_function1():
    var = 2
    print("Do I know that variable?", var)


def my_function2():
    global var
    var = 2
    print("Do I know that variable?", var)

def my_function3(n):
    print("I got", n)
    n += 1
    print("I have", n)

def my_function4(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

def my_function5(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

var = 1
my_function1()
print(var)

print()

my_function2()
print(var)

print()

my_function3(var)
print(var)

print()

my_list_2 = [2, 3]
my_function4(my_list_2)
print("Print #5:", my_list_2)

print()

my_function5(my_list_2)
print("Print #5:", my_list_2)