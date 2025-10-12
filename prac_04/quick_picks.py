"""
import random
NUMBER_OF_PICKS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
function main():

    get quick_picks_count
    for _ in range(quick_picks_count):
        get quick_pick
        while len(quick_pick) < NUMBER_OF_PICKS:
            get number
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print "" ".join(f"{num:2}" for num in quick_pick)"

main()
"""
import random
NUMBER_OF_PICKS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
def main():

    quick_picks_count = int(input("How many quick picks? "))
    for _ in range(quick_picks_count):
        quick_pick = []
        while len(quick_pick) < NUMBER_OF_PICKS:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

main()