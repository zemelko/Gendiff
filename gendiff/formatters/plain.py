import itertools


def delete(val1=None, val2=None):
    return 'was removed'


def add(val1=None, val2=None):
    return f'was added with value: {val2}'


def update(val1, val2):
    return f'was updated. From {val1} to {val2}'


def decor(val):
    non_string = {
        'true',
        'false',
        'null'
    }

    if val in non_string or isinstance(val, int):
        return val
    else:
        return f'\'{val}\''


def corrected_val(val):
    if isinstance(val, dict):
        return '[complex value]'
    else:
        return decor(val)


CONDITION = {
    'diff': update,
    'delete': delete,
    'add': add
}


def plain(value):  # noqa: C901

    def iter_(current_value, sequence):

        if not isinstance(current_value, dict):
            return str(current_value)

        lines = []
        indent = 'Property'

        for key, node in current_value.items():

            sequence.append(key)

            if isinstance(node, list):

                flag = node[0]
                if flag in CONDITION.keys():
                    if flag == 'diff':
                        l_val = corrected_val(node[1])
                        r_val = corrected_val(node[2])
                        cond_str = CONDITION[flag](l_val, r_val)
                    else:
                        val = corrected_val(node[1])
                        cond_str = CONDITION[flag](val2=val)
                    key_sequence = '.'.join(sequence)
                    r_str = f'{indent} \'{key_sequence}\' {cond_str}'
                    lines.append(r_str)
            else:
                lines.append(iter_(node, sequence))
            sequence.pop()

        result = itertools.chain(lines)
        return '\n'.join(result)

    return iter_(value, [])
