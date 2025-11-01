from prac_06.guitar import Guitar
# Test the first guitar
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
age1 = guitar1.get_age()
vintage1 = guitar1.is_vintage()
print(f"Gibson L-5 CES get_age() {age1}")
print(f"Gibson L-5 CES is_vintage() {vintage1}")
# Test the second guitar
guitar2 = Guitar("Another Guitar", 2013, 0)
age2 = guitar2.get_age()
vintage2 = guitar2.is_vintage()
print(f"Another Guitar get_age() {age2}")
print(f"Another Guitar is_vintage() {vintage2}")