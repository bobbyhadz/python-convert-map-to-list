# Convert a Map object to a List in Python

my_list = ['1.1', '2.2', '3.3']

new_list = list(map(float, my_list))
print(new_list)  # 👉️ [1.1, 2.2, 3.3]

print(type(new_list))  # 👉️ <class 'list'>
