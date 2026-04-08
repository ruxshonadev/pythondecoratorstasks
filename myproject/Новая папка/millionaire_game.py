import json
from datetime import datetime

with open('questions.json', 'r', encoding='utf-8') as f:
    savollar = json.load(f)

print("=" * 50)
print("WHO WANTS TO BE A MILLIONAIRE")
print("=" * 50)
ism = input("\nIsmingiz: ")
if not ism:
    ism = "Anonim"

ball = 0


for i, savol in enumerate(savollar, 1):
    print(f"\n{'=' * 50}")
    print(f"SAVOL {i}/{len(savollar)} - BALL: {ball}")
    print(f"{'=' * 50}")
    print(f"\n{savol['question']}\n")

    harflar = ['a', 'b', 'c', 'd']
    togri = None

    for j, javob in enumerate(savol['answers']):
        print(f"{harflar[j]}) {javob['key']}")
        if javob['isTrue']:
            togri = harflar[j]

    j = input("\nJavob (a/b/c/d) yoki 'chiqish': ").lower()

    if j == 'chiqish':
        print(f"\nSiz {ball} ball bilan chiqdingiz!")
        break

    if j == togri:
        ball += 100
        print(" TO'G'RI!")
    else:
        print(f" Noto'g'ri! To'g'ri javob: {togri}")
        break
else:
    print(f"\n TABRIKLAYMIZ! {ball} BALL!")

try:
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
except:
    users = []

users.append({
    "ism": ism,
    "ball": ball,
    "sana": datetime.now().strftime("%Y-%m-%d %H:%M")
})

users.sort(key=lambda x: x['ball'], reverse=True)

with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("\n Natija saqlandi!")

print("\nTOP 5:")
for i, u in enumerate(users[:5], 1):
    print(f"{i}. {u['ism']} - {u['ball']} ball")