class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


valid_domains = ['com', 'bg', 'net', 'org']


while True:
    email = input()
    if email == 'End':
        break
    try:
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @')
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError('Email should contain only one @')
        if len(email.split('@')[0]) <= 4:
            raise NameTooShortError('Name nust be more than 4 characters')
        if email.split('.')[-1] not in valid_domains:
            raise InvalidDomainError('Domain must be one of the folowing: .com, .bg, .org, .net')

    except IndexError:
        print("Invalid email")

    else:
        print('Email is valid')
