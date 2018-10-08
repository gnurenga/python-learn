from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.completion import WordCompleter
from pygments.lexers import PythonLexer
from prompt_toolkit.styles import Style
import os

pykeyword_completer = WordCompleter([
    'ls', 'man', 'cd', 'mkdir', 'cp',
    'touch', 'ifconfig', 'touch', 'clear',
    'firefox', 'gedit', 'git'], ignore_case = True) 

style = Style.from_dict({
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000',
        'scrollbar.background': 'bg:#ffffff',
        'scrollbar.button': 'bg:#00FF00',
    })


def main():
    session = PromptSession(lexer=PygmentsLexer(PythonLexer),
                            completer = pykeyword_completer,
                            style = style)

    while True:
        try:
            text = session.prompt("PySh~~> ")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            os.system(text)


    print ":: Good Bye, PySh ::"

if __name__ == '__main__':
    main()
