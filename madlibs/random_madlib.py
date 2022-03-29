from sample_madlibs import one, two, three
import random

if __name__ == "__main__":
    m = random.choice([one, two, three])
    m.madlib()