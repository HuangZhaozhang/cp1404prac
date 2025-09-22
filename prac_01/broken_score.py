"""
get score
if score <= 0 or score > 100:
    print "Invalid score"
else if score>=90:
    print "Excellent"
else if score>=50:
    print "Pass"
else:
    print "Fail"
"""
score = float(input("Score: "))
if score<=0 or score>100:
    print("Invalid score")
elif score>=90:
    print("Excellent")
elif score>=50:
    print("Pass")
else:
    print("Fail")