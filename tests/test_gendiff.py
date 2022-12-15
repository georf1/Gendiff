from gendiff.scripts.gendiff import generate_diff


correct_diff1 = open('tests/fixtures/diff1.txt').read()
correct_diff2 = open('tests/fixtures/diff2.txt').read()

def test1():
    diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    assert diff == correct_diff1

def test2():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == correct_diff2