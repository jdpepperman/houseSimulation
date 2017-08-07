from Room import Room


class Kitchen(Room):
    def __init__(self, house, name):
        Room.__init__(self, house, name)
