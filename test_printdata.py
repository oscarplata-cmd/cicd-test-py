import pytest
from printdata import print_data as pd

def test_pd():
  assert pd(123) == "123"