class Elf:
    def __init__(self):
        self.items_list = []
        self.maximum_food = 0

    def calc_max_food(self):
        for item in self.items_list:
            self.maximum_food += int(item)


def get_elf_with_max_food(elf_list):
    elf_with_most_food = elf_list[0]
    for elf in elf_list:
        if elf.maximum_food > elf_with_most_food.maximum_food:
            elf_with_most_food = elf
    return elf_with_most_food

def main_cycle(file_input=""):
    if file_input:
        print(file_input)

    elf_list = []
    user_input = None
    running = True
    counter = 0
    while running:
        user_input = input()
        while user_input:
            if user_input == "n":
                break
            if counter == 0:
                print("Creating elf")
                elf = Elf()
                elf_list.append(elf)
                counter = 1
            elf.items_list.append(int(user_input))
            user_input = input()
        counter = 0
        if user_input == "n":
            print(f"Finished input. There are {len(elf_list)} elves.")
            running = False
            break
    for elf in elf_list:
        elf.calc_max_food()
    print(f"The elf with the most food has {get_elf_with_max_food(elf_list).maximum_food} calories.")
    return get_elf_with_max_food(elf_list).maximum_food

if __name__ == '__main__':
    main_cycle()