from gendiff.engine.generate_diff import generate_diff
import pytest


@pytest.fixture
def file1_json_flat():
    return 'tests/fixtures/json/file1_flat.json'


@pytest.fixture
def file2_json_flat():
    return 'tests/fixtures/json/file2_flat.json'


@pytest.fixture
def file1_yaml_flat():
    return 'tests/fixtures/yaml/file1_flat.yaml'


@pytest.fixture
def file2_yaml_flat():
    return 'tests/fixtures/yaml/file2_flat.yaml'


@pytest.fixture
def file1_json_tree():
    return 'tests/fixtures/json/file1_tree.json'


@pytest.fixture
def file2_json_tree():
    return 'tests/fixtures/json/file2_tree.json'


@pytest.fixture
def file1_yaml_tree():
    return 'tests/fixtures/yaml/file1_tree.yaml'


@pytest.fixture
def file2_yaml_tree():
    return 'tests/fixtures/yaml/file2_tree.yaml'


@pytest.fixture
def flatten_stylish_expected():
    with open('tests/fixtures/expected/stylish/Flatten.txt') as f:
        return f.read()


@pytest.fixture
def tree_stylish_expected():
    with open('tests/fixtures/expected/stylish/Tree.txt') as f:
        return f.read()


@pytest.fixture
def tree_plain_expected():
    with open('tests/fixtures/expected/plain/Tree.txt') as f:
        return f.read()


@pytest.fixture
def to_json_expected():
    with open('tests/fixtures/expected/json/to_json.json') as f:
        return f.read()


# Stylish format
def test_stylish_json_flatten(file1_json_flat, file2_json_flat, flatten_stylish_expected):
    assert flatten_stylish_expected == generate_diff(file1_json_flat, file2_json_flat)


def test_stylish_yaml_flatten(file1_yaml_flat, file2_yaml_flat, flatten_stylish_expected):
    assert flatten_stylish_expected == generate_diff(file1_yaml_flat, file2_yaml_flat)


def test_stylish_json_tree(file1_json_tree, file2_json_tree, tree_stylish_expected):
    assert tree_stylish_expected == generate_diff(file1_json_tree, file2_json_tree)


def test_stylish_yaml_tree(file1_yaml_tree, file2_yaml_tree, tree_stylish_expected):
    assert tree_stylish_expected == generate_diff(file1_yaml_tree, file2_yaml_tree)


# Plain format
def test_plain_yaml_tree(file1_yaml_tree, file2_yaml_tree, tree_plain_expected):
    assert tree_plain_expected == generate_diff(file1_yaml_tree, file2_yaml_tree, format='plain')


# Json format
def test_dict_to_json(file1_json_tree, file2_json_tree, to_json_expected):
    assert to_json_expected == generate_diff(file1_json_tree, file2_json_tree, format='json')
