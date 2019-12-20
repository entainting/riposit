lst = range(-50,376)

for value in lst:
    if value % 2 and value % 1:
        print('foobar')
    elif value % 2:
        print('foo')
    elif value % 1:
        print('bar')
    else:
        print(value)
