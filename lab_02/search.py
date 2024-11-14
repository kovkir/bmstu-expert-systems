from items import Rule, Node, Label


class Search:
    """
    Метод поиска в ширину от данных к цели 
    """
    def __init__(self, rule_arr: list[Rule]):
        self.rule_arr = rule_arr  # база знаний
        self.open_rule_lst = []
        self.close_node_lst = []
        self.close_rule_lst = []

        self.goal_node = None
        self.solution_flag = False
        self.no_solution_flag = False

    def run(self, goal_node: Node, in_node_arr: list[Node]):
        self.goal_node = goal_node
        self.close_node_lst = in_node_arr

        while not self.solution_flag and not self.no_solution_flag:
            rule_cnt = self.parent_search()

            if self.solution_flag:
                return
            
            if rule_cnt == 0:
                self.no_solution_flag = True
                print("\nРешение не было найдено ❌\n")

    def parent_search(self):
        count_rules = 0

        for rule in self.rule_arr:
            if not self.solution_flag:
                print(f'\nТекущее правило: {rule.number}')
                
                if rule.label != Label.OPEN:
                    print(f'Правило уже было доказано\n\n{'—' * 64}')
                    continue

                if self.is_close_nodes_cover(rule.node_arr):
                    print('Все входные вершины правила являются закрытими')

                    rule.label = Label.CLOSE
                    self.close_rule_lst.append(rule)
                    self.close_node_lst.append(rule.out_node)
                    self.set_nodes_closed(rule.node_arr)

                    if rule.out_node == self.goal_node:
                        self.solution_flag = True
                        print('Выходная вершина правила является целевой ✅')

                    count_rules += 1
                else:
                    print('Не все входные вершины правила являются закрытими')
            else:
                print(f'\nРешение было найдено ✅\n\n{'—' * 64}')
                break

            print('Список доказанных правил: ', end='')
            self.print_rules(self.close_rule_lst)
            print(f'Список закрытых вершин: ', end='')
            self.print_nodes(self.close_node_lst)
            print('\n' + '—' * 64)

        print(f'\t\tКол-во доказанных правил при обходе: {count_rules}\n{'—' * 64}')
        return count_rules

    def is_close_nodes_cover(self, in_node_arr: list[Node]):
        for node in in_node_arr:
            if node not in self.close_node_lst:
                return False
        return True

    def set_nodes_closed(self, node_arr):
        for node in node_arr:
            node.flag = Label.CLOSE

    def print_rules(self, rule_arr: list[Rule]):
        for rule in rule_arr:
            print(rule.number, end=' ')
        print()

    def print_nodes(self, node_arr: list[Node]):
        for node in node_arr:
            print(node, end=' ')
        print()
