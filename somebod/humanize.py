# -*- coding: UTF-8 -*-

import decimal

intword_converters = ((1E15, "P"), (1E12, "T"), (1E9, "G"), (1E6, "M"), (1E3, "K"))


def intword(val):
    """
      Converts a large number to a friendly text representation.
      Inspired in large part by django.contrib.humanize
    """
    if val is None:
        return ""
    if isinstance(val, str) or isinstance(val, unicode):
        return val

    if isinstance(val, decimal.Decimal):
        val = float(val)

    for thr, suffix in intword_converters:
        if val > thr:
            return "%.1f%s" % (float(val) / thr, suffix)
    if isinstance(val, float):
        return "%.1f" % val
    return str(val)


def print_ratio(value, den):
    """
        Human output of a ratio
    """
    return "%s/%s (%.2f%%)" % (intword(value), intword(den), 100. * value / den if den else 0.)
