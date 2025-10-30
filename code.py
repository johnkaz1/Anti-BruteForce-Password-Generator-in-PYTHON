#Password Generator For Registerations
import secrets
import string

# Define character pools
lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
specials = ['!', '@']

# Combine all characters
all_chars = lower_letters + upper_letters + numbers + specials

# Fixed password length
length = 20

# Ensure at least one of each category
password_chars = [
    secrets.choice(lower_letters),
    secrets.choice(upper_letters),
    secrets.choice(numbers),
    secrets.choice(specials)
]

# Fill the rest randomly
password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]

# Shuffle to remove predictable order
secrets.SystemRandom().shuffle(password_chars)

# Join into final password string
password = ''.join(password_chars)

print("Generated password:", password)
