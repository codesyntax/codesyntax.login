# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import codesyntax.login


class CodesyntaxLoginLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=codesyntax.login)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'codesyntax.login:default')


CODESYNTAX_LOGIN_FIXTURE = CodesyntaxLoginLayer()


CODESYNTAX_LOGIN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CODESYNTAX_LOGIN_FIXTURE,),
    name='CodesyntaxLoginLayer:IntegrationTesting',
)


CODESYNTAX_LOGIN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CODESYNTAX_LOGIN_FIXTURE,),
    name='CodesyntaxLoginLayer:FunctionalTesting',
)


CODESYNTAX_LOGIN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CODESYNTAX_LOGIN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CodesyntaxLoginLayer:AcceptanceTesting',
)
