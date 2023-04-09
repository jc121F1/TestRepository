import time
from core import main

def test_cool_stuff():
    assert 1 == 1

def test_main():
    time.sleep(1)
    main()
    assert 1 == 1
