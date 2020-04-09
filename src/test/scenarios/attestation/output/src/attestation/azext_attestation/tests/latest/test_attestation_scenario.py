# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg, rg_2, rg_3):
    pass


# EXAMPLE: Operations_List
@try_manual
def step_operations_list(test, rg, rg_2, rg_3):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: AttestationProviders_Create
@try_manual
def step_attestationproviders_create(test, rg, rg_2, rg_3):
    test.cmd('az attestation attestation-provider create '
             '--provider-name "myattestationprovider" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: AttestationProviders_Get
@try_manual
def step_attestationproviders_get(test, rg, rg_2, rg_3):
    test.cmd('az attestation attestation-provider show '
             '--provider-name "myattestationprovider" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def mytest(test, rg, rg_2, rg_3):
    pass


# EXAMPLE: AttestationProviders_List
@try_manual
def step_attestationproviders_list(test, rg, rg_2, rg_3):
    test.cmd('az attestation attestation-provider list',
             checks=[])


# EXAMPLE: AttestationProviders_ListByResourceGroup
@try_manual
def step_attestationproviders_listbyresourcegroup(test, rg, rg_2, rg_3):
    test.cmd('az attestation attestation-provider list '
             '--resource-group "{rg_2}"',
             checks=[])


# EXAMPLE: AttestationProviders_Delete
@try_manual
def step_attestationproviders_delete(test, rg, rg_2, rg_3):
    test.cmd('az attestation attestation-provider delete '
             '--provider-name "myattestationprovider" '
             '--resource-group "{rg_3}"',
             checks=[])


@try_manual
def cleanup(test, rg, rg_2, rg_3):
    pass


@try_manual
def call_scenario(self, rg, rg_2, rg_3):
    setup(test, rg, rg_2, rg_3)
    step_operations_list(test, rg, rg_2, rg_3)
    step_attestationproviders_create(test, rg, rg_2, rg_3)
    step_attestationproviders_get(test, rg, rg_2, rg_3)
    mytest(test, rg, rg_2, rg_3)
    step_attestationproviders_list(test, rg, rg_2, rg_3)
    step_attestationproviders_listbyresourcegroup(test, rg, rg_2, rg_3)
    step_attestationproviders_delete(test, rg, rg_2, rg_3)
    cleanup(test, rg, rg_2, rg_3)


@try_manual
class AttestationManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestattestation_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestattestation_testrg1'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestattestation_sample-resource-group'[:7], key='rg_3', parameter_name='rg_3'
                           '')
    def test_attestation(self, rg, rg_2, rg_3):

        call_scenario(test, rg, rg_2, rg_3)
