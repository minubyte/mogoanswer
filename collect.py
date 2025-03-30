import os
import json

answers = {}

filenames = os.listdir("ans/txt")
for filename in filenames:
    with open(f"ans/txt/{filename}") as file:
        for line in file.read().split("\n"):
            num, ans = line.split(",")
            if num not in answers:
                answers[num] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
            answers[num][ans] += 1

with open("ans/res.json", "w") as file:
    json.dump(answers, file, indent=4)