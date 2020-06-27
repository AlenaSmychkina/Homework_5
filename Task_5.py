def my_sum():
    try:
        with open("test_5.txt", "w+", encoding="utf8") as file_obj:
            line = input("Enter numbers separated by space: \n")
            file_obj.writelines(line)
            my_numb = line.split()

            print(f"The total {sum(map(int, my_numb))}")
    except IOError:
        print("Error!")
    except ValueError:
        print("Error. Please enter the number.")


my_sum()

