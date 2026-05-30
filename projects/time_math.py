import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_porblem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)

    return exp, answer

wrong = 0

print("=" * 50)
print("🎮  MENTAL MATH CHALLENGE  🎮")
print("=" * 50)
print(f"📝 You will solve {TOTAL_PROBLEMS} math problems")
print("⏱️  The clock starts when you begin!")
print("=" * 50)
input("\n✨ Press enter to start!")
print()

start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_porblem()
    while True:
        guess = input(f"Problem #{i+1}/{TOTAL_PROBLEMS}: {exp} = ")
        if guess == str(answer):
            print("✅ Correct!\n")
            break
        else:
            print("❌ Wrong! Try again.")
            wrong += 1

end_time = time.time()

total_time = round((end_time - start_time), 2)

print("=" * 50)
print("🎉 Nice work! 🎉")
print("=" * 50)
print(f"✅ Total Correct: {TOTAL_PROBLEMS}")
print(f"❌ Total Mistakes: {wrong}")
print(f"⏱️  Time Taken: {total_time} seconds")
print("=" * 50)



      