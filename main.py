import json
import random


print("Welcome to 'Who Wants to Be a Billionaire?'")

with open("tests.json","r", encoding="utf=8") as f:
    questions = json.load(f)


try:
    with open("users.json","r", encoding="utf-8") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}


def user_add(name):
    if name not in users:
        users[name]={"partipication": 0, "best_score": 0}


def show_users():
    print(f"\n{'Name':<15} {'Participation':<15} {'Best Score':<10}")
    print("-" * 40)
    for name, info in users.items():
        print(f"{name:<15} {info['partipication']:<15} {info['best_score']:<10}")


def game(name):
    ball = 0
    random.shuffle(questions)

    for i, savol in enumerate(questions):
        print(f"\n {i+1}-savol: {savol["question"]}")

        for j, javob in enumerate(savol["answers"]):
            print(f"\n {j+1}. {javob['key']}")

        tanlov = input("Enter your choice? (1-4): ")

        tanlangan = savol["answers"][int(tanlov)-1]


        if tanlangan["isTrue"]:
            ball +=1
            print("togri")

        else:
            print("Xato, o'yin tugadi.")
            break


    print(f"\n{name}, sizning balingiz : {ball}")
    return ball


def save_result(name, ball):
    users[name]["partipication"] += 1
    if ball > users[name]["best_score"]:
        users[name]["best_score"]= ball

    with open("users.json", "w", encoding="utf-8")  as f:
        json.dump(users,f, ensure_ascii=False, indent=4)


name = input("Enter your name?..")
user_add(name)
ball = game(name)
save_result(name, ball)
show_users()