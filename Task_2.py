my_list = ["I do my homework\n", "Alena\n", "Difficult Python\n", "Oh, my God!\n"]

with open("test_2.txt", "w+", encoding="utf8") as file_obj:
    file_obj.writelines(my_list)

with open("test_2.txt", encoding="utf8") as file_obj:
    num_str = 0
    num_words = 0

    for my_str in file_obj:
        num_str += 1
        num_words = 0
        for element in my_str:
            if element == " " or element == "\n":
                num_words += 1

        print(f"There are {num_words} words in the line {num_str}")

print(f"There are {num_str} strings.")
