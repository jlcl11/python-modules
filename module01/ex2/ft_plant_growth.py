class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    initial_height = 25.0
    rose = Plant("Rose", initial_height, 30)

    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    total_increase = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_increase}cm")
