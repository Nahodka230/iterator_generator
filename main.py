import types


def flat_generator(list_of_lists):
    counter = 0
    counter_in = 0
    while counter < len(list_of_lists):
            while counter_in < len(list_of_lists[counter])-1:
                item = list_of_lists[counter][counter_in]
                counter_in +=1
                yield item
            else:
                item = list_of_lists[counter][counter_in]
                counter_in = 0
                counter += 1
                yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = 0
        self.counter_in = 0
        return self


    def __next__(self):
        if self.counter < len(self.list_of_list):
            if self.counter_in < len(self.list_of_list[self.counter])-1:
                item = self.list_of_list[self.counter][self.counter_in]
                self.counter_in +=1
                return item
            else:
                item = self.list_of_list[self.counter][self.counter_in]
                self.counter_in = 0
                self.counter += 1
                return item

        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    test_2()