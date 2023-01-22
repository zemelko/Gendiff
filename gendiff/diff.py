FLAGS = ['same', 'delete', 'add', 'diff']


def diff_mapping(dict1, dict2):  # noqa: C901

    def parsed_value(value):

        values = {
            True: 'true',
            False: 'false',
            None: 'null'
        }
        if isinstance(value, dict):
            return value

        return values.get(value, value)

    def mapping(d1, d2):

        union_keys = d1.keys() | d2.keys()
        intersection_keys = d1.keys() & d2.keys()
        left = d1.keys() - d2.keys()
        right = d2.keys() - d1.keys()

        sorted_union_keys = sorted(union_keys)
        diff_of_files = {}
        for key in sorted_union_keys:

            node = []
            childrens = {}

            l_val = parsed_value(d1.get(key))
            r_val = parsed_value(d2.get(key))

            same_key = key in intersection_keys

            both_dicts = isinstance(l_val, dict) and isinstance(r_val, dict)

            if both_dicts:
                childrens = mapping(l_val, r_val)
                diff_of_files[key] = childrens
            else:
                if same_key:
                    if l_val == r_val:
                        node.extend([FLAGS[0], l_val])
                    else:
                        node.extend([FLAGS[3], l_val, r_val])

                if key in left:
                    node.extend([FLAGS[1], l_val])

                if key in right:
                    node.extend([FLAGS[2], r_val])

                diff_of_files[key] = node

        return diff_of_files

    return mapping(dict1, dict2)
