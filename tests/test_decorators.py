from src.decorators import log

@log()
def my_function(x, y):
    return x + y

def test_log(capsys):
    my_function(1,2)
    captured = capsys.readouterr()

    assert captured.out == "Name func: my_function\nok\n"

    my_function(1, '2')
    captured = capsys.readouterr()

    assert captured.out == "Name func: my_function\nerror: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2') {}\n"