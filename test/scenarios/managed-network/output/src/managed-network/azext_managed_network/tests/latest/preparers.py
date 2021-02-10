# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure_devtools.scenario_tests import SingleValueReplacer
from azure.cli.testsdk.preparers import NoTrafficRecordingPreparer
from azure.cli.testsdk.reverse_dependency import get_dummy_cli


class VirtualNetworkPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(
        self,
        resource_group_key="rg",
        key="vn",
        name_prefix="clitest.vn",
        random_name_length=24,
    ):
        super(VirtualNetworkPreparer, self).__init__(name_prefix, random_name_length)
        self.cli_ctx = get_dummy_cli()
        self.key = key
        self.resource_group_key = resource_group_key
        self.name_prefix = name_prefix
        self.random_name_length = random_name_length

    def create_resource(self, name, **_):
        cmd = 'az network vnet create --resource-group {} --name {}'
        cmd = cmd.format(self.test_class_instance.kwargs.get(self.resource_group_key), name)
        self.live_only_execute(self.cli_ctx, cmd)
        self.test_class_instance.kwargs[self.key] = name
        return {self.key: name}

    def remove_resource(self, name, **_):
        cmd = 'az network vnet delete --resource-group {} --name {}'
        cmd = cmd.format(self.test_class_instance.kwargs.get(self.resource_group_key), name)
        self.live_only_execute(self.cli_ctx, cmd)


class SubnetPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(
        self,
        virtual_network_key="vn",
        resource_group_key="rg",
        key="subnets",
        name_prefix="clitest.subnets",
        random_name_length=24,
    ):
        super(SubnetPreparer, self).__init__(name_prefix, random_name_length)
        self.cli_ctx = get_dummy_cli()
        self.key = key
        self.virtual_network_key = virtual_network_key
        self.resource_group_key = resource_group_key
        self.name_prefix = name_prefix
        self.random_name_length = random_name_length

    def create_resource(self, name, **_):
        cmd = 'az network vnet subnet create -n {} --vnet-name {} -g {} --address-prefixes "10.0.0.0/21"'
        cmd = cmd.format(
            name,
            self.test_class_instance.kwargs.get(self.virtual_network_key),
            self.test_class_instance.kwargs.get(self.resource_group_key),
        )
        self.live_only_execute(self.cli_ctx, cmd)
        self.test_class_instance.kwargs[self.key] = name
        return {self.key: name}

    def remove_resource(self, name, **_):
        cmd = 'az network vnet subnet delete --name {} --resource-group {} --vnet-name {}'
        cmd = cmd.format(
            name,
            self.test_class_instance.kwargs.get(self.resource_group_key),
            self.test_class_instance.kwargs.get(self.virtual_network_key),
        )
        self.live_only_execute(self.cli_ctx, cmd)
