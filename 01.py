# dynamically typed : it can understand the var type
# primary data type
# a = 1 # this is a variable
# b = 1.35477
# c = "Nandani"
# d = True
# f = False
# print("A = ",a, type(a))
# print("B = ",b,type(b))

# compund data type : list,tuple,dictionary
list_a = [1,2,3,4,5,6,7,"nandani"] # mutable (can be changed)
tuple_b = (1,2,3,4,5,"nandani") # immutable (can't be changed)
# print(list_a)
dictionary_d = {
    "Name":"Nandani",
    "Age":21,
    "Salary":15000.537
}
# print(tuple_b)
# print(dictionary_d["Name"])
# print(dictionary_d["Age"])
dictionary_d["Salary"] = 15001.69
# print(dictionary_d)

def funAdd(a,b):
    sum = a + b
    return sum

def funSub(a,b):
    sub = a - b
    return sub

if __name__ == "__main__":
    total = funAdd(2,3)
    diff = funSub(5,7)
    print(total)
    print(diff)