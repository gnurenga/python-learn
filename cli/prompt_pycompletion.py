from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.completion import WordCompleter
from pygments.lexers import PythonLexer

pykeyword_completer = WordCompleter([
    'and', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else',
    'except', 'exec', 'finally', 'for', 'from',
    'global', 'if', 'import', 'in', 'is', 'lambda',
    'not', 'or', 'pass', 'print', 'raise',
    'return', 'try', 'while', 'with', 'yield'], ignore_case = True) 


def main():
    session = PromptSession(lexer=PygmentsLexer(PythonLexer), completer=pykeyword_completer)

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
