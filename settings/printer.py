import pprint


def create_printer():
    return pprint.PrettyPrinter(indent=4, sort_dicts=True, compact=False)


def print_object(object):
    printer = create_printer()
    printer.pprint(object)
