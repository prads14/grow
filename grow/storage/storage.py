"""
Utility functionality for working with storage.
"""

class Storager(object):
    """Generic storage support for object."""

    def __init__(self, *args, storage=None, **kwargs):
        self.storage = storage