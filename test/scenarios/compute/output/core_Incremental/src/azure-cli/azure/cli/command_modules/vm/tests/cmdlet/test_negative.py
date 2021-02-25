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

from azure.cli.testsdk import ScenarioTest
from azure.core.exceptions import ResourceNotFoundError


# Test class for Scenario
class NegativeTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(NegativeTest, self).__init__(*args, **kwargs)

    # EXAMPLE: /VirtualMachines/post/Assess patch state of a virtual machine.
    def test_virtual_machine_assess_patch(self):
        try:
            self.cmd('az vm virtual-machine assess-patch '
                     '--resource-group "myResourceGroupName" '
                     '--name "myVMName"')
            raise Exception("Error Expected!")
        except ResourceNotFoundError as e:
            assert e.message.startswith("(500)")