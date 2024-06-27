#!/usr/bin/python3
"""Class with no class or object attribute
- prevents the user from dynamically creating new instance attributes
- except if the new instance attribute is called first_name.
"""


class LockedClass:
    """Simple class with locked slots."""

    __slots__ = ("first_name",)
