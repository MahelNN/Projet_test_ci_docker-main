from main import count_char, check_if_maj, check_if_special, check_if_valid_password


def test_count_char():
    input = "Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result


def test_check_if_maj():
    input = "Bonjour"
    expected = True
    result = check_if_maj(input)
    assert expected == result


def test_check_if_special():
    input = "Bonjour*"
    expected = True
    result = check_if_special(input)
    assert expected == result


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
