# Main

from scan import scan
from parse import parse
from errors import GrammaticalError
from ast import printAST

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        f = open(filename)
    else:
        f = sys.stdin

    while True:
        line = f.readline()
        if line == '': break
        if line == '\n': continue

        print ">", line,
        try:
            ast = parse(scan(line))
            printAST(ast)
        except GrammaticalError as e:
            print "Error:", e

    if f != sys.stdin:
        f.close()

    print 'ok'