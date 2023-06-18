from random import randint

ran_num = randint(1,100)
print(ran_num)

num_try = 1

while True:
    inp = int(input('Enter your guess from 1-100 : '))

    if inp < 1 or inp > 100:
        print("OUT OF BOUNDS")
        continue

    if inp == ran_num:
        print(f'you have guessed the number correctly!!!  NUMBER OF TRIES : {num_try}')
        break

    if num_try == 1:
        if (abs(ran_num - inp) <= 10) and (abs(ran_num - inp) >= 1):
            num_try += 1
            print("WARM!")

        else:
            num_try += 1
            print("COLD!")
        prev_inp = inp
    else:
        num_try += 1
        if abs(ran_num - inp) > abs(ran_num - prev_inp):
            print("COLDER!")
        else:
            print("WARMER!")
        prev_inp = inp
