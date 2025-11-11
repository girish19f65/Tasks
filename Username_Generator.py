# ---USERNAME GENERATOR AND STRING ANALYZER---

print("=== WELCOME TO USERNAME_GENERATOR ===\n")
# Input user details
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Positive Indexing
print("\n--- INDEXING ---")
print(f"second character of first name: {first_name[1]}")
# Negative indexing
print(f"Last character of last name: {last_name[-1]}")

# Slicing Examples
print("\n--- SLICING ---")
print(f"First 4 letters of first name: {first_name[0:4]}")    # start:end
print(f"Every 2nd letter in last name: {last_name[::2]}")     # step slicing
# Negative slicing
print(f"Reverse of last name: {first_name[::-1]}")

# STRING METHODS
print("\n--- STRING METHODS ---")
print("Uppercase:", first_name.upper())
print("Lowercase:", last_name.lower())
print("Title Case:", first_name.title() + " " + last_name.title())
print("Length of first name:", len(first_name))
print("swapcase:", last_name.swapcase())
print("join first and last name with '-':", '.'.join([first_name, last_name]))
print("Capitalized:", first_name.capitalize())
print("starts with 'A':", first_name.startswith('Name:'))
print("ends with 'n':", last_name.endswith('Hello'))
print("Replace first name with '*':", first_name.replace('h', '*'))
print("Count of 'h' in last name:", first_name.count('h'))

# F-STRING FORMATTING
print("\n--- F-STRING FORMATTING ---")
name_length = len(first_name + last_name)
print(
    f"Your name has total {name_length:^10} characters (center aligned with spaces)")

# STRING ANALYSIS TECHNIQUES
print("\n--- STRING ANALYSIS ---")

full_name = (first_name + last_name).lower()
vowels = "aeiou"
vowel_count = sum(1 for char in full_name if char in vowels)
consonant_count = sum(
    1 for char in full_name if char.isalpha() and char not in vowels)

print(f"Total letters: {len(full_name)}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Digits in birth year: {sum(1 for ch in birth_year if ch.isdigit())}")


# USERNAME GENERATION USING STRING FORMATTING
username1 = first_name[:3].lower() + last_name[-3:].lower() + birth_year[-2:]
username2 = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"
username3 = f"{first_name[::-1].lower()}_{birth_year}"

print("\n--- GENERATED USERNAMES ---")
print(f"Username1: {username1}")
print(f"Username2: {username2}")
print(f"Username3: {username3}")

print("THANK YOU FOR USING THE USERNAME_GENERATOR")
