print("Hello Python")

#  string
# const_my_name = "MY NAME IS Azhar"
# print(my_name)

my_name = "MY NAME IS Farzam"
# print(my_name)

# Checking memory addresses
# print(hex(id(my_name)))

# char
my_pet_name = "A"

# integer
my_age = 23

# float
my_salary = 50000.000

# boolean
graduate = False

# list (mutable)
names_list = ["farzam", 23, False, 23, "azhar", "asfar", 26, "ashar", 27, "hammad", 24, "shaheer", 20]
# print(names_list)
names_list[7] = "not ashar"
# print(names_list)


# tuple (immutable)
names_tuple = ("farzam", 23, False, 23, "azhar", "asfar", 26, "ashar", 27, "hammad", 24, "shaheer", 20)
# names_tuple[2] = True
# print(names_tuple)


author = "Farzam"
book_name = "How to teach python to a noob"
pages = 500
price = 8000


library = ["Farzam", "How to teach python to a noob", 500, 6000]
# print(library)
library = {'author': "farzam", "book_name": "How to teach python to a noob", "pages": 500, "price": 6000}
print(library['book_name'])