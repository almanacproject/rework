import argparse
import json
import rework
import sys
import yaml

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
    parser.add_argument('config',
                        type=argparse.FileType('r'),
                        help='rework configuration file ')
    return parser.parse_args()


def rework_file(src_str, dest_str, engine):
    with open(src_str) as src, open(dest_str, 'w') as dest:
        for line in src:
            for string, bool in engine.replace_template(line):
                if bool:
                    print(string, end='', file=dest)
                else:
                    print(string, end='', file=dest)
                    print('There was no value for {} in the dictionary.'.format(string), file=sys.stderr)


def main():
    """ Main function """
    args = parse_args()

    dictionary = json.load(sys.stdin)
    config = yaml.load(args.config)["rework"]

    e = rework.Engine(REGEX, dictionary)

    for line in config["templates"]:
        src, dest = line
        rework_file(src, dest, e)


if __name__ == "__main__":
    main()
