import inspect


def _to_parameter_name(par_name):
    """Given a string, it returns a version of it that can be used as a Python parameter name"""
    return par_name.translate({ord(c): "_" for c in "/!@#*+-%&|<>[]()$ \r\n\t"})


def remove_duplicates(elements: list[inspect.Parameter]):
    """monkey-patch solution to remove duplicate entries from the
    signature parameters list without destroying its ordering"""
    keys = set()
    out_els = []
    for e in elements:
        if e.name not in keys:
            out_els.append(e)
            keys.add(e.name)
    return out_els


def build_translation_tables(*args):
    """given any collection of strings, it evaluates sanitized versions of said strings
    and returns two dictionaries containing the translation mapping:
    original string -> sanitized string
    and
    sanitized string -> original string"""
    ab = {}
    ba = {}
    for d in args:
        for k in d:
            san_k = _to_parameter_name(k)
            ab[k] = san_k
            ba[san_k] = k
    return ab, ba
