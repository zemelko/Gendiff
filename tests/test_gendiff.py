from gendiff.scripts.gendiff import generate_diff
import pytest


@pytest.fixture
def file1_json_flat():
    return 'tests/fixtures/file1_flat.json'


@pytest.fixture
def file2_json_flat():
    return 'tests/fixtures/file2_flat.json'


@pytest.fixture
def file1_yaml_flat():
    return 'tests/fixtures/file1_flat.yaml'


@pytest.fixture
def file2_yaml_flat():
    return 'tests/fixtures/file2_flat.yaml'


@pytest.fixture
def flatten_expected():
    with open('tests/fixtures/expected/Flatten.txt') as f:
        return f.read()


def test_json_flatten(file1_json_flat, file2_json_flat, flatten_expected):
    assert flatten_expected == generate_diff(file1_json_flat, file2_json_flat)


def test_yaml_flatten(file1_yaml_flat, file2_yaml_flat, flatten_expected):
    assert flatten_expected == generate_diff(file1_yaml_flat, file2_yaml_flat)