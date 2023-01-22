import itertools

INDENTS = {
    'same': '  ',
    'delete': '- ',
    'add': '+ '
}


def stylish(value, indent='  ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        d_ind_sz = depth + spaces_count
        d_ind = indent * (d_ind_sz + depth)
        current_indent = indent * (depth * 2)
        lines = []
        for key, node in current_value.items():

            val = node

            if isinstance(node, list):

                flag = node[0]

                if flag == 'diff':
                    l_ind = INDENTS['delete']
                    r_ind = INDENTS['add']
                    l_val = node[1]
                    r_val = node[2]
                    l_str = f'{d_ind}{l_ind}{key}: {iter_(l_val, d_ind_sz)}'
                    r_str = f'{d_ind}{r_ind}{key}: {iter_(r_val, d_ind_sz)}'

                    lines.append(l_str)
                    lines.append(r_str)
                else:
                    flag_ind = INDENTS[flag]
                    val = node[1]
                    res_str = f'{d_ind}{flag_ind}{key}: {iter_(val, d_ind_sz)}'

                    lines.append(res_str)
            else:
                flag_ind = INDENTS['same']
                res_str = f'{d_ind}{flag_ind}{key}: {iter_(val, d_ind_sz)}'

                lines.append(res_str)

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
