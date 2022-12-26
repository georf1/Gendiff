import pytest
from gendiff.generate_diff_engine import generate_diff


@pytest.mark.parametrize("file1,file2,extension,expected", [
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml', 'stylish', 'tests/fixtures/diff1.txt'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish', 'tests/fixtures/diff2.txt'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml', 'plain', 'tests/fixtures/diff3.txt'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain', 'tests/fixtures/diff4.txt'),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json', 'tests/fixtures/diff5.txt')])
def test_stylish(file1, file2, extension, expected):
    assert generate_diff(file1, file2, extension) == open(expected).read()
