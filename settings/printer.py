from copy import copy
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


def create_instance_copy(instance):
    return copy(instance)


def create_printer():
    return pprint.PrettyPrinter(indent=4, sort_dicts=True, compact=False)


def get_attributes(instance):
    attributes = vars(instance)
    for key, values in attributes.items():
        if type(values) is list:
            nested_attributes = []
            for nested_attribute in values:
                nested_attributes.append(vars(nested_attribute))
            attributes[key] = nested_attributes
    return attributes


def print_class_instance(instance):
    copy = create_instance_copy(instance)
    printer = create_printer()
    attributes = get_attributes(copy)
    printer.pprint(attributes)
