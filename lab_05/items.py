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
    def __init__(self, name: str, args: list[Term], isPositive = True ):
        self.name = name
        self.args = args
        self.isPositive = isPositive

    def __repr__(self):
        return "{:}{:}({:})".format(
            '~' if not self.isPositive else '',
            self.name,
            ", ".join([
                "{:}".format(term) for term in self.args
            ])
        )
    
    def copy(self):
        return Atom(
            name=self.name, 
            args=[arg.copy() for arg in self.args],
            isPositive=self.isPositive
        )


class Conjunct:
    def __init__(self, args: list[Atom]):
        self.args = args

    def __repr__(self):
        if len(self.args) == 0:
            return "Пусто"

        return " & ".join([
            "{:}".format(atom) for atom in self.args
        ])
    
    def copy(self):
        return Conjunct(
            args=[arg.copy() for arg in self.args]
        )


class Implication:
    def __init__(self, left: Conjunct, right: Conjunct):
        self.left = left
        self.right = right

    def __repr__(self):
        return "{:} -> {:}".format(self.left, self.right)

    def copy(self):
        return Implication(
            left=self.left.copy(), 
            right=self.right.copy()
        )


class Knowleadge:
    def __init__(
        self, 
        data: Conjunct, 
        open_rules: list[Implication],
        close_rules: list[Implication] = [],
    ):
        self.data = data
        self.open_rules = open_rules
        self.close_rules = close_rules

    def __repr__(self):
        return "\n".join([
            "База фактов (закрытые вершины): ",
            *[f"  {fact}" for fact in self.data.args],
            "\nСписок открытых правил: ",
            *[f"  {rule}" for rule in self.open_rules],
            "\nСписок доказанных правил: ",
            *[f"  {rule}" for rule in self.close_rules],
        ])

    def copy(self):
        return Knowleadge(
            data=self.data.copy(),
            open_rules=[rule.copy() for rule in self.open_rules],
            close_rules=[rule.copy() for rule in self.close_rules],
        )
