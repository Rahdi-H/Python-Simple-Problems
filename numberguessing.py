actual_number = 56
attempts = 0

while True:
    attempts += 1
    guess = int(input("guess the number:\n"))
    if guess < actual_number:
        print("your guess is too low")
    elif guess > actual_number:
        print('your guess is too high')
    else:
        print(f'Hurry, You won at {attempts} attempts')
        