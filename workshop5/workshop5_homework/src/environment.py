class Environment:
    def __init__(self):
        self.values = {}

    def define(self, name: str, value):
        self.values[name] = value
        return value

    def get(self, name: str):
        if name in self.values:
            return self.values[name]
        raise NameError(f"Variable {name!r} is not defined")

    def assign(self, name: str, value):
        if name in self.values:
            self.values[name] = value
            return value
        raise NameError(f"Variable {name!r} is not defined")

    def __repr__(self) -> str:
        return f"Environment({self.values})"
