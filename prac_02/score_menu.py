"""
function main():
    get score
    get is_running
    while is_running:
        print "\n=== Score Management Menu ==="
        print "(G)et a valid score"
        print "(P)rint result"
        print "(S)how stars"
        print "(Q)uit"
        get choice
        if choice == "G":
            get score
        else if choice == "P":
            get print_result
        else if choice == "S":
            get show_stars
        else if choice == "Q":
            print "Thank you for using. Goodbye!"
            is_running = False
        else:
            print "Invalid option. Please select again."
function get_score_grade(score):
    if score >= 90:
        return "Excellent"
    else if score >= 80:
        return "Good"
    else if score >= 70:
        return "Average"
    else if score >= 60:
        return "Pass"
    else:
        return "Fail"
function get_valid_score():
    function inner_get_score():
        try:
            get score
            if 0 <= score <= 100:
                return score
            else:
                print "The score must be between 0 and 100. Please enter again."
                return inner_get_score()
        except ValueError:
            print "Please enter a valid integer."
            return inner_get_score()
    return inner_get_score()
function print_result(score):
    from score import get_score_grade
    get result
    print "Grade: {result}"

function show_stars(score):
    print""*" * score"
if __name__ == "__main__":
    main()

"""
def main():
    score = get_valid_score()
    is_running = True
    while is_running:
        print("\n=== Score Management Menu ===")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Please select an option: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using. Goodbye!")
            is_running = False
        else:
            print("Invalid option. Please select again.")

def get_score_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

def get_valid_score():
    def inner_get_score():
        try:
            score = int(input("Please enter a score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("The score must be between 0 and 100. Please enter again.")
                return inner_get_score()
        except ValueError:
            print("Please enter a valid integer.")
            return inner_get_score()
    return inner_get_score()

def print_result(score):
    from score import get_score_grade
    result = get_score_grade(score)
    print(f"Grade: {result}")

def show_stars(score):
    print("*" * score)



if __name__ == "__main__":
    main()