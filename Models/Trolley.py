from Models.Item import Item


class Trolley:

    def __init__(self):
        self.stored_items = []

    def add_item(self, item: Item):
        self.stored_items.append(item)

    def storage_space_calculator(self, item: Item):
        size_0 = 0
        size_1 = 0
        size_2 = 0
        size_3 = 0
        for x in self.stored_items:
            if x.size == "rekesz":
                size_0 += 1
            elif x.size == "viz":
                size_1 += 1
            elif x.size == "karton":
                size_2 += 1
            else:
                size_3 += 1
