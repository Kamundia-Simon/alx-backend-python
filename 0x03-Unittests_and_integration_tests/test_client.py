#!/usr/bin/env python3
"""
method to  test that GithubOrgClient.org returns the correct value.
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, res: Dict, mocked_fxn: MagicMock) -> None:
        """Tests org method."""
        mocked_fxn.return_value = MagicMock(return_value=res)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), res)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
