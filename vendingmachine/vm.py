from vendingmachine.parts import (MoneyEquipment, StorageEquiment, DisplayEquipment, InstructionEquipment)

class VendingMachine():
    def __init__(self):
        self.money_eq = MoneyEquipment()
        self.storage_eq = StorageEquiment()
        self.display_eq = DisplayEquipment()
        self.inst_eq = InstructionEquipment()

    def run(self):
        self.display_eq.display()

    def get_value(self):
        return 10

    def get_instance(self):
        return self.display_eq

    def __display_menu(self):
        pass

class DrinkVm(VendingMachine):
    def run(self):
        super().run()
        print("subclass run")
    def __display_menu(self):
        pass

if __name__ == "__main__":
    vm = VendingMachine()
    value1 = vm.get_value()
    value2 = vm.get_instance()

    print ("value1", type(value1))
    print ("value2", type(value2))
