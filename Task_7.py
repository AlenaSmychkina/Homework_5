import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open("test_7.txt", "r", encoding="utf8") as file:
    for line in file:
        name, firm, earning, lost = line.split()
        profit[name] = int(earning) - int(lost)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f"Average income - {prof_aver:.2f} rubles.")
    else:
        print(f"You lost")
    pr = {"Average income is": round(prof_aver)}
    profit.update(pr)
    print(f"The income for every company - {profit}")

with open("test_7.json", "w", encoding="utf8") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f"The file json contents the whole data: \n "
          f" {js_str}")

