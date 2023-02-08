from idlelib.multicall import r
from re import findall


class NameTooShortError(Exception):
    pass


class MustHaveASymbol(Exception):
    pass


class InvalidDomain(Exception):
    pass


class MoreThatOneSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r"[\w+\.]+"
pattern_domain = r"\.[a-z]+"
valid_domain = [".com", ".bg", ".net", ".org"]
email = input()


min_length = 4
while email != "End":
    try:
        if email.count("@") > 1:
            raise MoreThatOneSymbolError("Email must contain only one @")
        if "@" not in email:
            raise MustHaveASymbol("Email must contain @")
        if len(email.split("@")[0]) <= min_length:
            raise NameTooShortError("Name must be more than 4 characters")
        if findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name must contain numbers and letters")
        if findall(pattern_domain, email)[-1] not in valid_domain:
            raise InvalidDomain(f"Domain must contain one of {', '.join(valid_domain)}")

    except IndexError:
        print("Invalid Email")
    else:
        print("Email is valid")

    email = input()
