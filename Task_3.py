firm = {"Ivanov": 10000, "Petrov": 15000, "Sidorov": 25000.1, "Ivanova": 15000.7, "Petrova": 19000.9,
        "Sidorova": 26000.1, "Oktyabrskiy": 30000.5, "Petrovskiy": 26000.4, "Znamenskiy": 12000, "Koretskiy": 31000.9}
try:
    file_obj = open("test_3.txt", "w", encoding="utf8")
    for last_name, salary in firm.items():
        file_obj.write(last_name + ":" + str(salary) + "\n")
except IOError:
    print("Error!")
finally:
    file_obj.close()
fin_sum = 0
count = 0
persons = []
with open("test_3.txt", "r", encoding="utf8") as file_obj:
    for line in file_obj:
        print(line, end="")
        elements = line.split(":")
        if float(elements[1]) <= 20000:
            persons.append(elements[0])
        fin_sum += float(elements[1])
        count += 1
result = fin_sum / count
print(f"Employees who have the salary below 20.000: {persons}")
print(f"The average salary is: {result}")