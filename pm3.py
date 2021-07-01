

class Foo:
    def __init__(self, bar: str, baz: int):
        self.bar = bar
        self.baz = baz


def foo_match(foo: Foo):
    match foo:
        case Foo(bar="Hello", baz=_):
            print("Hello Foo!")
        case Foo(bar=_, baz=42):
            print("Foo 42!")
        case Foo(bar=_, baz=_):
            print("Foo Foo!")
        