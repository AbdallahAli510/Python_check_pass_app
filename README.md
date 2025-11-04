# Python_check_pass_app
# 🔒 Password Strength Checker

A small terminal-based **Password Strength Checker** written in Python.  
It evaluates a password for lowercase, uppercase, digits, special characters, and minimum length, then gives a simple strength rating and feedback.

---

## Table of Contents
- [About](#about)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example Session](#example-session)  
- [How it works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  
- [Script (`password_strength_checker.py`)](#script-password_strength_checkerpy)

---

## About
This script checks a user-entered password against basic rules (lowercase, uppercase, number, allowed special characters, and minimum length) and prints a strength classification with helpful feedback. It's intended as a teaching example and a quick CLI tool.

---

## Features
- Checks for: lowercase, uppercase, digits, specific special characters, and length (≥ 8).  
- Returns three categories: **Very strong**, **Medium**, **Weak**.  
- Simple, dependency-free, and easy to read.

---

## Requirements
- Python 3.x

---

## Installation
1. Create a new file in your repository (recommended name: `password_strength_checker.py`).  
2. Paste the script from the **Script** section below.  
3. Commit and push to your GitHub repository (optionally add this README as `README.md`).

---

## Usage
Run the script from the terminal:

```bash
python password_strength_checker.py
```

Enter the password when prompted. The script will display the strength message and feedback. If the password is judged *Very strong*, the program exits; otherwise it keeps asking for a new password.

---

## Example Session

```
$ python password_strength_checker.py
Enter the password: hello
Weak password: The password does not meet enough requirements. Try adding uppercase and lowercase letters, numbers, and special characters.
Enter the password: Hello123
Medium password: The password meets some requirements but can be improved.
Enter the password: Hello@123
Very strong password: The password contains uppercase and lowercase letters, numbers, special characters, and is of sufficient length.
```

---

## How it works
1. Uses Python's `re` module to check existence of:
   - lowercase letters `[a-z]`
   - uppercase letters `[A-Z]`
   - digits `[0-9]`
   - special characters from the set `! @ # $ ^ %` (`[!@#$^%]`)
   - length at least 8 characters
2. Sums the boolean results to compute a score (0–5).  
3. Interprets the score:
   - `5` → **Very strong password**
   - `3` or `4` → **Medium password**
   - `< 3` → **Weak password**
4. Prints a message + feedback and continues or exits depending on strength.

---

## Customization
- Expand the special characters set (update the regex `[!@#$^%]`) to include more symbols.  
- Require a longer minimum length (change `is_lengthy = len(pwd) >= 8`).  
- Add checks for repeated characters, common words, or dictionary lookup to detect weak patterns.  
- Return machine-friendly output (JSON) for use in other scripts or web backends.  
- Add command-line flags (use `argparse`) to run a one-off check or to read passwords from a file (careful with security).

---

## Contributing
Small improvements are welcome:
- Add unit tests for the checker.  
- Add a CLI argument to change required rules.  
- Improve feedback to suggest exact fixes (e.g., "add a symbol" vs. generic advice).

---

## License
Use freely. Add an open-source license file (e.g., MIT) to clarify reuse if desired.

---

## Script: `password_strength_checker.py`
Copy the exact code below into `password_strength_checker.py`:

```python
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
```
