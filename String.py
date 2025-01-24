# Step 1: Define the data
names = ["Jane", "Bob", "Xenia", "Delan", "Yunita"]
ages = [25, 30, 22, 29, 28]
countries = ["Kenya", "Canada", "South Africa", "Nigeria", "USA"]
allowed_countries = ("Kenya", "Nigeria", "South Africa")

# Step 2: Check if the last person's country is in the allowed_countries tuple
last_person_name = names[-1]
last_person_country = countries[-1]

if last_person_country in allowed_countries:
    print(f"{last_person_name} is from an allowed country.")
else:
    print(f"{last_person_name} is not from an allowed country.")

# Step 3: Summarize results
total_people = len(names)
from_allowed_countries = sum(1 for country in countries if country in allowed_countries)
not_from_allowed_countries = total_people - from_allowed_countries

print("\nSummary:")
print(f"Total number of people checked: {total_people}")
print(f"Number of people from allowed countries: {from_allowed_countries}")
print(f"Number of people not from allowed countries: {not_from_allowed_countries}")