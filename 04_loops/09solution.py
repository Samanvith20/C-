items = ["apple", "banana", "orange", "apple", "mango"]

# Create an empty set to store seen items
seen = set()

# Loop through each item in the list
for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break  # Exit the loop once a duplicate is found
    seen.add(item)
else:
    print("All elements are unique")
