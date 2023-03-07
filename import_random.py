import random

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_roll_sum = (dice_1 + dice_2 )

result = True
while(result):
    if (dice_roll_sum == 7 or  dice_roll_sum == 11):
        print(f"The sum of dice is {dice_1} + {dice_2} = {dice_roll_sum}\nyou won")
        result = False
    elif (dice_roll_sum == 2 or  dice_roll_sum == 3 or dice_roll_sum == 12):
        print(f"The sum of dice is {dice_1} + {dice_2} = {dice_roll_sum}\nyou lose")
        result = False
    elif (dice_roll_sum == 4 or  dice_roll_sum == 5 or dice_roll_sum == 6 or dice_roll_sum == 8 or dice_roll_sum == 9 or dice_roll_sum == 10):
        goal = dice_roll_sum
        if (goal == 4 or goal == 5 or goal == 6 or goal == 8 or goal == 9 or goal == 10):
                print(f"The sum of dice is {dice_1} + {dice_2} = {dice_roll_sum}")
                print(f"Now your goal number is {dice_roll_sum}")
                last_test = True
                while(last_test):
                    dice_3 = random.randint(1, 6)
                    dice_4 = random.randint(1, 6)
                    dice_roll_sum_2 = (dice_3 + dice_4)
                    if (dice_roll_sum_2 == 7):
                        print(f"The sum of dice is {dice_3} + {dice_4} = {dice_roll_sum_2}\nyou lose")
                        last_test = False
                    elif (dice_roll_sum_2 == goal):
                        print(f"The sum of dice is {dice_3} + {dice_4} = {dice_roll_sum_2}\nyou won")
                        last_test = False
                    else:
                        print(f"The sum of dice is {dice_3} + {dice_4} = {dice_roll_sum_2}")
                                        
        break
        




        
