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

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_synapse.generated._client_factory import cf_big_data_pool
    synapse_big_data_pool = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._big_data_pools_operations#BigDataPoolsOperatio'
        'ns.{}',
        client_factory=cf_big_data_pool)
    with self.command_group('synapse big-data-pool', synapse_big_data_pool, client_factory=cf_big_data_pool) as g:
        g.custom_command('list', 'synapse_big_data_pool_list')
        g.custom_show_command('show', 'synapse_big_data_pool_show')
        g.custom_command('create', 'synapse_big_data_pool_create', supports_no_wait=True)
        g.custom_command('update', 'synapse_big_data_pool_update')
        g.custom_command('delete', 'synapse_big_data_pool_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'synapse_big_data_pool_show')

    from azext_synapse.generated._client_factory import cf_operation
    synapse_operation = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._operations_operations#Operations.{}',
        client_factory=cf_operation)
    with self.command_group('synapse operation', synapse_operation, client_factory=cf_operation) as g:
        g.custom_command('show-azure-async-header-result', 'synapse_operation_show_azure_async_header_result')
        g.custom_command('show-location-header-result', 'synapse_operation_show_location_header_result')

    from azext_synapse.generated._client_factory import cf_ip_firewall_rule
    synapse_ip_firewall_rule = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._ip_firewall_rules_operations#IpFirewallRulesOp'
        'erations.{}',
        client_factory=cf_ip_firewall_rule)
    with self.command_group('synapse ip-firewall-rule', synapse_ip_firewall_rule,
                            client_factory=cf_ip_firewall_rule) as g:
        g.custom_command('list', 'synapse_ip_firewall_rule_list')
        g.custom_show_command('show', 'synapse_ip_firewall_rule_show')
        g.custom_command('create', 'synapse_ip_firewall_rule_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='ip_firewall_rule_info',
                                 setter_name='begin_create_or_update',
                                 custom_func_name='synapse_ip_firewall_rule_update', supports_no_wait=True)
        g.custom_command('delete', 'synapse_ip_firewall_rule_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('replace-all', 'synapse_ip_firewall_rule_replace_all', supports_no_wait=True)
        g.custom_wait_command('wait', 'synapse_ip_firewall_rule_show')

    from azext_synapse.generated._client_factory import cf_sqlpool
    synapse_sqlpool = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pools_operations#SqlPoolsOperations.{}',
        client_factory=cf_sqlpool)
    with self.command_group('synapse sql-pool', synapse_sqlpool, client_factory=cf_sqlpool) as g:
        g.custom_command('list', 'synapse_sql_pool_list')
        g.custom_show_command('show', 'synapse_sql_pool_show')
        g.custom_command('create', 'synapse_sql_pool_create', supports_no_wait=True)
        g.custom_command('update', 'synapse_sql_pool_update')
        g.custom_command('delete', 'synapse_sql_pool_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('pause', 'synapse_sql_pool_pause', supports_no_wait=True)
        g.custom_command('rename', 'synapse_sql_pool_rename')
        g.custom_command('resume', 'synapse_sql_pool_resume', supports_no_wait=True)
        g.custom_wait_command('wait', 'synapse_sql_pool_show')

    from azext_synapse.generated._client_factory import cf_sqlpool_metadata_sync_config
    synapse_sqlpool_metadata_sync_config = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_metadata_sync_configs_operations#SqlP'
        'oolMetadataSyncConfigsOperations.{}',
        client_factory=cf_sqlpool_metadata_sync_config)
    with self.command_group('synapse sql-pool-metadata-sync-config', synapse_sqlpool_metadata_sync_config,
                            client_factory=cf_sqlpool_metadata_sync_config) as g:
        g.custom_show_command('show', 'synapse_sql_pool_metadata_sync_config_show')
        g.custom_command('create', 'synapse_sql_pool_metadata_sync_config_create')

    from azext_synapse.generated._client_factory import cf_sqlpool_operation_result
    synapse_sqlpool_operation_result = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_operation_results_operations#SqlPoolO'
        'perationResultsOperations.{}',
        client_factory=cf_sqlpool_operation_result)
    with self.command_group('synapse sql-pool-operation-result', synapse_sqlpool_operation_result,
                            client_factory=cf_sqlpool_operation_result) as g:
        g.custom_command('show-location-header-result',
                         'synapse_sql_pool_operation_result_show_location_header_result')

    from azext_synapse.generated._client_factory import cf_sqlpool_geo_backup_policy
    synapse_sqlpool_geo_backup_policy = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_geo_backup_policies_operations#SqlPoo'
        'lGeoBackupPoliciesOperations.{}',
        client_factory=cf_sqlpool_geo_backup_policy)
    with self.command_group('synapse sql-pool-geo-backup-policy', synapse_sqlpool_geo_backup_policy,
                            client_factory=cf_sqlpool_geo_backup_policy) as g:
        g.custom_show_command('show', 'synapse_sql_pool_geo_backup_policy_show')

    from azext_synapse.generated._client_factory import cf_sqlpool_data_warehouse_user_activity
    synapse_sqlpool_data_warehouse_user_activity = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_data_warehouse_user_activities_operat'
        'ions#SqlPoolDataWarehouseUserActivitiesOperations.{}',
        client_factory=cf_sqlpool_data_warehouse_user_activity)
    with self.command_group('synapse sql-pool-data-warehouse-user-activity',
                            synapse_sqlpool_data_warehouse_user_activity,
                            client_factory=cf_sqlpool_data_warehouse_user_activity) as g:
        g.custom_show_command('show', 'synapse_sql_pool_data_warehouse_user_activity_show')

    from azext_synapse.generated._client_factory import cf_sqlpool_restore_point
    synapse_sqlpool_restore_point = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_restore_points_operations#SqlPoolRest'
        'orePointsOperations.{}',
        client_factory=cf_sqlpool_restore_point)
    with self.command_group('synapse sql-pool-restore-point', synapse_sqlpool_restore_point,
                            client_factory=cf_sqlpool_restore_point) as g:
        g.custom_command('list', 'synapse_sql_pool_restore_point_list')
        g.custom_command('create', 'synapse_sql_pool_restore_point_create')

    from azext_synapse.generated._client_factory import cf_sqlpool_replication_link
    synapse_sqlpool_replication_link = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_replication_links_operations#SqlPoolR'
        'eplicationLinksOperations.{}',
        client_factory=cf_sqlpool_replication_link)
    with self.command_group('synapse sql-pool-replication-link', synapse_sqlpool_replication_link,
                            client_factory=cf_sqlpool_replication_link) as g:
        g.custom_command('list', 'synapse_sql_pool_replication_link_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_transparent_data_encryption
    synapse_sqlpool_transparent_data_encryption = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_transparent_data_encryptions_operatio'
        'ns#SqlPoolTransparentDataEncryptionsOperations.{}',
        client_factory=cf_sqlpool_transparent_data_encryption)
    with self.command_group('synapse sql-pool-transparent-data-encryption',
                            synapse_sqlpool_transparent_data_encryption,
                            client_factory=cf_sqlpool_transparent_data_encryption) as g:
        g.custom_show_command('show', 'synapse_sql_pool_transparent_data_encryption_show')
        g.custom_command('create', 'synapse_sql_pool_transparent_data_encryption_create')
        g.generic_update_command('update', custom_func_name='synapse_sql_pool_transparent_data_encryption_update')

    from azext_synapse.generated._client_factory import cf_sqlpool_blob_auditing_policy
    synapse_sqlpool_blob_auditing_policy = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_blob_auditing_policies_operations#Sql'
        'PoolBlobAuditingPoliciesOperations.{}',
        client_factory=cf_sqlpool_blob_auditing_policy)
    with self.command_group('synapse sql-pool-blob-auditing-policy', synapse_sqlpool_blob_auditing_policy,
                            client_factory=cf_sqlpool_blob_auditing_policy) as g:
        g.custom_show_command('show', 'synapse_sql_pool_blob_auditing_policy_show')
        g.custom_command('create', 'synapse_sql_pool_blob_auditing_policy_create')
        g.generic_update_command('update', custom_func_name='synapse_sql_pool_blob_auditing_policy_update')

    from azext_synapse.generated._client_factory import cf_sqlpool_operation
    synapse_sqlpool_operation = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_operations_operations#SqlPoolOperatio'
        'nsOperations.{}',
        client_factory=cf_sqlpool_operation)
    with self.command_group('synapse sql-pool-operation', synapse_sqlpool_operation,
                            client_factory=cf_sqlpool_operation) as g:
        g.custom_command('list', 'synapse_sql_pool_operation_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_usage
    synapse_sqlpool_usage = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_usages_operations#SqlPoolUsagesOperat'
        'ions.{}',
        client_factory=cf_sqlpool_usage)
    with self.command_group('synapse sql-pool-usage', synapse_sqlpool_usage, client_factory=cf_sqlpool_usage) as g:
        g.custom_command('list', 'synapse_sql_pool_usage_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_sensitivity_label
    synapse_sqlpool_sensitivity_label = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_sensitivity_labels_operations#SqlPool'
        'SensitivityLabelsOperations.{}',
        client_factory=cf_sqlpool_sensitivity_label)
    with self.command_group('synapse sql-pool-sensitivity-label', synapse_sqlpool_sensitivity_label,
                            client_factory=cf_sqlpool_sensitivity_label) as g:
        g.custom_command('create', 'synapse_sql_pool_sensitivity_label_create')
        g.custom_command('update', 'synapse_sql_pool_sensitivity_label_update')
        g.custom_command('delete', 'synapse_sql_pool_sensitivity_label_delete', confirmation=True)
        g.custom_command('disable-recommendation', 'synapse_sql_pool_sensitivity_label_disable_recommendation')
        g.custom_command('enable-recommendation', 'synapse_sql_pool_sensitivity_label_enable_recommendation')
        g.custom_command('list-current', 'synapse_sql_pool_sensitivity_label_list_current')
        g.custom_command('list-recommended', 'synapse_sql_pool_sensitivity_label_list_recommended')

    from azext_synapse.generated._client_factory import cf_sqlpool_schema
    synapse_sqlpool_schema = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_schemas_operations#SqlPoolSchemasOper'
        'ations.{}',
        client_factory=cf_sqlpool_schema)
    with self.command_group('synapse sql-pool-schema', synapse_sqlpool_schema, client_factory=cf_sqlpool_schema) as g:
        g.custom_command('list', 'synapse_sql_pool_schema_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_table
    synapse_sqlpool_table = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_tables_operations#SqlPoolTablesOperat'
        'ions.{}',
        client_factory=cf_sqlpool_table)
    with self.command_group('synapse sql-pool-table', synapse_sqlpool_table, client_factory=cf_sqlpool_table) as g:
        g.custom_command('list', 'synapse_sql_pool_table_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_table_column
    synapse_sqlpool_table_column = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_table_columns_operations#SqlPoolTable'
        'ColumnsOperations.{}',
        client_factory=cf_sqlpool_table_column)
    with self.command_group('synapse sql-pool-table-column', synapse_sqlpool_table_column,
                            client_factory=cf_sqlpool_table_column) as g:
        g.custom_command('list', 'synapse_sql_pool_table_column_list')

    from azext_synapse.generated._client_factory import cf_sqlpool_connection_policy
    synapse_sqlpool_connection_policy = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_connection_policies_operations#SqlPoo'
        'lConnectionPoliciesOperations.{}',
        client_factory=cf_sqlpool_connection_policy)
    with self.command_group('synapse sql-pool-connection-policy', synapse_sqlpool_connection_policy,
                            client_factory=cf_sqlpool_connection_policy) as g:
        g.custom_show_command('show', 'synapse_sql_pool_connection_policy_show')

    from azext_synapse.generated._client_factory import cf_sqlpool_vulnerability_assessment
    synapse_sqlpool_vulnerability_assessment = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_vulnerability_assessments_operations#'
        'SqlPoolVulnerabilityAssessmentsOperations.{}',
        client_factory=cf_sqlpool_vulnerability_assessment)
    with self.command_group('synapse sql-pool-vulnerability-assessment', synapse_sqlpool_vulnerability_assessment,
                            client_factory=cf_sqlpool_vulnerability_assessment) as g:
        g.custom_command('list', 'synapse_sql_pool_vulnerability_assessment_list')
        g.custom_show_command('show', 'synapse_sql_pool_vulnerability_assessment_show')
        g.custom_command('create', 'synapse_sql_pool_vulnerability_assessment_create')
        g.generic_update_command('update', custom_func_name='synapse_sql_pool_vulnerability_assessment_update')
        g.custom_command('delete', 'synapse_sql_pool_vulnerability_assessment_delete', confirmation=True)

    from azext_synapse.generated._client_factory import cf_sqlpool_vulnerability_assessment_scan
    synapse_sqlpool_vulnerability_assessment_scan = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_vulnerability_assessment_scans_operat'
        'ions#SqlPoolVulnerabilityAssessmentScansOperations.{}',
        client_factory=cf_sqlpool_vulnerability_assessment_scan)
    with self.command_group('synapse sql-pool-vulnerability-assessment-scan',
                            synapse_sqlpool_vulnerability_assessment_scan,
                            client_factory=cf_sqlpool_vulnerability_assessment_scan) as g:
        g.custom_command('list', 'synapse_sql_pool_vulnerability_assessment_scan_list')
        g.custom_command('export', 'synapse_sql_pool_vulnerability_assessment_scan_export')
        g.custom_command('initiate-scan', 'synapse_sql_pool_vulnerability_assessment_scan_initiate_scan')

    from azext_synapse.generated._client_factory import cf_sqlpool_security_alert_policy
    synapse_sqlpool_security_alert_policy = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_security_alert_policies_operations#Sq'
        'lPoolSecurityAlertPoliciesOperations.{}',
        client_factory=cf_sqlpool_security_alert_policy)
    with self.command_group('synapse sql-pool-security-alert-policy', synapse_sqlpool_security_alert_policy,
                            client_factory=cf_sqlpool_security_alert_policy) as g:
        g.custom_show_command('show', 'synapse_sql_pool_security_alert_policy_show')
        g.custom_command('create', 'synapse_sql_pool_security_alert_policy_create')
        g.generic_update_command('update', custom_func_name='synapse_sql_pool_security_alert_policy_update')

    from azext_synapse.generated._client_factory import cf_sqlpool_vulnerability_assessment_rule_baseline
    synapse_sqlpool_vulnerability_assessment_rule_baseline = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._sql_pool_vulnerability_assessment_rule_baselin'
        'es_operations#SqlPoolVulnerabilityAssessmentRuleBaselinesOperations.{}',
        client_factory=cf_sqlpool_vulnerability_assessment_rule_baseline)
    with self.command_group('synapse sql-pool-vulnerability-assessment-rule-baseline',
                            synapse_sqlpool_vulnerability_assessment_rule_baseline,
                            client_factory=cf_sqlpool_vulnerability_assessment_rule_baseline) as g:
        g.custom_command('create', 'synapse_sql_pool_vulnerability_assessment_rule_baseline_create')
        g.custom_command('update', 'synapse_sql_pool_vulnerability_assessment_rule_baseline_update')
        g.custom_command('delete', 'synapse_sql_pool_vulnerability_assessment_rule_baseline_delete',
                         confirmation=True)

    from azext_synapse.generated._client_factory import cf_workspace
    synapse_workspace = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._workspaces_operations#WorkspacesOperations.{}',
        client_factory=cf_workspace)
    with self.command_group('synapse workspace', synapse_workspace, client_factory=cf_workspace) as g:
        g.custom_command('list', 'synapse_workspace_list')
        g.custom_show_command('show', 'synapse_workspace_show')
        g.custom_command('create', 'synapse_workspace_create', supports_no_wait=True)
        g.custom_command('update', 'synapse_workspace_update', supports_no_wait=True)
        g.custom_command('delete', 'synapse_workspace_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'synapse_workspace_show')

    from azext_synapse.generated._client_factory import cf_workspace_aadadmin
    synapse_workspace_aadadmin = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._workspace_aad_admins_operations#WorkspaceAadAd'
        'minsOperations.{}',
        client_factory=cf_workspace_aadadmin)
    with self.command_group('synapse workspace-aad-admin', synapse_workspace_aadadmin,
                            client_factory=cf_workspace_aadadmin) as g:
        g.custom_show_command('show', 'synapse_workspace_aad_admin_show')
        g.custom_command('create', 'synapse_workspace_aad_admin_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='aad_admin_info', setter_name='begin_create_or_update',
                                 custom_func_name='synapse_workspace_aad_admin_update', supports_no_wait=True)
        g.custom_command('delete', 'synapse_workspace_aad_admin_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'synapse_workspace_aad_admin_show')

    from azext_synapse.generated._client_factory import cf_workspace_managed_identity_sqlcontrol_setting
    synapse_workspace_managed_identity_sqlcontrol_setting = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._workspace_managed_identity_sql_control_setting'
        's_operations#WorkspaceManagedIdentitySqlControlSettingsOperations.{}',
        client_factory=cf_workspace_managed_identity_sqlcontrol_setting)
    with self.command_group('synapse workspace-managed-identity-sql-control-setting',
                            synapse_workspace_managed_identity_sqlcontrol_setting,
                            client_factory=cf_workspace_managed_identity_sqlcontrol_setting) as g:
        g.custom_show_command('show', 'synapse_workspace_managed_identity_sql_control_setting_show')
        g.custom_command('create', 'synapse_workspace_managed_identity_sql_control_setting_create')
        g.generic_update_command('update', setter_arg_name='managed_identity_sql_control_settings',
                                 custom_func_name='synapse_workspace_managed_identity_sql_control_setting_update')

    from azext_synapse.generated._client_factory import cf_integration_runtime
    synapse_integration_runtime = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtimes_operations#IntegrationRun'
        'timesOperations.{}',
        client_factory=cf_integration_runtime)
    with self.command_group('synapse integration-runtime', synapse_integration_runtime,
                            client_factory=cf_integration_runtime) as g:
        g.custom_command('list', 'synapse_integration_runtime_list')
        g.custom_show_command('show', 'synapse_integration_runtime_show')
        g.custom_command('create', 'synapse_integration_runtime_create', supports_no_wait=True)
        g.custom_command('update', 'synapse_integration_runtime_update')
        g.custom_command('delete', 'synapse_integration_runtime_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('start', 'synapse_integration_runtime_start')
        g.custom_command('stop', 'synapse_integration_runtime_stop')
        g.custom_command('upgrade', 'synapse_integration_runtime_upgrade')
        g.custom_wait_command('wait', 'synapse_integration_runtime_show')

    from azext_synapse.generated._client_factory import cf_integration_runtime_node_ip_address
    synapse_integration_runtime_node_ip_address = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_node_ip_address_operations'
        '#IntegrationRuntimeNodeIpAddressOperations.{}',
        client_factory=cf_integration_runtime_node_ip_address)
    with self.command_group('synapse integration-runtime-node-ip-address', synapse_integration_runtime_node_ip_address,
                            client_factory=cf_integration_runtime_node_ip_address) as g:
        g.custom_command('get', 'synapse_integration_runtime_node_ip_address_get')

    from azext_synapse.generated._client_factory import cf_integration_runtime_object_metadata
    synapse_integration_runtime_object_metadata = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_object_metadata_operations'
        '#IntegrationRuntimeObjectMetadataOperations.{}',
        client_factory=cf_integration_runtime_object_metadata)
    with self.command_group('synapse integration-runtime-object-metadata', synapse_integration_runtime_object_metadata,
                            client_factory=cf_integration_runtime_object_metadata) as g:
        g.custom_command('get', 'synapse_integration_runtime_object_metadata_get')
        g.custom_command('refresh', 'synapse_integration_runtime_object_metadata_refresh')

    from azext_synapse.generated._client_factory import cf_integration_runtime_node
    synapse_integration_runtime_node = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_nodes_operations#Integrati'
        'onRuntimeNodesOperations.{}',
        client_factory=cf_integration_runtime_node)
    with self.command_group('synapse integration-runtime-node', synapse_integration_runtime_node,
                            client_factory=cf_integration_runtime_node) as g:
        g.custom_show_command('show', 'synapse_integration_runtime_node_show')
        g.custom_command('update', 'synapse_integration_runtime_node_update')
        g.custom_command('delete', 'synapse_integration_runtime_node_delete', confirmation=True)

    from azext_synapse.generated._client_factory import cf_integration_runtime_credentials
    synapse_integration_runtime_credentials = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_credentials_operations#Int'
        'egrationRuntimeCredentialsOperations.{}',
        client_factory=cf_integration_runtime_credentials)
    with self.command_group('synapse integration-runtime-credentials', synapse_integration_runtime_credentials,
                            client_factory=cf_integration_runtime_credentials) as g:
        g.custom_command('sync', 'synapse_integration_runtime_credentials_sync')

    from azext_synapse.generated._client_factory import cf_integration_runtime_connection_info
    synapse_integration_runtime_connection_info = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_connection_infos_operation'
        's#IntegrationRuntimeConnectionInfosOperations.{}',
        client_factory=cf_integration_runtime_connection_info)
    with self.command_group('synapse integration-runtime-connection-info', synapse_integration_runtime_connection_info,
                            client_factory=cf_integration_runtime_connection_info) as g:
        g.custom_command('get', 'synapse_integration_runtime_connection_info_get')

    from azext_synapse.generated._client_factory import cf_integration_runtime_auth_key
    synapse_integration_runtime_auth_key = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_auth_keys_operations#Integ'
        'rationRuntimeAuthKeysOperations.{}',
        client_factory=cf_integration_runtime_auth_key)
    with self.command_group('synapse integration-runtime-auth-key', synapse_integration_runtime_auth_key,
                            client_factory=cf_integration_runtime_auth_key) as g:
        g.custom_command('list', 'synapse_integration_runtime_auth_key_list')
        g.custom_command('regenerate', 'synapse_integration_runtime_auth_key_regenerate')

    from azext_synapse.generated._client_factory import cf_integration_runtime_monitoring_data
    synapse_integration_runtime_monitoring_data = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_monitoring_data_operations'
        '#IntegrationRuntimeMonitoringDataOperations.{}',
        client_factory=cf_integration_runtime_monitoring_data)
    with self.command_group('synapse integration-runtime-monitoring-data', synapse_integration_runtime_monitoring_data,
                            client_factory=cf_integration_runtime_monitoring_data) as g:
        g.custom_command('get', 'synapse_integration_runtime_monitoring_data_get')

    from azext_synapse.generated._client_factory import cf_integration_runtime_status
    synapse_integration_runtime_status = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._integration_runtime_status_operations#Integrat'
        'ionRuntimeStatusOperations.{}',
        client_factory=cf_integration_runtime_status)
    with self.command_group('synapse integration-runtime-status', synapse_integration_runtime_status,
                            client_factory=cf_integration_runtime_status) as g:
        g.custom_command('get', 'synapse_integration_runtime_status_get')

    from azext_synapse.generated._client_factory import cf_private_link_resource
    synapse_private_link_resource = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._private_link_resources_operations#PrivateLinkR'
        'esourcesOperations.{}',
        client_factory=cf_private_link_resource)
    with self.command_group('synapse private-link-resource', synapse_private_link_resource,
                            client_factory=cf_private_link_resource) as g:
        g.custom_command('list', 'synapse_private_link_resource_list')
        g.custom_show_command('show', 'synapse_private_link_resource_show')

    from azext_synapse.generated._client_factory import cf_private_endpoint_connection
    synapse_private_endpoint_connection = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._private_endpoint_connections_operations#Privat'
        'eEndpointConnectionsOperations.{}',
        client_factory=cf_private_endpoint_connection)
    with self.command_group('synapse private-endpoint-connection', synapse_private_endpoint_connection,
                            client_factory=cf_private_endpoint_connection) as g:
        g.custom_command('list', 'synapse_private_endpoint_connection_list')
        g.custom_show_command('show', 'synapse_private_endpoint_connection_show')
        g.custom_command('create', 'synapse_private_endpoint_connection_create', supports_no_wait=True)
        g.custom_command('delete', 'synapse_private_endpoint_connection_delete', supports_no_wait=True,
                         confirmation=True)
        g.custom_wait_command('wait', 'synapse_private_endpoint_connection_show')

    from azext_synapse.generated._client_factory import cf_private_link_hub
    synapse_private_link_hub = CliCommandType(
        operations_tmpl='azext_synapse.vendored_sdks.synapse.operations._private_link_hubs_operations#PrivateLinkHubsOp'
        'erations.{}',
        client_factory=cf_private_link_hub)
    with self.command_group('synapse private-link-hub', synapse_private_link_hub,
                            client_factory=cf_private_link_hub) as g:
        g.custom_command('list', 'synapse_private_link_hub_list')
        g.custom_show_command('show', 'synapse_private_link_hub_show')
        g.custom_command('create', 'synapse_private_link_hub_create')
        g.custom_command('update', 'synapse_private_link_hub_update')
        g.custom_command('delete', 'synapse_private_link_hub_delete', confirmation=True)

    with self.command_group('synapse', is_experimental=True):
        pass