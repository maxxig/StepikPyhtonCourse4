def hash_function(obj):
    st = str(obj)
    ln = len(st)
    res, delta = 0, -1
    iter = ln // 2
    for i in range(iter):
        # print(st[i], st[delta])
        # print(ord(st[i]), ord(st[delta]))
        res += ord(st[i]) * ord(st[delta])
        delta -= 1
    if ln % 2 == 1:
        res += ord(st[iter])
    temp1 = res
    temp2 = 0
    s = 0
    for i in range(len(st)):
        if s == 0:
            temp2 += ord(st[i]) * (i+1)
            s = 1
        else:
            temp2 -= ord(st[i]) * (i + 1)
            s = 0
    result = (temp1 * temp2) % 123456791
    return result

# TEST_4:
print(hash_function([1, 2, 3, 'python']))

# TEST_5:
array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

for obj in array:
    print(hash_function(obj))




