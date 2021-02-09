"""Word Finder: finds random words from a dictionary."""
from random import randint


class WordFinder:
    """ Word Finder: finds random words from a dictionary.

    WordFinder expects a text file with the path included.
    The text file has one word on each line. WordFinder reads
    the text file, builds a word list, and returns the number
    of words read, "xx words read"

    WordFinder does not test words for uniqueness, so gigo!

    .random() method returns a random word from the word list

    .how_many_words() method returns the number of words read.

    >>> wf_tests = WordFinder("./data/doctest_wf.txt")
    5 words read

    >>> wf_tests
    <WordFinder file_with_path='./data/doctest_wf.txt' nbr_of_words=5>

    >>> wf_tests.random()
    'supercalifragilisticexpialidocious'

    >>> wf_tests.random()
    'supercalifragilisticexpialidocious'

    """

    def __init__(self, filename_with_path):
        self.words = []
        self.filename_with_path = filename_with_path
        self.nbr_of_words = 0

        # need to read file and count words
        self.read_word_file(filename_with_path)

    def __repr__(self):
        return f"<WordFinder file_with_path='{self.filename_with_path}' nbr_of_words={self.nbr_of_words}>"

    def read_word_file(self, filename_with_path):

        try:
            file_in = open(filename_with_path, 'r', closefd=True)
        except FileNotFoundError:
            print(f"The file '{filename_with_path}' was not found.")
            return

        word_ctr = 0
        for file_data in file_in:
            self.words.append(file_data.strip('\n').strip())
            word_ctr = word_ctr + 1

        self.nbr_of_words = word_ctr
        print(f"{word_ctr} words read")

        file_in.close()

    def random(self):
        return self.words[randint(0, (self.how_many_words() - 1))]

    def how_many_words(self):
        return self.nbr_of_words


class SpecialWordFinder(WordFinder):
    """
    SpecialWordFinder, a subclass of WordFinder, functions the same
    as WordFinder except blank lines and lines that start with a # are
    ignored.

    SpecialWordFinder expects a text file with the path included.
    The text file has one word on each line. SpecialWordFinder reads
    the text file, and adds the word to the word list unless the word
    begins with a #. Blank lines are ignored. Only words added to the
    word list are included in the word count, 'xx words read'

    SpecialWordFinder does not check words for uniqueness.

    .random() method returns a random word from the word list

    .how_many_words() method returns the number of words read.

    >>> swf_tests = SpecialWordFinder("./data/doctest_swf.txt")
    7 words read

    >>> swf_tests
    <SpecialWordFinder file_with_path='./data/doctest_swf.txt' nbr_of_words=7 nbr_of_words_ignored (began with #)=2 nbr_of_blank_lines=2>

    >>> swf_tests.random()
    'special'

    >>> swf_tests.random()
    'special'

    """

    def __init__(self, filename_with_path):

        self.nbr_of_words_ignored = 0
        self.nbr_of_blank_lines = 0

        super().__init__(filename_with_path)

    def __repr__(self):
        return (f"<SpecialWordFinder file_with_path='{self.filename_with_path}' " +
                f"nbr_of_words={self.nbr_of_words} " +
                f"nbr_of_words_ignored (began with #)={self.nbr_of_words_ignored} " +
                f"nbr_of_blank_lines={self.nbr_of_blank_lines}>")

    def read_word_file(self, filename_with_path):

        try:
            file_in = open(filename_with_path, 'r', closefd=True)
        except FileNotFoundError:
            print(f"The file '{filename_with_path}' was not found.")
            return

        ctr_word = 0
        ctr_ignored = 0
        ctr_blank_line = 0

        word_temp = None
        for file_data in file_in:
            word_temp = file_data.strip('\n').strip()
            # requirement stated not to return blank lines or comments. Best
            #  way to not return blank lines or comments is not to load blank
            #  lines or lines that begin with # into words.
            # NOTE: "   # Veggies" with any number of spaces before the # is
            #  treated the same as "# Veggies" -- they are both ignored!
            if (len(word_temp) > 0):
                if (word_temp[0] != "#"):
                    self.words.append(word_temp)
                    ctr_word = ctr_word + 1
                else:
                    ctr_ignored = ctr_ignored + 1
            else:
                ctr_blank_line = ctr_blank_line + 1

        self.nbr_of_words = ctr_word
        self.nbr_of_words_ignored = ctr_ignored
        self.nbr_of_blank_lines = ctr_blank_line

        print(f"{ctr_word} words read")

        file_in.close()
