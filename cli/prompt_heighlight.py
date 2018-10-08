from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers import PythonLexer


def main():
    session = PromptSession(lexer=PygmentsLexer(PythonLexer))

    while True:
        try:
            text = session.prompt("~~> ")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print "You Entered:", text


    print "Good Bye ::"

if __name__ == '__main__':
    main()
