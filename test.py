class Test:
    def __init__(self, name):
        self.name = name

    def hello(self, name):
        print(f"hello {name}")


ob = Test("a7a")

getattr(ob, "hello")("aziz")
