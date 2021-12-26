import pytest
from django.test import TestCase

from theapp.tools import a


class TestRootView(TestCase):
    def test_5(self):
        assert a() == 5