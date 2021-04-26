def test_ok():
    assert 0 == 0 # Test is ok


def test_failed():
    #assert 1 == 0 # Test failed REMOVE THIS PART AND USE assert not
    assert not 1 == 0



def test_different_exit_code():
    open('/nonexistent', 'r')
