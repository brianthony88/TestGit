# my_input = input('what is your input ')
# print(my_input)

# x = 0

# while x <= 100:
#     print(x)
#     x += 1

while True:
    my_name = input('What is your name?\n')
    if my_name.lower()[0] in 'abcdefg':
        print('Please procede to table One')
    elif my_name.lower()[0] in 'hijklmnop':
        print("Please procede to table Two")
    elif my_name.lower()[0] in 'qrstuvwxyz':
        print('Please proceed to table Three')
    elif my_name.lower() == 'quit':
        # break
        