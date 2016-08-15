# programmed by Bak Yeon O(bakyeono@gmail.com)

import sys
import re


OPS = {
    'MUL': lambda x, y: x.__mul__(y),
    'DIV': lambda x, y: x.__truediv__(y),
    'ADD': lambda x, y: x.__add__(y),
    'SUB': lambda x, y: x.__sub__(y),
}


EXPS = {
    'NUM': r'^([\+-]?\d+\.?\d*)$',
    'POS': r'^\+([\+-]?\d+\.?\d*)$',
    'NEG': r'^-([\+-]?\d+\.?\d*)$',
    'PAR': r'^(.*)\(([^()]*)\)(.*)$',
    'MUL': r'^([^\*/]*?)(\d+\.?\d*)\*([\+-]?\d+\.?\d*)(.*)$',
    'DIV': r'^([^\*/]*?)(\d+\.?\d*)/([\+-]?\d+\.?\d*)(.*)$',
    'ADD': r'^([\+-]?\d+\.?\d*)\+(-?\d+\.?\d*)(.*)$',
    'SUB': r'^([\+-]?\d+\.?\d*)-(-?\d+\.?\d*)(.*)$',
}

for k, v in EXPS.items():
    EXPS[k] = re.compile(v)


def evaluate(exp):
    case = EXPS['NUM'].match(exp)
    if case:
        return case.group(1)

    case = EXPS['POS'].match(exp)
    if case:
        return evaluate(case.group(1))

    case = EXPS['NEG'].match(exp)
    if case:
        return evaluate(str(-1.0 * float(case.group(1))))

    case = EXPS['PAR'].search(exp)
    if case:
        return evaluate(case.group(1) + evaluate(case.group(2)) + case.group(3))

    case = EXPS['MUL'].search(exp)
    if case:
        return evaluate(case.group(1) + str(OPS['MUL'](float(case.group(2)), float(case.group(3)))) + case.group(4))

    case = EXPS['DIV'].search(exp)
    if case:
        return evaluate(case.group(1) + str(OPS['DIV'](float(case.group(2)), float(case.group(3)))) + case.group(4))

    case = EXPS['ADD'].search(exp)
    if case:
        return evaluate(str(OPS['ADD'](float(case.group(1)), float(case.group(2)))) + case.group(3))

    case = EXPS['SUB'].search(exp)
    if case:
        return evaluate(str(OPS['SUB'](float(case.group(1)), float(case.group(2)))) + case.group(3))

    exit(42)


def strip_whitespaces(s):
    s = s.replace(' ', '')
    s = s.replace('\t', '')
    s = s.replace('\n', '')
    return s


try:
    result = float(evaluate(strip_whitespaces(sys.argv[1])))
    if result.is_integer():
        print(str(int(result)))
    else:
        print(str(result))
    exit(0)

except Exception:
    exit(42)
