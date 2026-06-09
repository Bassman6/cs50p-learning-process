from vanity_plate import is_valid

# def test_is_valid():
#     assert is_valid("cs50")
#     assert is_valid("cs50p")
#     assert is_valid("cs05")
#     assert is_valid("PI3.14")
#     assert is_valid("outatime")
#     assert is_valid("h")



def test_starts_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("CS") == True
    assert is_valid("AAAAAAA") == False

def test_number_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False # Number in the middle

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False # Zero cannot be the first number

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False