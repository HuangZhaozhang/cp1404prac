"""
import random
function main():
    get user_score
    print "user_score"
    get random_score
    print "random_score, level"
function get_score_grade():
    if score <= 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"
if __name__ == "__main__":
    main()
"""
import random
def main():
    user_score = float(input("Score: "))
    print(get_score_grade(user_score))
    random_score = random.uniform(0,100)
    print(f"Random score: {random_score:.2f}, Level: {get_score_grade(random_score)}")

def get_score_grade(score):
    if score <= 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

if __name__ == '__main__':
    main()