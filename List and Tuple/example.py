# List example - shopping cart (items can change)
shopping_cart = ['milk', 'bread']
shopping_cart.append('eggs')  # Can add items
shopping_cart.remove('bread') # Can remove items

# Tuple example - person's basic info (shouldn't change)
person_info = ('John', 'Doe', 1990)  # name, surname, birth_year
# person_info[0] = 'Jane'  # This would cause an error!

# Tuple for function return
def get_name_age():
    return ('Alice', 25)  # Returns tuple

name, age = get_name_age()  # Unpacking