import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

class TestStringUtils:

    def test_capitalize(self, string_utils):
        assert string_utils.capitalize("skypro") == "Skypro"
        assert string_utils.capitalize("Skypro") == "Skypro"
        assert string_utils.capitalize("") == ""
        assert string_utils.capitalize("123") == "123"

    def test_trim(self, string_utils):
        assert string_utils.trim("   skypro") == "skypro"
        assert string_utils.trim("skypro   ") == "skypro   "
        assert string_utils.trim("  skypro  ") == "skypro  "
        assert string_utils.trim("skypro") == "skypro"
        assert string_utils.trim("") == ""
        assert string_utils.trim("   ") == ""

    def test_contains(self, string_utils):
        assert string_utils.contains("SkyPro", "S") == True
        assert string_utils.contains("SkyPro", "U") == False
        assert string_utils.contains("SkyPro", "k") == True
        assert string_utils.contains("", "a") == False
        assert string_utils.contains("abc", "") == True

    def test_delete_symbol(self, string_utils):
        assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
        assert string_utils.delete_symbol("aaaa", "a") == ""
        assert string_utils.delete_symbol("", "a") == ""
        assert string_utils.delete_symbol("abc", "") == "abc"
