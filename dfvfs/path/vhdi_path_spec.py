# -*- coding: utf-8 -*-
"""The VHD image path specification implementation."""

from dfvfs.lib import definitions
from dfvfs.path import factory
from dfvfs.path import path_spec


class VHDIPathSpec(path_spec.PathSpec):
  """Class that implements the VHD image path specification."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_VHDI

  def __init__(self, parent=None, **kwargs):
    """Initializes the path specification object.

    Note that the VHDI file path specification must have a parent.

    Args:
      parent (Optional[PathSpec]): parent path specification.

    Raises:
      ValueError: when parent is not set.
    """
    if not parent:
      raise ValueError(u'Missing parent value.')

    super(VHDIPathSpec, self).__init__(parent=parent, **kwargs)

  @property
  def comparable(self):
    """str: comparable representation of the path specification."""
    return self._GetComparable()


# Register the path specification with the factory.
factory.Factory.RegisterPathSpec(VHDIPathSpec)
