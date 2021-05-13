from application import balance

def main(strings):
    for string in strings:
        print(f"cбалансированно: {string}") if balance.check(string) else print(f"неcбалансированно: {string}")


if __name__ == '__main__':
    brackets = [
        '((([{}])))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]',
        '({)}',
        '[][][])([]'
    ]

    main(brackets)
