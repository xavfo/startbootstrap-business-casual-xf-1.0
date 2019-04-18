# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ploneconf.theme.testing import PLONECONF_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.theme is properly installed."""

    layer = PLONECONF_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.theme'))

    def test_browserlayer(self):
        """Test that IPloneconfThemeLayer is registered."""
        from ploneconf.theme.interfaces import (
            IPloneconfThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneconfThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneconf.theme'])

    def test_product_uninstalled(self):
        """Test if ploneconf.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.theme'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfThemeLayer is removed."""
        from ploneconf.theme.interfaces import \
            IPloneconfThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneconfThemeLayer, utils.registered_layers())
