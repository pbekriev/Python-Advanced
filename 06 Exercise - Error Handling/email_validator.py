from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThenOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


min_name_length = 4
valid_domains = [".com", ".bg", ".net", ".org"]

pattern_name = r"[\w+\.]+"
pattern_domain = r"\.[a-z]+$"

email = input()

while email != "End":

    try:
        if email.count("@") > 1:
            raise MoreThenOneAtSymbolError("Email should contain only one @")

        if len(email.split("@")[0]) <= min_name_length:
            raise NameTooShortError(f"Name must be more than {min_name_length} characters")

        if findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name can only contain letters, numbers, underscores and dots.")

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        if findall(pattern_domain, email)[0] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

        print("Email is valid")

    except IndexError():
        print("Invalid email!")

    email = input()
