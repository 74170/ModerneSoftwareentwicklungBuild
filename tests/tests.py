import unittest
import day1

class TestHighestFoodCountForOneElf(unittest.TestCase):

    def test_elf_calc_max_food(self):
        elf = day1.Elf()
        elf.items_list = [10, 20, 30]
        elf.calc_max_food()
        assert elf.maximum_food == 60
    
    def test_get_elf_with_max_food(self):
        elf1 = day1.Elf()
        elf1.maximum_food = 50
        elf2 = day1.Elf()
        elf2.maximum_food = 100
        elf3 = day1.Elf()
        elf3.maximum_food = 75
        elf_list = [elf1, elf2, elf3]
        assert day1.get_elf_with_max_food(elf_list) == elf2

if __name__ == '__main__':
    unittest.main()