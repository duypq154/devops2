from click.testing import CliRunner
from hello import hello, toyou, add, subtract

def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Thor",
        "--color", "blue"])
    assert "Thor" in result.output

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9