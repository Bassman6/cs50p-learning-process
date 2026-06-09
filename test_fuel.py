from fuel import convert
from fuel import gauge
import pytest

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog") 
    with pytest.raises(ZeroDivisionError):    
      convert(1/0) 

def test_fuction():
    assert gauge(1/4) == "25%"
    assert gauge(1/2) == "50%"
    assert gauge(3/4) == "75%"
    assert gauge(1/1) == "F"
    assert gauge(0/1) ==  "E"
    
