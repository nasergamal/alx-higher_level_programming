#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (TypeError, ValueError, ZeroDivisionError, IndexError) as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return None
