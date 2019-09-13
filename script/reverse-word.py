#!/usr/bin/env python3


def rev_word(s):
    s = "Your list of words to reverse here"
    words = s.split(',')
    string = []
    for word in words:
        string.insert(0, word)
    print(",".join(string))

if __name__ == "__main__":
    rev_word("test it")
