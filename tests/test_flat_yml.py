from gendiff import generate_diff


def test_gendiff_flat_yaml():
    with open('tests/fixtures/flat_jaml.txt', 'r') as correct:
        assert correct.read() == generate_diff(
            'tests/fixtures/file_one.yml', 'tests/fixtures/file_two.yaml')