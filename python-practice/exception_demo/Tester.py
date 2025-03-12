class BaseNameError(ValueError):
    pass


class ShortNameError(BaseNameError):
    pass


class LongNameError(BaseNameError):
    pass


class InvalidNameError(BaseNameError):
    pass


def validate(name):
    if (len(name) < 4) or (len(name) > 16):
        raise ShortNameError('Name should be between 4 to 15 character')
    if not name.isalpha():
        raise InvalidNameError('Username can only contain alpha characters')


validate('2232323')
