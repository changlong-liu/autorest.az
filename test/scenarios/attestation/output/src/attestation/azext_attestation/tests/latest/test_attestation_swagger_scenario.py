# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .swagger_steps import step_create_provider
from .swagger_steps import step_attestation_provider_update
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_fakedtestscenario
@try_manual
def setup_fakedtestscenario(test):
    cmd = "az deployment group create --resource-group {{rg}} --template-file \"{}\"".format(os.path.join(TEST_DIR, 'depSto.json'))
    o = test.cmd(cmd).get_output_in_json()
    kwargs = {k: v.get("value") for k, v in o.get('properties', {}).get('outputs', {}).items()}
    test.kwargs.update(kwargs)


# Env cleanup_fakedtestscenario
@try_manual
def cleanup_fakedtestscenario(test):
    pass


# Testcase: fakedtestscenario
@try_manual
def call_fakedtestscenario(test):
    setup_fakedtestscenario(test)
    step_create_provider(test, checks=[])
    step_attestation_provider_update(test, checks=[])
    cleanup_fakedtestscenario(test)


# Test class for fakedtestscenario
@try_manual
class AttestationfakedtestscenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(AttestationfakedtestscenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscriptionId': self.get_subscription_id(),
            'location': 'eastus',
        })


    @ResourceGroupPreparer(name_prefix='clitest', key='resourceGroupName', location='eastus')
    def test_attestation_fakedtestscenario(self):
        call_fakedtestscenario(self)
        calc_coverage(__file__)
        raise_if()
