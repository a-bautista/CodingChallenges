def solve(letters):
    stack = []
    indexes_to_remove = set()
    string_builder = []

    # first part for providing the letters
    for i, value in enumerate(letters):
        if value not in '()':
            continue

        if value == '(':
            stack.append(i)

        elif not stack:
            indexes_to_remove.add(i)

        else:
            stack.pop()

    # join all the indexes that were left behind in the stack into the indexes to remove
    indexes_to_remove = indexes_to_remove.union(set(stack))

    # string builder to join only the values that do not appear in the indexes to remove
    for i, value in enumerate(letters):
        if i not in indexes_to_remove:
            string_builder.append(value)
    return "".join(string_builder)