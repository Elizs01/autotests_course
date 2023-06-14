import pytest
from datetime import datetime
import time
@pytest.fixture()
def time_start_end():
    print("\nНачало выполнения теста " + str(datetime.now().time()))
    yield
    print("\nОкончание выполнения теста " + str(datetime.now().time()))

@pytest.fixture()
def time_work():
    start = time.time()
    yield
    end = time.time()
    print(f"\nВремя выполнение теста {end-start}")