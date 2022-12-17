from gendiff.scripts.gendiff import generate_diff


correct_diff_stylish1 = open('tests/fixtures/diff1.txt').read()
correct_diff_stylish2 = open('tests/fixtures/diff2.txt').read()

correct_diff_plain1 = open('tests/fixtures/diff3.txt').read()
correct_diff_plain2 = open('tests/fixtures/diff4.txt').read()


def test1():
    diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
    assert diff == correct_diff_stylish1

def test2():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == correct_diff_stylish2

def test3():
    diff = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml', 'plain')
    assert diff == correct_diff_plain1

def test4():
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain')
    assert diff == correct_diff_plain2
