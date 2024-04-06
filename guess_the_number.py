import random

play = 1
while play:
    a = int(input("Enter your lower limit: "))
    b = int(input("Enter your upper limit: "))
    number = random.randrange(a, b)

    s = int(input(f"Pick a number between {a} and {b}: "))

    if s == number:
        print(f"Random number was {number} and your guess was {s}. Correct!")
        go = input("Wanna play again?\n")
        if go.lower() == 'yes':
            play = 1
    else:
        print(f"Random number was {number} but your choice was {s}:( \nMaybe next time!")
        go = input("Wanna play again?\n")
        if go.lower() == 'no':
            play = 0