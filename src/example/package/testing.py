# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import example.package


class ExamplePackageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=example.package)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.package:default')


EXAMPLE_PACKAGE_FIXTURE = ExamplePackageLayer()


EXAMPLE_PACKAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_PACKAGE_FIXTURE,),
    name='ExamplePackageLayer:IntegrationTesting'
)


EXAMPLE_PACKAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_PACKAGE_FIXTURE,),
    name='ExamplePackageLayer:FunctionalTesting'
)


EXAMPLE_PACKAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_PACKAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ExamplePackageLayer:AcceptanceTesting'
)
