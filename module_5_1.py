# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self. number_of_floors = number_of_floors
    def go_to(self, new_floor):
 # Условие: Если же new_floor больше чем self.number_of_floors или меньше 1,:
        if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
        else:
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно):
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)