"""A module to say hi in several langages."""

base = {
    'en': 'Hi {}!',
    'fr': 'Salut {}!',
    'cn': '你好 {}!',
}

current_language = 'en'


def say_hi(name):
    """Say hi in the current language."""
    print(base[current_language].format(name))


def set_current_language(lang):
    """Set language currently spoken by the module."""
    global current_language
    if lang not in base:
        print('Language unknown: {}'.format(lang))
    current_language = lang


if __name__ == '__main__':
    # execute only if run as a script
    import sys
    nargs = len(sys.argv)
    if nargs == 3:
        set_current_language(sys.argv[2])
        say_hi(sys.argv[1])
    else:
        print('Syntax:')
        print('%run greetings.py name language')
        print('Languages available: {}'.format(list(base)))
