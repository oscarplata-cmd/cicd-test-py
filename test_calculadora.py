import pytest
from calculadora import Calculadora

def test_suma_positiva():
  cal = Calculadora()
  assert cal.sum(1,2) == 3
  
def test_fallo_sum():
  cal = Calculadora()
  assert cal.sum(1,2) != 4