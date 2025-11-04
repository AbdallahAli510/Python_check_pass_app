import re


def assess_password_strength(pwd):
    # Check for the presence of lowercase letters, uppercase letters, numbers, and special characters
    has_lower = re.search(r"[a-z]", pwd) is not None
    has_upper = re.search(r"[A-Z]", pwd) is not None
    has_digit = re.search(r"[0-9]", pwd) is not None
    has_special = re.search(r"[!@#$^%]", pwd) is not None
    is_lengthy = len(pwd) >= 8

    # Calculate the strength score
    score = sum([has_lower, has_upper, has_digit, has_special, is_lengthy])

    # Categorize the password strength
    if score == 5:
        return (
            "Very strong password",
            "The password contains uppercase and lowercase letters, numbers, special characters, and is of sufficient length.",
        )
    elif score >= 3:
        return (
            "Medium password",
            "The password meets some requirements but can be improved.",
        )
    else:
        return (
            "Weak password",
            "The password does not meet enough requirements. Try adding uppercase and lowercase letters, numbers, and special characters.",
        )


while True:
    password = input("Enter the password: ")
    strength, feedback = assess_password_strength(password)
    print(f"{strength}: {feedback}")
    if strength == "Very strong password":
        break
