import sys
import unicodedata

DELIM = '\t'

lettermap = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 8,
    'g': 3,
    'h': 5,
    'i': 1,
    'j': 1,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 7,
    'p': 8,
    'q': 1,
    'r': 2,
    's': 3,
    't': 4,
    'u': 6,
    'v': 6,
    'w': 6,
    'x': 5,
    'y': 1,
    'z': 7,
    'æ': 6,
    'ø': 7,
    'å': 1
}

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s > 9:
        return sum_digits(s)
    else:
        return s

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def beregn(name):
    name = strip_accents(name.lower())
    sum = 0
    for letter in name:
        if letter in lettermap:
            sum += lettermap[letter]
    return (sum, sum_digits(sum))


if __name__=='__main__':
    if len(sys.argv) < 2:
        print('usage: python3 noegle.py FIL FIL FIL')
    for fname in sys.argv[1:]:
        with open(fname) as fin:
            for line in fin.readlines():
                name = line.strip()
                noegle = beregn(name)
                #elems = [name, str(noegle[0]), str(noegle[1])]
                elems = [name, str(noegle[0])]
                output = DELIM.join(elems)
                print(output)
