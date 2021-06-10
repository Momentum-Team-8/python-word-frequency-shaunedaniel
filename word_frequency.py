
import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
# open file - read file and lowercase the data in the file - split off the data - sort data in ABC order
# remove the punctuations - remove stop words - count words - display on terminal.


def print_word_freq(file):

    file = open(file)
    text = file.read().lower()
    words = text.split()
    output = sorted(
        [word.strip(string.punctuation) for word in words])
    print(output)


print(print_word_freq)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
