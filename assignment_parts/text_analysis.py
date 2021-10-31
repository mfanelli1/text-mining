import random
import string
import sys
from unicodedata import category


def file_process(filename, skip_header):
    """this function makes a histogram that contains all the words from the file and returns the map from each word to the number of time the word appears"""
    hist = {}
    fp = open(filename, encoding = 'utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break
        
        line = line.replace(',', ' ')
        line = line.replace(chr(8212), ' ')
        line = line.replace('!', ' ')
        line = line.replace('-', ' ')

        for word in line.split():
            # this function removes punctuation and converts words to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header."""
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

def total_words(hist):
    """This function returns the total of the frequencies in the histogram"""
    return sum(hist.values())

def diff_words(hist):
    """this function returns the number of different words in the histogram"""
    return len(hist)

def ten_common(hist):
    """This function returns the top 10 most frequent words"""
    s = sorted(hist.items(), key=lambda item: item[1], reverse = True)[0:10]
    return s

def least_common(hist):
    """This function returns the 10 least frequent words"""
    s = sorted(hist.items(), key=lambda item: item[1], reverse = False)[0:10]
    return s

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


def main():
    hist = file_process('assignment_parts/alices_wonderland.txt', skip_header=True)
    print('\nTotal number of words:', total_words(hist))

    print('\nThere are', len(hist), 'different words in the book')

    print('\nThe top ten most commonly used words in this book are: ', ten_common(hist))

    print('\nThe ten least commonly used words in the book are:', least_common(hist))

    print("\n\nHere are some random words from the book:")
    for i in range(100):
        print(random_word(hist), end=' ')



if __name__ == '__main__':
        main()