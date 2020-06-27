my_dict = {}
with open("test_6.txt", "r", encoding="utf8") as init_f:
    for line in init_f:
        subject, hours = line.split(":")
        hour_clear = hours.replace("-", " ").split()
        sum_hours = 0
        for element in hour_clear:
            sum_hours += int(element.split("(")[0])
        my_dict[subject] = sum_hours
    print(my_dict)



