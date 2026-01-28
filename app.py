import os

def main():
    name = os.getenv("APP_NAME", "Hello")
    return name
