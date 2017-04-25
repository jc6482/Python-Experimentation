#Juan Carlos Ramirez
#Generate a Markov Chain from a body of text
import argparse, random

parser = argparse.ArgumentParser(description="Generate a Markov Chain from a body of text")
parser.add_argument("-fileName", default="",  help="Body of text we will generate from")
parser.add_argument("-genSize", type=int, default=25,  help="Size of Body of text we will generate from")
args = parser.parse_args()


class MarkovGenerator(object):
    def __init__(self,open_file):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words


    def trips(self):
        """Generates trips for string, EX: "What a Lovely MOO" -> (What, a, lovely) -> (a,lovely,moo)"""
        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield(self.words[i],self.words[i+1],self.words[i+2])

    def database(self):
        for w1,w2,w3 in self.trips():
            key = (w1,w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self,size=25):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed],self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1,w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)


if args.fileName == "":
    print "Usage: python markovChain.py -fileName [fileName]"
    exit()

file_ = open(args.fileName)


markov = MarkovGenerator(file_)
print markov.generate_markov_text(args.genSize)
