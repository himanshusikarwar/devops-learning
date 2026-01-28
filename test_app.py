from app import main
import os

def test_output():
    os.environ["APP_NAME"] = "Hello"
    assert main() == "Hello"
