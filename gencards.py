import random

def luhn_checksum(card_number):
    """Calculate the Luhn checksum for a card number."""
    num_digits = len(card_number)
    checksum = 0
    for i in range(num_digits):
        digit = int(card_number[num_digits - i - 1])
        if i % 2 == 1:  # Double every second digit from the right
            digit *= 2
            if digit > 9:  
                digit -= 9  # Subtract 9 if the result is greater than 9
        checksum += digit
    return checksum % 10

def generate_card_number(prefix, length):
    """Generate a random card number with a specific prefix and length."""
    card_number = str(prefix)
    # Fill the card number with random digits until it reaches the desired length - 1
    card_number += ''.join([str(random.randint(0, 9)) for _ in range(length - len(card_number) - 1)])
    # Calculate the checksum digit
    checksum_digit = luhn_checksum(card_number + '0')
    card_number += str((10 - checksum_digit) % 10)  # Append the checksum digit
    return card_number

def generate_random_card():
    """Generate a random card number based on common prefixes."""
    prefixes = ['4', '5', '3', '6']  # Visa, MasterCard, American Express, Discover 
    prefix = random.choice(prefixes)
    length = 16 if prefix in ['4', '5', '6'] else 15  # Visa, MasterCard, Discover = 16; Amex = 15
    return generate_card_number(prefix, length)

# Generate and display a random card number
if __name__ == "__main__":
    random_card = generate_random_card()
    print(f"Случайный номер карты: {random_card}")
