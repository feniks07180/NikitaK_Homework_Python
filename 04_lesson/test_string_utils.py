import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

class TestStringUtils:

    class TestCapitalize:
        def test_capitalize_positive(self, string_utils):
            assert string_utils.capitalize("skypro") == "Skypro"
            assert string_utils.capitalize("Skypro") == "Skypro"
            assert string_utils.capitalize("123") == "123"

        def test_capitalize_negative(self, string_utils):
            assert string_utils.capitalize("") == ""

    class TestTrim:
        def test_trim_positive(self, string_utils):
            assert string_utils.trim("   skypro") == "skypro"
            assert string_utils.trim("skypro   ") == "skypro   "
            assert string_utils.trim("  skypro  ") == "skypro  "
            assert string_utils.trim("skypro") == "skypro"

        def test_trim_negative(self, string_utils):
            assert string_utils.trim("") == ""
            assert string_utils.trim("   ") == ""

    class TestContains:
        def test_contains_positive(self, string_utils):
            assert string_utils.contains("SkyPro", "S") == True
            assert string_utils.contains("SkyPro", "k") == True
            assert string_utils.contains("abc", "") == True

        def test_contains_negative(self, string_utils):
            assert string_utils.contains("SkyPro", "U") == False
            assert string_utils.contains("", "a") == False

    class TestDeleteSymbol:
        def test_delete_symbol_positive(self, string_utils):
            assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
            assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
            assert string_utils.delete_symbol("aaaa", "a") == ""
            assert string_utils.delete_symbol("abc", "") == "abc"

        def test_delete_symbol_negative(self, string_utils):
            assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
            assert string_utils.delete_symbol("", "a") == ""