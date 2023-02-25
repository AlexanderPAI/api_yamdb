from random import randint


FROM_EMAIL = 'info@olo.com'


def code_generator():
    """Генератор кода подтверждения."""
    code = randint(0000, 9999)
    return code
