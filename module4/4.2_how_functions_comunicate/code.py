def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
#adding(3, a = 1, b = 2) TypeError: adding() got multiple values for argument 'a'
adding(4, 3, c = 2)


introduction("Henry")
introduction()
introduction(last_name="Hopkins")


def my_f(a):
    print (a)
    print (b)


a  =  6
b = 13
my_f(12)
