from gendiff import generate_diff


def test_norm_gen_diff():
    with open('tests/fixtures/flat_json.txt', 'r') as correct:
        assert correct.read() == generate_diff('file1.json', 'file2.json')
