import csv

# Read Wimbledon men's singles champion data (1968-2022)
wimbledon_data = []
with open('wimbledon.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        if row[0] != '2020':  # Exclude the 2020 event cancellation record
            wimbledon_data.append(row)

# Count the number of championships won by each champion
champion_count = {}
for row in wimbledon_data:
    champion = row[1]
    if champion in champion_count:
        champion_count[champion] += 1
    else:
        champion_count[champion] = 1

# Count the number of championships by the country of the champion
country_count = {}
for row in wimbledon_data:
    country = row[2]
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1
# Format and output the results
print("=== Wimbledon Gentlemen's Singles Champions Statistics (1968-2022) ===")
print("\n### Top 5 Champions by Number of Titles")
sorted_champions = sorted(champion_count.items(), key=lambda x: x[1], reverse=True)
for i, (champion, count) in enumerate(sorted_champions[:5], 1):
    print(f"{i}. {champion} - {count} times")

print("\n### Top 5 Countries by Number of Titles")
sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)
for i, (country, count) in enumerate(sorted_countries[:5], 1):
    print(f"{i}. {country} - {count} times")

print("\n### Examples of Championship Years and Scores")
for row in wimbledon_data[-5:]:  # Take the last 5 valid data entries
    print(f"Year {row[0]}: {row[1]} ({row[2]}) defeated {row[3]} ({row[4]}), score {row[5]}")