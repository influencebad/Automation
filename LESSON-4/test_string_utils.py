import pytest
from string_utils import StringUtils


stringutils = StringUtils()


@pytest.mark.parametrize("string, result", [("mary", "Mary"), ("алёша", "Алёша"), ("", ""), ("0987654321", "0987654321"), ("КАТЯ", "КАТЯ")])
def test_capitilize(string, result):
    result = stringutils.capitilize(string)
    assert result == result


@pytest.mark.parametrize("string, result", [(" Mary", "Mary"), ("  Mary", "Mary"), ("          Катя", "Катя"), ("", ""), ("123", "123")])
def test_trim(string, result):
    result = stringutils.trim(string)
    assert result == result


@pytest.mark.parametrize("string, delimeter, result", [
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("m_a_r_y", "_", ["m", "a", "r", "y"]),
    ("Первый; Второй; Третий", ";", ["Первый", "Второй", "Третий"]),
    ("@!@!@!@!@", "!", ["@", "@", "@", "@", "@"]),
    ("Груши + яблоки + виноград", "+", ["Груши", "яблоки", "виноград"]),
    ("", "", []), ("1;2;3;4", "-", "1;2;3;4")])
def test_to_list(string, delimeter, result):
    result = stringutils.to_list(string, delimeter)
    assert result == result


@pytest.mark.parametrize("string, symbol, result", [
    ("12345", "1", True), ("Устала", "а", True), ("Bang", "B", True),
    ("Too_much", "_", True), ("!@#$%^&", "6", False), ("09876", "5", False), ("Maша", "S", False), ("", "", "")])
def test_contains_true_positive(string, symbol, result):
    result = stringutils.contains(string, symbol)
    assert result == result


@pytest.mark.parametrize("string, symbol, result", [
    ("09876", "76", "098"), ("Maша", "ша", "Ма"), ("!@#$%^&", "$%", "!@#^&"),
    ("Delete", "e", "Dlt"), ("", "", None), ("12345", "CP", "12345"), ("Когда", "", "Когда")])
def test_delete_symbol(string, symbol, result):
    result = stringutils.delete_symbol(string, symbol)
    assert result == result
    

@pytest.mark.parametrize("string, symbol, result", [
    ("Катерина", "К", True), ("1234567890", "1", True), ("!@#$%", "!", True),
    ("Bool", "B", True), ("Car", "c", False), ("", "", None), ("1234", "5", False)])
def test_starts_with(string, symbol, result):
    result = stringutils.starts_with(string, symbol)
    assert result == result


@pytest.mark.parametrize("string, symbol, result", [("Катерина", "а", True), ("1234567890", "0", True), ("!@#$%", "%", True),
    ("Bool", "l", True), ("Car", "a", False), ("", "", None), ("1234", "1", False)])
def test_end_with(string, symbol, result):
    result = stringutils.end_with(string, symbol)
    assert result == result


@pytest.mark.parametrize("string, result", [
    ("", True), (" ", True), ("       ", True),
    (",", False), ("1225", False), ("Мама", False), ("SON", False)])
def test_is_empty(string, result):
    result = stringutils.is_empty(string)
    assert result == result


@pytest.mark.parametrize("lst, joiner, result", [
    ([1, 2, 3, 4], "", "1, 2, 3 4"), (["Мама", "Папа", "Дочь", "Сын"], "+", "Мама+Папа+Дочь+Сын"), ([],"","")])
def test_list_to_string(lst, joiner, result):
    result = stringutils.list_to_string(lst, joiner)
    assert result == result
