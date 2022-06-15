from main import count_char, check_if_maj, check_if_special, check_if_valid_password


def test_count_char():
    input = "Bonjour"
    input2 = "LongPassword"
    expected = 7
    expected2 = 12
    result = count_char(input)
    result2 = count_char(input2)
    assert expected == result
    assert expected2 == result2


def test_check_if_maj():
    input = "Bonjour"
    input2 = "bonjour"
    expected = True
    expected2 = False
    result = check_if_maj(input)
    result2 = check_if_maj(input2)
    assert expected == result
    assert expected2 == result


def test_check_if_special():
    input = "Bonjour*"
    input2 = "Bonjour"
    expected = True
    expected2 = False
    result = check_if_special(input)
    result2 = check_if_special(input2)
    assert expected == result
    assert expected2 == result2


def test_check_if_valid_password():
    input = "Strong*Password"
    input2 = "NoSpecialCharactere"
    input3 = "no_upper-charactere"
    input4 = "Shrtpwd!"
    expected = True
    expected2 = False
    expected3 = False
    expected4 = False
    result = check_if_valid_password(input)
    result2 = check_if_valid_password(input2)
    result3 = check_if_valid_password(input3)
    result4 = check_if_valid_password(input4)
    assert expected == result
    assert expected2 == result2
    assert expected3 == result3
    assert expected4 == result4
