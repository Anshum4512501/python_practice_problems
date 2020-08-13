sep = '-' * 32 + '\n'
print(sep)
try:
    x = 'spam'[13]
    print(x)
except IndexError:
    print('except run')
finally:
    print('finally run')
    print('after run')