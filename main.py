# Iterator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]

print("Печать элемента каждого вложенного списка")
for item in FlatIterator(nested_list):
    print(item)

print("Плоский список")
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# Generator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def flat_generator(flats):
    for numb in nested_list:
        for el in numb:
            yield el


print("Печать элемента каждого вложенного списка")
for item in flat_generator(nested_list):
    print(item)

print("Плоский список")
flat_list = list(flat_generator(nested_list))
print(flat_list)
