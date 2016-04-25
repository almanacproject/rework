import argparse
import json
import rework
import sys


REGEX = r"""
\$\$\{              # Start of the pattern
(?P<id>             # identifier of match
    (?:             # ignore the group with the "."
        (?:[^\.}]+) # find a string that does not contain a "."
        \.          # match a seperation "."
    )*              # match 0 to n strings seperatred by "." e.g. "abc.def.ghi."
    (?:[^\.}]*)     # match a final string with out a "."
)
\}
"""


def parse_args():
    """ Prarse the arguments """
    parser = argparse.ArgumentParser(description='Rework a simple template engine')
    parser.add_argument('template',
                        type=argparse.FileType('r'),
                        help='template file ')
    return parser.parse_args()


def main():
    """ Main function """
    args = parse_args()

    dictionary = json.load(sys.stdin)

    t = rework.Template(REGEX, dictionary)

    for line in args.template:
        for string in t.replace_template(line):
            print(string, end='')

main()
