class Term:
    def __init__(self, name: str, type: str, value=None):
        self.name = name
        self.type = type
        self.value = None
        
        if type == "const":
            if value: 
                self.value = value
            else:
                self.value = name
    
    def __repr__(self):
        return "{:}:{:}".format(self.name, self.type)
    
    def copy(self):
        return Term(self.name, self.type, self.value)


class Atom:
    def __init__(self, name: str, args: list[Term], isPositive=True):
        self.name = name
        self.args = args
        self.isPositive = isPositive

    def __repr__(self):
        return "{:}{:}({:})".format(
            '~' if not self.isPositive else '', 
            self.name, 
            ", ".join(["{:}".format(term) for term in self.args])
        )

    def copy(self):
        return Atom(
            name=self.name, 
            args=[arg.copy() for arg in self.args], 
            isPositive=self.isPositive
        )


class Disjunct:
    def __init__(self, args: list[Atom]):
        self.args = args

    def __repr__(self):
        if len(self.args) == 0:
            return "Пусто"

        return " | ".join(["{:}".format(atom) for atom in self.args])

    def copy(self):
        return Disjunct([arg.copy() for arg in self.args])
