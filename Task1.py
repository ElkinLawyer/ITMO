class Chocolate:
    def __init__(self, price: float, addition: str = None):
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self.price = price
        self.addition = addition

    def show_my_chocolate(self):
        if self.addition:
            return f"Шоколадный батончик, добавка: {self.addition}"
        else:
            return "Обычный шоколадный батончик"

    def __str__(self):
        return f"Шоколадный батончик, {self.price} рублей"


choco1 = Chocolate(100, "карамель")
print(choco1)
print(choco1.show_my_chocolate())

choco2 = Chocolate(80)
print(choco2)
print(choco2.show_my_chocolate())

try:
    choco_wrong = Chocolate(-20)
except ValueError as e:
    print(e)
