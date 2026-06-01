#!/bin/python3

class Plant:
    start_height = 0
    gap = 0.8  # make the plants behaviors that will drive grow() differently

    def __init__(self, _name, _height, _age):
        self._name = _name
        self.start_height = _height
        self._height = _height
        self._age = _age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 2)}cm, ", end="")
        print(f"{self._age} days old")

    def grow(self) -> None:
        for x in range(7):
            print(f"=== Day {x + 1} ===")
            self._height += self.gap
            self.gap += 0.1
            self._age += 1
            self.show()

    def age(self) -> int:
        return self._age

    def get_growth_week(self) -> int:
        return (round(self._age - self.start_height, 2))


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 20)
    rose.grow()
    print(f'Growth this week: {rose.get_growth_week()}cm')
