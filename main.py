class MyDict:
    def __init__(self):
        self._data = []

    def __getitem__(self, key):
        for k, v in self._data:
            if k == key:
                return v
        return None

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self._data):
            if k == key:
                self._data[i] = (key, value)
                return
        self._data.append((key, value))

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self._data):
            if k == key:
                del self._data[i]
                return

    def __str__(self):
        items_str = ", ".join(f"{k}: {v}" for k, v in self._data)
        return f"{{{items_str}}}"

    def __contains__(self, key):
        for k, v in self._data:
            if k == key:
                return True
        return False

    def keys(self):
        return [k for k, v in self._data]

    def values(self):
        return [v for k, v in self._data]

    def items(self):
        return list(self._data)



my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict)
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict.items())
