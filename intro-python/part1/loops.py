'''
while True:
    answer = input('Please provide a word: \nType "done" to finish> ')
    if answer == 'done':
        break
    print(answer)

def wartosc(arg1, arg2):
    result = arg1 - arg2
    return result

wartosc(20, 10)

print(wartosc)

'''

def hello(*args):
    for arg in args:
        print("hello", arg, "!")

hello("Caleb", "Pip", "Jim")

print(hello)