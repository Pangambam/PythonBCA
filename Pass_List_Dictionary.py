def print_list_items(items):
    print("List items:")
    for item in items:
        print(item)

def print_dict_items(info):
    print("Dictionary items:")
    for key, value in info.items():
        print(key, ":", value)

# Function calls
my_list = ["apple", "banana", "cherry"]
my_dict = {"name": "Rahul", "age": 22, "city": "Delhi"}

print_list_items(my_list)
print_dict_items(my_dict)
