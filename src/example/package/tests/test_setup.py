# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from example.package.testing import EXAMPLE_PACKAGE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that example.package is properly installed."""

    layer = EXAMPLE_PACKAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.package is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'example.package'))

    def test_browserlayer(self):
        """Test that IExamplePackageLayer is registered."""
        from example.package.interfaces import (
            IExamplePackageLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IExamplePackageLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EXAMPLE_PACKAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['example.package'])

    def test_product_uninstalled(self):
        """Test if example.package is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'example.package'))

    def test_browserlayer_removed(self):
        """Test that IExamplePackageLayer is removed."""
        from example.package.interfaces import \
            IExamplePackageLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IExamplePackageLayer,
           utils.registered_layers())
