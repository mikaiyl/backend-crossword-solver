#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

import re

__author__ = "???"

# YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        '''Please enter a word to solve.\n
        Use spaces to signify unknown letters: ''').lower()

    # YOUR ADDITIONAL CODE HERE
    word_re = re.compile(test_word.replace(' ', '.'))
    match_array = filter(lambda w: len(test_word) == len(w) and
                         word_re.match(w), words)
    print('\n'.join(match_array))


if __name__ == '__main__':
    main()
