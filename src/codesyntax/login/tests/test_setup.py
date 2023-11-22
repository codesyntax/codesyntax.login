# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from codesyntax.login.testing import CODESYNTAX_LOGIN_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that codesyntax.login is properly installed."""

    layer = CODESYNTAX_LOGIN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if codesyntax.login is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'codesyntax.login'))

    def test_browserlayer(self):
        """Test that ICodesyntaxLoginLayer is registered."""
        from codesyntax.login.interfaces import (
            ICodesyntaxLoginLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICodesyntaxLoginLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CODESYNTAX_LOGIN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('codesyntax.login')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if codesyntax.login is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'codesyntax.login'))

    def test_browserlayer_removed(self):
        """Test that ICodesyntaxLoginLayer is removed."""
        from codesyntax.login.interfaces import \
            ICodesyntaxLoginLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICodesyntaxLoginLayer, utils.registered_layers())
