#/usr/bin/python3
"""Module 101-add_attribute.
Checks if an attribute can be added to an object.
"""


def add_attribute(obj, name, value):
    """Checks if name of value value can be added to obj.
    Args:
        - obj: object to add the attribute to
        - name: name of the attribute
        - value: value of the attribute to add
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
