"""A module to say hi in several langages."""

base = {
    'en':'Hi {}!', 
    'fr':'Salut {}!', 
    'cn':'你好 {}!'
}

def say_hi(name, lang='en'):
    """Say hi in the language of your choice."""
    if lang not in base:
        print('Language unknown: {}'.format(lang))
    print(base[lang].format(name))
    
def add_lang(key, phrase):
    """Add a language to the list."""
    global base
    if key in base:
        print('Language {} already available'.format(key))
        return
    base[key] = phrase

if __name__ == '__main__':
    # execute only if run as a script
    import sys
    nargs = len(sys.argv)
    if nargs == 3:
        say_hi(sys.argv[1], lang=sys.argv[2])
    else:
        print('Syntax:')
        print('%run greetings.py name language')
        print('Languages available: {}'.format(list(base)))
