"""A module to say hi in several langages."""

base = {
    'en': 'Hi {}!',
    'fr': 'Salut {}!',
    'cn': '你好 {}!',
}


def say_hi(name, language='en'):
    """Say hi in the current language."""
    print(base[language].format(name))


if __name__ == '__main__':
    # execute only if run as a script
    import sys
    nargs = len(sys.argv)
    if nargs == 3:
        say_hi(sys.argv[1], language=sys.argv[2])
    else:
        print('Syntax:')
        print('%run greetings.py name language')
        print('Languages available: {}'.format(list(base)))
