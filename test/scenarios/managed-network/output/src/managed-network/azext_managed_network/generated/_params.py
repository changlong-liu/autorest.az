# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_managed_network.action import (
    AddSubscriptions,
    AddVirtualNetworks,
    AddSubnets,
    AddHub,
    AddSpokes,
    AddMesh
)


def load_arguments(self, _):

    with self.argument_context('managed-network mn list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('top', type=int, help='May be used to limit the number of results in a page for list queries.')
        c.argument('skiptoken', type=str, help='Skiptoken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skiptoken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('managed-network mn create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', options_list=['--name', '-n', '--managed-network-name'], type=str,
                   help='The name of the Managed Network.')
        c.argument('managed_network', type=validate_file_or_dict, help='Parameters supplied to the create/update a '
                   'Managed Network Resource Expected value: json-string/@json-file.')

    with self.argument_context('managed-network mn update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', options_list=['--name', '-n', '--managed-network-name'], type=str,
                   help='The name of the Managed Network.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('managed-network mn delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', options_list=['--name', '-n', '--managed-network-name'], type=str,
                   help='The name of the Managed Network.', id_part='name')

    with self.argument_context('managed-network mn show-modify') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', options_list=['--name', '-n', '--managed-network-name'], type=str,
                   help='The name of the Managed Network.', id_part='name')

    with self.argument_context('managed-network mn scope-assignment list') as c:
        c.argument('scope', type=str, help='The base resource of the scope assignment.')

    with self.argument_context('managed-network mn scope-assignment show') as c:
        c.argument('scope', type=str, help='The base resource of the scope assignment.')
        c.argument('scope_assignment_name', options_list=['--name', '-n', '--scope-assignment-name'], type=str,
                   help='The name of the scope assignment to get.')

    with self.argument_context('managed-network mn scope-assignment create') as c:
        c.argument('scope', type=str, help='The base resource of the scope assignment to create. The scope can be any '
                   'REST resource instance. For example, use \'subscriptions/{subscription-id}\' for a subscription, '
                   '\'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and '
                   '\'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider'
                   '}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('scope_assignment_name', options_list=['--name', '-n', '--scope-assignment-name'], type=str,
                   help='The name of the scope assignment to create.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('assigned_managed_network', type=str,
                   help='The managed network ID with scope will be assigned to.')

    with self.argument_context('managed-network mn scope-assignment update') as c:
        c.argument('scope', type=str, help='The base resource of the scope assignment to create. The scope can be any '
                   'REST resource instance. For example, use \'subscriptions/{subscription-id}\' for a subscription, '
                   '\'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and '
                   '\'subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider'
                   '}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('scope_assignment_name', options_list=['--name', '-n', '--scope-assignment-name'], type=str,
                   help='The name of the scope assignment to create.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('assigned_managed_network', type=str,
                   help='The managed network ID with scope will be assigned to.')
        c.ignore('parameters')

    with self.argument_context('managed-network mn scope-assignment delete') as c:
        c.argument('scope', type=str, help='The scope of the scope assignment to delete.')
        c.argument('scope_assignment_name', options_list=['--name', '-n', '--scope-assignment-name'], type=str,
                   help='The name of the scope assignment to delete.')

    with self.argument_context('managed-network mn group list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.')
        c.argument('top', type=int, help='May be used to limit the number of results in a page for list queries.')
        c.argument('skiptoken', type=str, help='Skiptoken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skiptoken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('managed-network mn group show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('group_name', type=str, help='The name of the Managed Network Group.', id_part='child_name_1')

    with self.argument_context('managed-network mn group create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.')
        c.argument('group_name', type=str, help='The name of the Managed Network Group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('management_groups', type=validate_file_or_dict, help='The collection of management groups covered '
                   'by the Managed Network Expected value: json-string/@json-file.')
        c.argument('subscriptions', action=AddSubscriptions, nargs='+', help='The collection of subscriptions covered '
                   'by the Managed Network')
        c.argument('virtual_networks', action=AddVirtualNetworks, nargs='+', help='The collection of virtual nets '
                   'covered by the Managed Network')
        c.argument('subnets', action=AddSubnets, nargs='+', help='The collection of  subnets covered by the Managed '
                   'Network')

    with self.argument_context('managed-network mn group update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('group_name', type=str, help='The name of the Managed Network Group.', id_part='child_name_1')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('management_groups', type=validate_file_or_dict, help='The collection of management groups covered '
                   'by the Managed Network Expected value: json-string/@json-file.')
        c.argument('subscriptions', action=AddSubscriptions, nargs='+', help='The collection of subscriptions covered '
                   'by the Managed Network')
        c.argument('virtual_networks', action=AddVirtualNetworks, nargs='+', help='The collection of virtual nets '
                   'covered by the Managed Network')
        c.argument('subnets', action=AddSubnets, nargs='+', help='The collection of  subnets covered by the Managed '
                   'Network')
        c.ignore('managed_network_group_name', 'managed_network_group')

    with self.argument_context('managed-network mn group delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('group_name', type=str, help='The name of the Managed Network Group.', id_part='child_name_1')

    with self.argument_context('managed-network mn group wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('group_name', type=str, help='The name of the Managed Network Group.', id_part='child_name_1')

    with self.argument_context('managed-network managed-network-peering-policy list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.')
        c.argument('top', type=int, help='May be used to limit the number of results in a page for list queries.')
        c.argument('skiptoken', type=str, help='Skiptoken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skiptoken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('managed-network managed-network-peering-policy show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.',
                   id_part='child_name_1')

    with self.argument_context('managed-network managed-network-peering-policy hub-and-spoke-topology create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('hub', action=AddHub, nargs='+', help='Gets or sets the hub virtual network ID')
        c.argument('spokes', action=AddSpokes, nargs='+', help='Gets or sets the spokes group IDs')
        c.argument('mesh', action=AddMesh, nargs='+', help='Gets or sets the mesh group IDs')
        c.argument('managed_network_policy', type=str, help='inside managedNetworkPolicy')

    with self.argument_context('managed-network managed-network-peering-policy mesh-topology create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('hub', action=AddHub, nargs='+', help='Gets or sets the hub virtual network ID')
        c.argument('spokes', action=AddSpokes, nargs='+', help='Gets or sets the spokes group IDs')
        c.argument('mesh', action=AddMesh, nargs='+', help='Gets or sets the mesh group IDs')
        c.argument('managed_network_policy', type=str, help='inside managedNetworkPolicy')

    with self.argument_context('managed-network managed-network-peering-policy hub-and-spoke-topology update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.',
                   id_part='child_name_1')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('hub', action=AddHub, nargs='+', help='Gets or sets the hub virtual network ID')
        c.argument('spokes', action=AddSpokes, nargs='+', help='Gets or sets the spokes group IDs')
        c.argument('mesh', action=AddMesh, nargs='+', help='Gets or sets the mesh group IDs')
        c.argument('managed_network_policy', type=str, help='inside managedNetworkPolicy')
        c.ignore('managed_network_peering_policy_name')

    with self.argument_context('managed-network managed-network-peering-policy mesh-topology update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.',
                   id_part='child_name_1')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('hub', action=AddHub, nargs='+', help='Gets or sets the hub virtual network ID')
        c.argument('spokes', action=AddSpokes, nargs='+', help='Gets or sets the spokes group IDs')
        c.argument('mesh', action=AddMesh, nargs='+', help='Gets or sets the mesh group IDs')
        c.argument('managed_network_policy', type=str, help='inside managedNetworkPolicy')
        c.ignore('managed_network_peering_policy_name')

    with self.argument_context('managed-network managed-network-peering-policy delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.',
                   id_part='child_name_1')

    with self.argument_context('managed-network managed-network-peering-policy wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_network_name', type=str, help='The name of the Managed Network.', id_part='name')
        c.argument('policy_name', type=str, help='The name of the Managed Network Peering Policy.',
                   id_part='child_name_1')
