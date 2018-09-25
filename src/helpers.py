"""
Various helper functions used by PythonTurtle.
"""
import math
import os
import queue
import sys


def deg_to_rad(deg):
    """Convert degrees to radians."""
    return (deg * math.pi) / 180


def rad_to_deg(rad):
    """Convert radians to degrees."""
    return (rad / math.pi) * 180


def dump_queue(my_queue):
    """
    Empties all pending items in a queue and returns them in a list.
    """
    result = []

    while True:
        try:
            thing = my_queue.get(block=False)
            result.append(thing)
        except queue.Empty:
            return result


def from_resource_folder(filename):
    """
    Absolute path for a file assumed to be in resources folder.
    """
    return os.path.join('PythonTurtle.app',
                        'Contents',
                        'Resources',
                        'resources',
                        filename) if sys.platform == "darwin" \
        else os.path.join('resources', filename)