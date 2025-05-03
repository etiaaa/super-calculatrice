from calculate.view import View

def test_get_user_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    assert View.get_user_input("entrez") == "test"

def test_print_result(capsys):
    View.print_result("2+2", 4)
    captured = capsys.readouterr()
    assert "RESULTAT" in captured.out