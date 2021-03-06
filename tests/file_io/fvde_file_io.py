#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the file-like object implementation using pyfvde."""

import os
import unittest

from dfvfs.lib import errors
from dfvfs.path import fvde_path_spec
from dfvfs.path import os_path_spec
from dfvfs.path import qcow_path_spec
from dfvfs.path import tsk_partition_path_spec
from dfvfs.resolver import resolver
from tests.file_io import test_lib


class FVDEFileTest(test_lib.ImageFileTestCase):
  """Tests for the FileVault Drive Encryption (FVDE) file-like object."""

  _FVDE_PASSWORD = u'fvde-TEST'

  _INODE_PASSWORDS_TXT = 26
  _INODE_ANOTHER_FILE = 24

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    super(FVDEFileTest, self).setUp()
    test_file = os.path.join(u'test_data', u'fvdetest.qcow2')
    path_spec = os_path_spec.OSPathSpec(location=test_file)
    path_spec = qcow_path_spec.QCOWPathSpec(parent=path_spec)
    self._tsk_partition_path_spec = (
        tsk_partition_path_spec.TSKPartitionPathSpec(
            location=u'/p1', parent=path_spec))
    self._fvde_path_spec = fvde_path_spec.FVDEPathSpec(
        parent=self._tsk_partition_path_spec)
    resolver.Resolver.key_chain.SetCredential(
        self._fvde_path_spec, u'password', self._FVDE_PASSWORD)

  def testOpenCloseInode(self):
    """Test the open and close functionality using an inode."""
    self._TestOpenCloseInode(self._fvde_path_spec)

  def testOpenCloseLocation(self):
    """Test the open and close functionality using a location."""
    self._TestOpenCloseLocation(self._fvde_path_spec)

    # Try open with a path specification that has no parent.
    path_spec = fvde_path_spec.FVDEPathSpec(
        parent=self._tsk_partition_path_spec)
    path_spec.parent = None

    with self.assertRaises(errors.PathSpecError):
      self._TestOpenCloseLocation(path_spec)

  def testSeek(self):
    """Test the seek functionality."""
    self._TestSeek(self._fvde_path_spec)

  def testRead(self):
    """Test the read functionality."""
    self._TestRead(self._fvde_path_spec)


if __name__ == '__main__':
  unittest.main()
