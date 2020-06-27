my_list = []
while True:
    a = input("Enter your data. To stop enter " ": ")
    if a == "":
        print(my_list)
        exit()
    else:
        a_2 = a + ""
        my_list.append(a_2)

    with open("test_1.txt", "w", encoding="utf8") as file_obj:
        file_obj.writelines(my_list)
