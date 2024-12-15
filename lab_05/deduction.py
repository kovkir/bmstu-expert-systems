from items import Atom, Conjunct, Implication, Knowleadge
from unification import unificate_atoms, apply_substitution, add_substitutions


class DirectDeduction():
    def __init__(self, knowleadge: Knowleadge) -> None:
        self.knowleadge = knowleadge.copy()

    def knowleadge_prove(self, goal: Atom) -> bool:
        facts = self.knowleadge.data
        open_rules = self.knowleadge.open_rules
        close_rules = self.knowleadge.close_rules
        
        if self.__is_proved(facts.args, goal):
            return True

        while True:
            close_rules_count = 0
            
            i = 0
            while i < len(open_rules):
                print(f"\nТекущее правило:\n  {open_rules[i]}")

                new_fact = self.__try_to_prove_rule(
                    facts=facts,
                    rule=open_rules[i],
                )
                if new_fact:
                    facts.args += new_fact.args            
                    close_rules.append(open_rules.pop(i))
                    close_rules_count += 1

                    if self.__is_proved(new_fact.args, goal):
                        return True
                else:
                    i += 1

            if close_rules_count == 0:
                break

        return False
    
    def __try_to_prove_rule(
        self, 
        facts: Conjunct, 
        rule: Implication,
    ) -> Conjunct | None:
        rule_result = rule.right.copy()
        rule_input_atoms = rule.left.copy()
        global_substitutions = {}
        
        while True:
            unificate_count = 0
            
            for rule_input_atom in rule_input_atoms.args:
                for fact_atom in facts.args:
                    if rule_input_atom.isPositive != fact_atom.isPositive:
                        continue

                    substitutions = unificate_atoms(
                        left=rule_input_atom, 
                        right=fact_atom,
                    )
                    if substitutions == None:
                        continue
                    
                    rule_input_atoms.args.remove(rule_input_atom)
                    
                    add_substitutions(
                        dest_substitions=global_substitutions,
                        sourse_substitions=substitutions,
                    )
                    apply_substitution(
                        atoms_list=rule_result.args + rule_input_atoms.args,
                        substitutions=substitutions, 
                    )
                    unificate_count += 1
                    break
            
            if unificate_count == 0:
                break
                
        if len(rule_input_atoms.args):
            print(
                f"\n{self.knowleadge}\n"\
                f"\n=> ❌\n"\
                f"\n{'-' * 64}"
            )
            return None
        
        print(
            f"\n{self.knowleadge}\n"\
            f"\n=> {rule_result} с подстановкой {global_substitutions}\n"\
            f"\n{'-' * 64}"
        )
        return rule_result
    
    def __is_proved(self, atoms: list[Atom], goal: Atom) -> bool:
        for atom in atoms:
            if atom.isPositive != goal.isPositive or \
                atom.name != goal.name or \
                not self.__equal_types(atom, goal):
                continue

            if unificate_atoms(atom, goal) != None:
                return True
            
        return False
    
    def __equal_types(self, left: Atom, right: Atom) -> bool:
        if len(left.args) != len(right.args):
            return False
        
        for i in range(len(left.args)):
            if left.args[i].type != right.args[i].type:
                return False
            
        return True
