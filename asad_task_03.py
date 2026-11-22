# ============================================================
#  BioSkillz CodeStart — Python Foundations | Batch 01
#  TASK 03: Loops (Session 03)
# ============================================================
#
#  Name            : Muhammad Asad
#  GitHub username : Muhammadasad43
#  Date            : 22 November 2026
#
#  DEADLINE: Friday, 27 November 2026, 9:00 PM (PKT)
# ============================================================


# ############################################################
#  PART A: SESSION EXERCISES (from the slides)
# ############################################################

# ------------------------------------------------------------
# Exercise 1: Predict the output
# ------------------------------------------------------------
# 1)  for i in range(3):
#         print("Hi", i)
#     My prediction: Hi 0 / Hi 1 / Hi 2 (three lines; range(3) gives 0, 1, 2)
#
# 2)  x = 0
#     for i in range(1, 4):
#         x += i * 2
#     print(x)
#     My prediction: 12  (2 + 4 + 6)
#
# 3)  for i in range(3, 0, -1):
#         print(i, end="")
#     My prediction: 321  (counts down, end="" keeps it on one line)
#
# 4)  for ch in "code":
#         if ch == "d": break
#         print(ch, end="")
#     My prediction: co  (the loop stops when it reaches "d")
#
# 5)  for i in range(6):
#         if i % 3 == 0: continue
#         print(i, end=" ")
#     My prediction: 1 2 4 5  (0 and 3 are skipped)
#
# 6)  for i in range(2, 10, 3):
#         print(i, end=" ")
#     My prediction: 2 5 8  (start 2, step 3, stop before 10)

print("--- Exercise 1 ---")

for i in range(3):
    print("Hi", i)

x = 0
for i in range(1, 4):
    x += i * 2
print(x)

for i in range(3, 0, -1):
    print(i, end="")
print()

for ch in "code":
    if ch == "d":
        break
    print(ch, end="")
print()

for i in range(6):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

for i in range(2, 10, 3):
    print(i, end=" ")
print()


# ------------------------------------------------------------
# Exercise 2: Find and fix 4 bugs
# ------------------------------------------------------------
# Original buggy program:
#
#     count = 1
#     while count <= 5
#         print(count)
#
#     for i in range(1, 5):
#         total = 0
#         total += i
#     print("Sum of 1 to 5:", total)

print("--- Exercise 2 ---")

count = 1
while count <= 5:           # Bug 1 (SyntaxError): the while line was missing a colon
    print(count)
    count += 1              # Bug 2 (infinite loop): count never changed, so it never reached 6

total = 0                   # Bug 3 (wrong answer): total = 0 was inside the loop and reset
                            # the sum on every round. It must be set once, before the loop.
for i in range(1, 6):       # Bug 4 (wrong answer): range(1, 5) stops at 4. Use range(1, 6)
    total += i              # to include 5.
print("Sum of 1 to 5:", total)


# ------------------------------------------------------------
# Exercise 3: Number guessing game
# ------------------------------------------------------------
import random

print("--- Exercise 3 ---")

secret = random.randint(1, 10)
tries = 0

while True:
    guess_text = input("Guess (1-10): ").strip()
    if not guess_text.isdigit():        # ignore typos instead of crashing
        print("Please enter a whole number")
        continue

    guess = int(guess_text)
    tries += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print(f"Correct! You took {tries} tries")
        break


# ############################################################
#  PART B: TASKS
# ############################################################

# ------------------------------------------------------------
# Task 1: Multiplication table
# ------------------------------------------------------------
print("--- Task 1 ---")

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ------------------------------------------------------------
# Task 2: Predict the output
# ------------------------------------------------------------
# 1)  for i in range(1, 4):
#         print(i * i, end=" ")
#     My prediction: 1 4 9
#
# 2)  total = 0
#     for i in range(0, 10, 3):
#         total += i
#     print(total)
#     My prediction: 18  (0 + 3 + 6 + 9)
#
# 3)  n = 3
#     while n > 0:
#         print(n)
#         n -= 1
#     My prediction: 3, 2, 1 (each on its own line)
#
# 4)  for ch in "loop":
#         if ch == "o":
#             continue
#         print(ch, end="")
#     My prediction: lp  (both "o" letters are skipped)
#
# 5)  count = 0
#     for i in range(5):
#         for j in range(2):
#             count += 1
#     print(count)
#     My prediction: 10  (5 outer rounds x 2 inner rounds)
#
# 6)  for i in range(5, 0, -2):
#         print(i, end=" ")
#     My prediction: 5 3 1

print("--- Task 2 ---")

for i in range(1, 4):
    print(i * i, end=" ")
print()

total = 0
for i in range(0, 10, 3):
    total += i
print(total)

n = 3
while n > 0:
    print(n)
    n -= 1

for ch in "loop":
    if ch == "o":
        continue
    print(ch, end="")
print()

count = 0
for i in range(5):
    for j in range(2):
        count += 1
print(count)

for i in range(5, 0, -2):
    print(i, end=" ")
print()


# ------------------------------------------------------------
# Task 3: Find and fix the bugs
# ------------------------------------------------------------
# Original buggy program:
#
#     total = 0
#     for i in range(1, 10)
#         if i % 2 = 0:
#             total += i
#     print("Sum of even numbers 1-10:", total)
#
#     count = 10
#     while count > 0:
#         print(count)

print("--- Task 3 ---")

total = 0
for i in range(1, 11):      # Bug 1 (SyntaxError): the for line was missing a colon.
                            # Bug 2 (wrong answer): range(1, 10) stops at 9 and misses 10,
                            # so the sum was 20 instead of 30. Use range(1, 11).
    if i % 2 == 0:          # Bug 3 (SyntaxError): = assigns, == compares.
        total += i
print("Sum of even numbers 1-10:", total)

count = 10
while count > 0:
    print(count)
    count -= 1              # Bug 4 (infinite loop): count never went down.


# ------------------------------------------------------------
# Task 4: Character counter
# ------------------------------------------------------------
print("--- Task 4 ---")

sentence = input("Sentence: ")

vowels = 0
digits = 0
spaces = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Digits:", digits)
print("Spaces:", spaces)


# ------------------------------------------------------------
# Task 5: Your field  (Option A: GC content)
# ------------------------------------------------------------
print("--- Task 5 ---")

dna = input("Enter a DNA sequence: ").strip().upper()

gc_count = 0
for base in dna:
    if base == "G" or base == "C":
        gc_count += 1

if len(dna) > 0:
    gc_content = (gc_count / len(dna)) * 100
    print(f"GC content: {gc_content}%")
else:
    print("No sequence entered")
