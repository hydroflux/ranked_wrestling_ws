import pprint


def iterate_list(list, web_element=None):
    if web_element is None:
        return [(f'{element}') for element in list]
    else:
        return [(f'{element.text}') for element in list]


def print_list_by_index(list, web_element=None):
    if web_element is None:
        [print(list.index(element), element, '\n-------------------------') for element in list]
    else:
        [print(list.index(element), element.text, '\n-------------------------') for element in list]


def create_printer():
    return pprint.PrettyPrinter(indent=4, sort_dicts=True, compact=False)


def print_class_instance(instance):
    printer = create_printer()
    attributes = vars(instance)
    printer.pprint(attributes)
