# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azure.cli.core.utils import get_resource_name_completion_list
from azure.cli.core.exception import handle_template_based_exception
from ..generated._client_factory import (
    cf_cluster,
    cf_cluster_principal_assignment,
    cf_database,
    cf_database_principal_assignment,
    cf_attached_database_configuration,
    cf_data_connection,
)


kusto_attached_database_configuration = CliCommandType(
    operations_tmpl='azure.mgmt.kusto.operations._attached_database_configurations_operations#AttachedDatabaseConfigurationsOperations.{}',
    client_factory=cf_attached_database_configuration,
)


kusto_cluster = CliCommandType(
    operations_tmpl='azure.mgmt.kusto.operations._clusters_operations#ClustersOperations.{}', client_factory=cf_cluster
)


kusto_cluster_principal_assignment = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.kusto.operations._cluster_principal_assignments_operations#ClusterPrincipalAssignmentsOperations.{}'
    ),
    client_factory=cf_cluster_principal_assignment,
)


kusto_data_connection = CliCommandType(
    operations_tmpl='azure.mgmt.kusto.operations._data_connections_operations#DataConnectionsOperations.{}',
    client_factory=cf_data_connection,
)


kusto_database = CliCommandType(
    operations_tmpl='azure.mgmt.kusto.operations._databases_operations#DatabasesOperations.{}',
    client_factory=cf_database,
)


kusto_database_principal_assignment = CliCommandType(
    operations_tmpl='azure.mgmt.kusto.operations._database_principal_assignments_operations#DatabasePrincipalAssignmentsOperations.{}',
    client_factory=cf_database_principal_assignment,
)


def load_command_table(self, _):

    with self.command_group(
        'kusto attached-database-configuration',
        kusto_attached_database_configuration,
        client_factory=cf_attached_database_configuration,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'kusto_attached_database_configuration_list')
        g.custom_show_command('show', 'kusto_attached_database_configuration_show')
        g.custom_command('create', 'kusto_attached_database_configuration_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_attached_database_configuration_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_attached_database_configuration_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_attached_database_configuration_show')

    with self.command_group('kusto cluster', kusto_cluster, client_factory=cf_cluster, is_experimental=True) as g:
        g.custom_command('list', 'kusto_cluster_list')
        g.custom_show_command('show', 'kusto_cluster_show')
        g.custom_command('create', 'kusto_cluster_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_cluster_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_cluster_delete', supports_no_wait=True, confirmation=True)
        g.custom_command(
            'add-language-extension',
            'kusto_cluster_add_language_extension',
            completer=get_resource_name_completion_list('Microsoft.Network/expressRouteCircuits'),
            supports_no_wait=True,
        )
        g.custom_command('detach-follower-database', 'kusto_cluster_detach_follower_database', supports_no_wait=True)
        g.custom_command('diagnose-virtual-network', 'kusto_cluster_diagnose_virtual_network', supports_no_wait=True)
        g.custom_command('list-follower-database', 'kusto_cluster_list_follower_database')
        g.custom_command('list-language-extension', 'kusto_cluster_list_language_extension')
        g.custom_command('list-sku', 'kusto_cluster_list_sku')
        g.custom_command(
            'remove-language-extension',
            'kusto_cluster_remove_language_extension',
            exception_handler=handle_template_based_exception,
            supports_no_wait=True,
        )
        g.custom_command('start', 'kusto_cluster_start', supports_no_wait=True)
        g.custom_command('stop', 'kusto_cluster_stop', supports_no_wait=True)
        g.custom_wait_command('wait', 'kusto_cluster_show')

    with self.command_group(
        'kusto cluster-principal-assignment',
        kusto_cluster_principal_assignment,
        client_factory=cf_cluster_principal_assignment,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'kusto_cluster_principal_assignment_list')
        g.custom_show_command('show', 'kusto_cluster_principal_assignment_show')
        g.custom_command('create', 'kusto_cluster_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_cluster_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_cluster_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_cluster_principal_assignment_show')

    with self.command_group(
        'kusto data-connection', kusto_data_connection, client_factory=cf_data_connection, is_experimental=True
    ) as g:
        g.custom_command('list', 'kusto_data_connection_list')
        g.custom_show_command('show', 'kusto_data_connection_show')
        g.custom_command('create', 'kusto_data_connection_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_data_connection_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_data_connection_delete', supports_no_wait=True, confirmation=True)
        g.custom_command(
            'data-connection-validation', 'kusto_data_connection_data_connection_validation', supports_no_wait=True
        )
        g.custom_wait_command('wait', 'kusto_data_connection_show')

    with self.command_group(
        'kusto database',
        kusto_database,
        client_factory=cf_database,
        exception_handler=handle_template_based_exception,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'kusto_database_list', option_list=['--private-cloud', 123, True])
        g.custom_show_command('show', 'kusto_database_show')
        g.custom_command('create', 'kusto_database_create', supports_no_wait=True)
        g.custom_command('update', 'kusto_database_update', supports_no_wait=True)
        g.custom_command('delete', 'kusto_database_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('add-principal', 'kusto_database_add_principal')
        g.custom_command('list-principal', 'kusto_database_list_principal')
        g.custom_command('remove-principal', 'kusto_database_remove_principal')
        g.custom_wait_command('wait', 'kusto_database_show')

    with self.command_group(
        'kusto database-principal-assignment',
        kusto_database_principal_assignment,
        client_factory=cf_database_principal_assignment,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'kusto_database_principal_assignment_list')
        g.custom_show_command('show', 'kusto_database_principal_assignment_show')
        g.custom_command('create', 'kusto_database_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='kusto_database_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'kusto_database_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'kusto_database_principal_assignment_show')
