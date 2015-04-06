from tests.tests_ import tests
import main

def cov():
    tests()
    main.main()

if __name__ == '__main__':
    cov()