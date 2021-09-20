import sys
sys.path.insert(0, "../code")
from code.keyword_recognition import start

if __name__ == '__main__':
    for i in range(10000):
        start(filepath='../data/key.c', level=4)

