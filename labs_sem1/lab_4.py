class Laptop:
    # def __init__(self):
    #     self._cpu = 0
    #     self._ram = 0
    #     self._name = "name"

    def __init__(self, cpu, ram, name, weight, battery):
        self._cpu = cpu
        self._ram = ram
        self.__name = name
        self.weight = weight  # public field
        self.battery = battery

    def get_cpu(self):
        return self._cpu

    def set_cpu(self, new_cpu):
        self._cpu = new_cpu

    def __str__(self):
        return (f"Laptop information_str: CPU = {self._cpu} GHz, RAM = {self._ram} GB,"
                f" Name = {self._name}, Weight = {self.weight} Kg, Battery = {self.battery} mAh")

    def __repr__(self):
        return f"Laptop information_repr: CPU = {self._cpu} GHz, RAM = {self._ram} GB, Name = {self._name}"


laptop1 = Laptop(0.98, 9, "Lenovo", 1.5, 15000)
# laptop1.set_cpu(2.09)
# print(laptop1.__str__())
# print(laptop1.__repr__())
# print(laptop1.get_cpu())
print(laptop1.__cpu)

