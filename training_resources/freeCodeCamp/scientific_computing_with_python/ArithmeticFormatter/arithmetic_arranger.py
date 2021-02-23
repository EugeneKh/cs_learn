from operator import add, sub


def arithmetic_arranger(prob, dec=False):
    # TESTing to limit the number of problems
    if len(prob) > 5:
        return 'Error: Too many problems.'
    prob_list = []
    for p in prob:
        s = p.split()
        m = len(max(s, key=len)) + 2
        s.append(m)
        prob_list.append(s)
    # TEST appropriate operators & only contain digits & digits in width restriction
    for p in prob_list:
        if p[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (p[0] + p[2]).isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(p[0]) > 4 or len(p[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    operators = {'+': add, '-': sub}
    strings = [[], [], [], []]
    for p in prob_list:
        max_len = p[3]
        strings[0].append(p[0].rjust(max_len))
        strings[1].append(p[1] + p[2].rjust(max_len - 1))
        strings[2].append('-' * max_len)
        res = operators[p[1]](int(p[0]), int(p[2]))
        strings[3].append(str(res).rjust(max_len))
    out = [(" " * 4).join(s) for s in strings[:3 + dec]]
    out = '\n'.join(out)

    return out

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
