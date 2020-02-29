# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ManagedNetworkManagementClientScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_managed_network_myResourceGroup', key='rg')
    def test_managed_network(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.cmd('az managed-network managed-networks create '
                 '--location "eastus" '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-network-groups create '
                 '--managed-network-group-name "myManagedNetworkGroup1" '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network scope-assignments create '
                 '--assigned-managed-network "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.ManagedNetwork/managedNetworks/myManagedNetwork" '
                 '--scope "subscriptions/subscriptionC" '
                 '--scope-assignment-name "subscriptionCAssignment"',
                 checks=[])

        self.cmd('az managed-network managed-network-peering-policies create '
                 '--managed-network-name "myManagedNetwork" '
                 '--managed-network-peering-policy-name "myHubAndSpoke" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-networks show '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-networks list '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-networks list',
                 checks=[])

        self.cmd('az managed-network scope-assignments show '
                 '--scope "subscriptions/subscriptionC" '
                 '--scope-assignment-name "subscriptionCAssignment"',
                 checks=[])

        self.cmd('az managed-network scope-assignments list '
                 '--scope "subscriptions/subscriptionC"',
                 checks=[])

        self.cmd('az managed-network managed-network-groups show '
                 '--managed-network-group-name "myManagedNetworkGroup1" '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-network-groups list '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-network-peering-policies show '
                 '--managed-network-name "myManagedNetwork" '
                 '--managed-network-peering-policy-name "myHubAndSpoke" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-network-peering-policies list '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-network-peering-policies delete '
                 '--managed-network-name "myManagedNetwork" '
                 '--managed-network-peering-policy-name "myHubAndSpoke" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network scope-assignments delete '
                 '--scope "subscriptions/subscriptionC" '
                 '--scope-assignment-name "subscriptionCAssignment"',
                 checks=[])

        self.cmd('az managed-network managed-network-groups delete '
                 '--managed-network-group-name "myManagedNetworkGroup1" '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az managed-network managed-networks delete '
                 '--managed-network-name "myManagedNetwork" '
                 '--resource-group "{rg}"',
                 checks=[])
