# import unittest
# import pytest
import importlib.metadata
from subprocess import run

def test_version():
    out = run(['argdown', '--version'], capture_output=True, text=True)
    assert out.stdout.strip() == 'argdown ' + importlib.metadata.version('argdown')

def test_dummy():
    out = run(['argdown', 'tests/dummy.py'], capture_output=True, text=True)
    with open('tests/dummy.md') as f:
        assert out.stdout.strip() == f.read().strip()