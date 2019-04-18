# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.theme


class PloneconfThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf.theme:default')


PLONECONF_THEME_FIXTURE = PloneconfThemeLayer()


PLONECONF_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_THEME_FIXTURE,),
    name='PloneconfThemeLayer:IntegrationTesting'
)


PLONECONF_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_THEME_FIXTURE,),
    name='PloneconfThemeLayer:FunctionalTesting'
)


PLONECONF_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneconfThemeLayer:AcceptanceTesting'
)
