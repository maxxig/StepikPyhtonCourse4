class Closer:
    def __init__(self, obj):
        self.obj = obj
    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except:
            print("Незакрываемый объект")


# TEST_4:
unclosable = [3.14, 'Elon', {'Ч': 'LXXIV'}, [1, 2, 3], (4, 5, 6), True, False]

for item in unclosable:
    with Closer(item) as zf:
        print(item)
