#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """Test for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """Test that access_nested_map output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found under 'a'")
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            expected_message: str,
            ) -> None:
        """Tests `access_nested_map` raises correct message."""
        with self.assertRaises(Exception) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Json function test"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests get_json output."""
        attribute = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attribute)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize class."""
    def test_memoize(self) -> None:
        """Test memoize output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
