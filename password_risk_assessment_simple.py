BLOCKLIST = ["password", "password123", "qwerty123", "12345678", "letmein", "admin123"]


def get_minimum_length(mfa):
    if mfa:
        return 8
    else:
        return 15


def check_blocklist(password):
    for word in BLOCKLIST:
        if password.lower() == word.lower():
            return True
    return False


def check_username(password, username):
    if len(username) >= 4:
        if username.lower() in password.lower():
            return True
    return False


def check_repeated_characters(password):
    if len(password) < 4:
        return False

    for i in range(len(password) - 3):
        if password[i] == password[i + 1]:
            if password[i] == password[i + 2]:
                if password[i] == password[i + 3]:
                    return True

    return False


def check_sequences(password):
    sequences = ["1234", "2345", "3456", "abcd", "bcde", "qwerty"]
    found = []

    for sequence in sequences:
        if sequence in password.lower():
            found.append(sequence)

    return found


def check_character_types(password):
    lowercase = False
    uppercase = False
    numbers = False
    special = False

    for character in password:
        if character.islower():
            lowercase = True
        elif character.isupper():
            uppercase = True
        elif character.isdigit():
            numbers = True
        else:
            special = True

    return lowercase, uppercase, numbers, special


def assess_password(password, username, mfa):
    minimum = get_minimum_length(mfa)

    reject = []
    review = []

    if len(password) < minimum:
        reject.append("Password is too short.")

    if check_blocklist(password):
        reject.append("Password is on the blocklist.")

    if check_username(password, username):
        reject.append("Password contains the username.")

    if check_repeated_characters(password):
        review.append("Password has 4 or more repeated characters.")

    sequences = check_sequences(password)

    if len(sequences) > 0:
        review.append("Password contains an obvious sequence.")

    if len(reject) > 0:
        result = "REJECT"
    elif len(review) > 0:
        result = "REVIEW"
    else:
        result = "ACCEPT"

    return result, reject, review, minimum


def show_report(password, username, mfa):
    result, reject, review, minimum = assess_password(password, username, mfa)
    lowercase, uppercase, numbers, special = check_character_types(password)

    print()
    print("PASSWORD RISK ASSESSMENT")
    print("------------------------")
    print("Password length:", len(password))
    print("MFA enabled:", mfa)
    print("Minimum length:", minimum)
    print("Result:", result)

    print()
    print("Reasons:")

    if len(reject) == 0 and len(review) == 0:
        print("No problems found.")
    else:
        for reason in reject:
            print("-", reason)

        for reason in review:
            print("-", reason)

    print()
    print("Character types:")
    print("Lowercase:", lowercase)
    print("Uppercase:", uppercase)
    print("Numbers:", numbers)
    print("Special characters:", special)


def get_mfa():
    while True:
        answer = input("Is MFA enabled? (yes/no): ").lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Please enter yes or no.")


def main():
    print("Password and Passphrase Risk Assessment Engine")
    print()

    password = input("Enter a password/passphrase: ")
    username = input("Enter username: ")
    mfa = get_mfa()

    show_report(password, username, mfa)


main()
