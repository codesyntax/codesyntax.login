# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
from pas.plugins.oidc.plugins import OIDCPlugin

try:
    from pas.plugins.oidc import PLUGIN_ID
except ImportError:
    from pas.plugins.oidc.utils import PLUGIN_ID

@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "codesyntax.login:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["codesyntax.login.upgrades"]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    create_group(context)
    deactivate_challenge_for_oidc(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def create_group(context):
    """create a group for codesyntax users and assing Manager permission"""
    group = api.group.get(groupname="codesyntax.eus")
    if group is None:
        api.group.create(
            groupname="codesyntax.eus",
            title="CodeSyntax",
            description="Group for CodeSyntax Users",
            roles=["Manager"],
        )


def deactivate_challenge_for_oidc(context):
    """deactivate challenge plugin for OIDC plugin"""
    portal = api.portal.get()
    acl_users = portal.get("acl_users", {})
    plugin = acl_users.get(PLUGIN_ID, None)
    plugins = acl_users._getOb("plugins")

    if plugin is not None:
        if not isinstance(plugin, OIDCPlugin):
            raise ValueError(
                "Existing PAS plugin {} is not a OIDCPlugin.".format(PLUGIN_ID)
            )
        pt = plugins._plugin_types
        id = plugin.getId()
        plugins = acl_users._getOb("plugins")
        for type in pt:
            ids = plugins.listPluginIds(type)
            if id in ids:
                plugins.deactivatePlugin(type, id)
