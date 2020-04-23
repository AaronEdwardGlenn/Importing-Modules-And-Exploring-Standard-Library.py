
print('Imported my_module...')

test = 'Test String'


def find_index(to_serach, target):
    for i, value in enumerate(to_serach):
        if value == target:
            return i

    return -1
