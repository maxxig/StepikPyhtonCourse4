def limited_hash(left, right, hash_function=hash):
    l = list(range(left, right+1,1))
    def func(obj):
        t = hash_function(obj)
        if left <= t <= right:
            return t
        elif t > right:
            r = (t - left) % (right - left+1)
            return l[r]
        else:
            r = (right - t) % (right - left+1)
            return l[len(l)-r-1]
    return func

# TEST_5:
def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))