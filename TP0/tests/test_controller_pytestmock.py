from calculate.controller import Controller

def test_input_validation():
    c = Controller()
    assert c._is_input_valid("1")
    assert not c._is_input_valid("6")

def test_quit_logic():
    c = Controller()
    assert not c._is_quit("5")
    assert c._is_quit("1")