translator = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

result = []
with open("test_4_1.txt", "r", encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split(" ", 1)
        result.append(translator[i[0]] + "  " + i[1])
    print(result)

with open("test_4_2.txt", "w", encoding="utf-8") as file_obj_2:
    file_obj_2.writelines(result)

