class Grammar:
    def __init__(self, rules):
        self.rules = rules

    def parse(self, symbol, string, visited=None):
        if visited is None:
            visited = set()

        state = (symbol, string)
        if state in visited:
            return None  # Запобігаємо зацикленню

        visited.add(state)

        if not string:
            return [] if symbol == "" else None

        if symbol not in self.rules:
            if string.startswith(symbol):
                return [(symbol, string[len(symbol):])]
            else:
                return None

        results = []
        for production in self.rules[symbol]:
            remainder = string
            subtree = []

            for term in production:
                parse_result = self.parse(term, remainder, visited)
                if parse_result is None:
                    break
                subtree.append((term, remainder[:len(remainder) - len(parse_result[0][1])]))
                remainder = parse_result[0][1]

            if subtree and remainder != string:
                results.append((subtree, remainder))

        return results if results else None


def build_tree(parse_result, symbol):
    if not parse_result:
        return None

    tree = {"symbol": symbol, "children": []}
    for production in parse_result[0][0]:
        if isinstance(production, tuple):
            term, _ = production
            subtree = build_tree([(term, "")], term)
            if subtree:
                tree["children"].append(subtree)
        elif isinstance(production, str):
            tree["children"].append({"symbol": production, "children": []})

    return tree


def display_tree(tree, indent=0):
    if tree:
        print(" " * indent + tree["symbol"])
        for child in tree["children"]:
            display_tree(child, indent + 2)


# Граматика у формі Бекуса-Наура
rules = {
    "<E>": [["(", "<E>", ")"], ["<E>", "+", "<E>"], ["<E>", "*", "<E>"], ["<V>"], ["<C>"]],
    "<V>": [["x"], ["y"]],
    "<C>": [["1"], ["2"]]
}

# Введений ланцюжок
string = "x+(y+y)*y"

grammar = Grammar(rules)
parse_result = grammar.parse("<E>", string)

if parse_result:
    print("Результат парсингу:", parse_result)  # Додано для перевірки
    tree = build_tree(parse_result, "<E>")
    print("Дерево виведення:")
    display_tree(tree)
else:
    print("Ланцюжок неможливо вивести.")

