import dictionary_flattener as dif

sample_dict1 = {
  'test': 1,
  'stuff': {
    'a': 1,
    'b': 2
  },
  'nums': [4,5,6,[7,8]]
}


def test_flatten_dict():
    dif.flatten_dict(sample_dict1) == {
        'test': 1,
        'stuff.a': 1,
        'stuff.b': 2,
        'nums.0': 4,
        'nums.1': 5,
        'nums.2': 6,
        'nums.3.0': 7,
        'nums.3.1': 8
    }
