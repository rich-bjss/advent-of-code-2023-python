import utils

def test_overlaps_work():
    assert utils.get_matches("fzrpfhbfvj6dbxbtfs7twofksfbshrzkdeightwoqg") == ['6', '7', 'two', 'eight', 'two']