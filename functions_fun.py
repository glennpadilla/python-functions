# def print_names(first_name, last_name):
#     print(first_name, last_name, sep = "|")

# print_names("Baz", "Sayid")

# def is_too_fast(current_speed, max_speed):
#     if current_speed <= max_speed:
#         return False
#     else:
#         return True

# is_too_fast(55, 55)

# Replace the line "# Write an if statement here"
# with an appropriate if statement

# def test_list(term, items):
#     for item in items:
#         if term == item:
#             return True
#     return False

# def test_list2(term, items):
#     for i in [1, 2, 3, 4]:
#         if term == i:
#             return True
#     return False

# test_list2(1,[1, 2, 3, 4])

# print(test_list2(1,[1, 2, 3, 4]))

# # Write your function add_two_numbers here
# def add_two_numbers(a, b):
#     sum = a + b
#     return sum

def add(*numbers):
    print(numbers)
    return None

total = add(1, 2, 3, 4)
print(total)
