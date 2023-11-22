# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api


class PloneLogin(BrowserView):
    def __call__(self):
        """do the redirect to the proper login view"""
        portal = api.portal.get()
        url = "{}/acl_users/oidc/login".format(portal.absolute_url())
        return self.request.RESPONSE.redirect(url)
