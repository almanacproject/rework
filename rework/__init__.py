import re
import itertools


def grouper(n, iterable, fillvalue=''):
    "s -> (s0,s1,...sn-1), (sn,sn+1,...s2n-1), (s2n,s2n+1,...s3n-1), ..."
    return itertools.zip_longest(*[iter(iterable)]*n, fillvalue=fillvalue)


class Template(object):

    """Docstring for Template. """

    def __init__(self, regex, dictionary):
        self._pattern = re.compile(regex, re.VERBOSE)
        self._dictionary = dictionary
        self._dictionary[''] = ''

    def replace_template(self, temp_str):
        sub_strings = self._pattern.split(temp_str)
        for s, replace in grouper(2, sub_strings):
            yield s
            yield self._dictionary[replace]