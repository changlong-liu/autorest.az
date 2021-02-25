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


# Test class for Scenario
class PositiveTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(PositiveTest, self).__init__(*args, **kwargs)

    # EXAMPLE: /Clusters/get/KustoClustersListByResourceGroup
    def test_cluster_list2(self):
        self.cmd('az kusto cluster list '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/get/KustoClustersList
    def test_cluster_list(self):
        self.cmd('az kusto cluster list')

    # EXAMPLE: /Clusters/get/KustoClustersGet
    def test_cluster_show(self):
        self.cmd('az kusto cluster show '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/put/KustoClustersCreateOrUpdate
    def test_cluster_create(self):
        self.cmd('az kusto cluster create '
                 '--cluster-name "kustoclusterrptest4" '
                 '--type "SystemAssigned" '
                 '--location "westus" '
                 '--enable-double-encryption false '
                 '--enable-purge true '
                 '--enable-streaming-ingest true '
                 '--name "Standard_L8s" '
                 '--capacity 2 '
                 '--tier "Standard" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/patch/KustoClustersUpdate
    def test_cluster_update(self):
        self.cmd('az kusto cluster update '
                 '--cluster-name "kustoclusterrptest4" '
                 '--type "SystemAssigned" '
                 '--location "westus" '
                 '--enable-purge true '
                 '--enable-streaming-ingest true '
                 '--key-vault-properties key-name="keyName" key-vault-uri="https://dummy.keyvault.com" key-version="keyVersion" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/delete/KustoClustersDelete
    def test_cluster_delete(self):
        self.cmd('az kusto cluster delete -y '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClusterAddLanguageExtensions
    def test_cluster_add_language_extension(self):
        self.cmd('az kusto cluster add-language-extension '
                 '--name "kustoclusterrptest4" '
                 '--value language-extension-name="PYTHON" '
                 '--value language-extension-name="R" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClusterDetachFollowerDatabases
    def test_cluster_detach_follower_database(self):
        self.cmd('az kusto cluster detach-follower-database '
                 '--name "kustoclusterrptest4" '
                 '--attached-database-configuration-name "myAttachedDatabaseConfiguration" '
                 '--cluster-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.Kusto/clusters/leader4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClusterDiagnoseVirtualNetwork
    def test_cluster_diagnose_virtual_network(self):
        self.cmd('az kusto cluster diagnose-virtual-network '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClusterListFollowerDatabases
    def test_cluster_list_follower_database(self):
        self.cmd('az kusto cluster list-follower-database '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClusterListLanguageExtensions
    def test_cluster_list_language_extension(self):
        self.cmd('az kusto cluster list-language-extension '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/get/KustoClustersListResourceSkus
    def test_cluster_list_sku(self):
        self.cmd('az kusto cluster list-sku '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/get/KustoClustersListSkus
    def test_cluster_list_sku2(self):
        self.cmd('az kusto cluster list-sku')

    # EXAMPLE: /Clusters/post/KustoClusterRemoveLanguageExtensions
    def test_cluster_remove_language_extension(self):
        self.cmd('az kusto cluster remove-language-extension '
                 '--name "kustoclusterrptest4" '
                 '--value language-extension-name="PYTHON" '
                 '--value language-extension-name="R" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClustersStart
    def test_cluster_start(self):
        self.cmd('az kusto cluster start '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Clusters/post/KustoClustersStop
    def test_cluster_stop(self):
        self.cmd('az kusto cluster stop '
                 '--name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /ClusterPrincipalAssignments/get/KustoPrincipalAssignmentsList
    def test_cluster_principal_assignment_list(self):
        self.cmd('az kusto cluster-principal-assignment list '
                 '--cluster-name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /ClusterPrincipalAssignments/get/KustoClusterPrincipalAssignmentsGet
    def test_cluster_principal_assignment_show(self):
        self.cmd('az kusto cluster-principal-assignment show '
                 '--cluster-name "kustoclusterrptest4" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /ClusterPrincipalAssignments/put/KustoClusterPrincipalAssignmentsCreateOrUpdate
    def test_cluster_principal_assignment_create(self):
        self.cmd('az kusto cluster-principal-assignment create '
                 '--cluster-name "kustoclusterrptest4" '
                 '--principal-id "87654321-1234-1234-1234-123456789123" '
                 '--principal-type "App" '
                 '--role "AllDatabasesAdmin" '
                 '--tenant-id "12345678-1234-1234-1234-123456789123" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /ClusterPrincipalAssignments/delete/KustoClusterPrincipalAssignmentsDelete
    def test_cluster_principal_assignment_delete(self):
        self.cmd('az kusto cluster-principal-assignment delete -y '
                 '--cluster-name "kustoclusterrptest4" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/get/KustoDatabasesListByCluster
    def test_database_list(self):
        self.cmd('az kusto database list '
                 '--cluster-name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/get/KustoDatabasesGet
    def test_database_show(self):
        self.cmd('az kusto database show '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/put/KustoDatabasesCreateOrUpdate
    def test_database_create(self):
        self.cmd('az kusto database create '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--read-write-database location="westus" soft-delete-period="P1D" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/patch/KustoDatabasesUpdate
    def test_database_update(self):
        self.cmd('az kusto database update '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--parameters "{{\\"properties\\":{{\\"softDeletePeriod\\":\\"P1D\\"}}}}" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/delete/KustoDatabasesDelete
    def test_database_delete(self):
        self.cmd('az kusto database delete -y '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/post/KustoDatabaseAddPrincipals
    def test_database_add_principal(self):
        self.cmd('az kusto database add-principal '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--value name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser=some_guid" role="Admin" '
                 '--value name="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup=some_guid" role="Viewer" '
                 '--value name="SomeApp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp=some_guid_app_id" role="Admin" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/post/KustoDatabaseListPrincipals
    def test_database_list_principal(self):
        self.cmd('az kusto database list-principal '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /Databases/post/KustoDatabaseRemovePrincipals
    def test_database_remove_principal(self):
        self.cmd('az kusto database remove-principal '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--value name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser=some_guid" role="Admin" '
                 '--value name="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup=some_guid" role="Viewer" '
                 '--value name="SomeApp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp=some_guid_app_id" role="Admin" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DatabasePrincipalAssignments/get/KustoPrincipalAssignmentsList
    def test_database_principal_assignment_list(self):
        self.cmd('az kusto database-principal-assignment list '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "Kustodatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DatabasePrincipalAssignments/get/KustoDatabasePrincipalAssignmentsGet
    def test_database_principal_assignment_show(self):
        self.cmd('az kusto database-principal-assignment show '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "Kustodatabase8" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DatabasePrincipalAssignments/put/KustoDatabasePrincipalAssignmentsCreateOrUpdate
    def test_database_principal_assignment_create(self):
        self.cmd('az kusto database-principal-assignment create '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "Kustodatabase8" '
                 '--principal-id "87654321-1234-1234-1234-123456789123" '
                 '--principal-type "App" '
                 '--role "Admin" '
                 '--tenant-id "12345678-1234-1234-1234-123456789123" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DatabasePrincipalAssignments/delete/KustoDatabasePrincipalAssignmentsDelete
    def test_database_principal_assignment_delete(self):
        self.cmd('az kusto database-principal-assignment delete -y '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "Kustodatabase8" '
                 '--principal-assignment-name "kustoprincipal1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /AttachedDatabaseConfigurations/get/KustoAttachedDatabaseConfigurationsListByCluster
    def test_attached_database_configuration_list(self):
        self.cmd('az kusto attached-database-configuration list '
                 '--cluster-name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /AttachedDatabaseConfigurations/get/AttachedDatabaseConfigurationsGet
    def test_attached_database_configuration_show(self):
        self.cmd('az kusto attached-database-configuration show '
                 '--name "attachedDatabaseConfigurations1" '
                 '--cluster-name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /AttachedDatabaseConfigurations/put/AttachedDatabaseConfigurationsCreateOrUpdate
    def test_attached_database_configuration_create(self):
        self.cmd('az kusto attached-database-configuration create '
                 '--name "attachedDatabaseConfigurations1" '
                 '--cluster-name "kustoclusterrptest4" '
                 '--location "westus" '
                 '--cluster-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.Kusto/Clusters/KustoClusterLeader" '
                 '--database-name "kustodatabase" '
                 '--default-principals-modification-kind "Union" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /AttachedDatabaseConfigurations/delete/AttachedDatabaseConfigurationsDelete
    def test_attached_database_configuration_delete(self):
        self.cmd('az kusto attached-database-configuration delete -y '
                 '--name "attachedDatabaseConfigurations1" '
                 '--cluster-name "kustoclusterrptest4" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/get/KustoDatabasesListByCluster
    def test_data_connection_list(self):
        self.cmd('az kusto data-connection list '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/get/KustoDataConnectionsGet
    def test_data_connection_show(self):
        self.cmd('az kusto data-connection show '
                 '--cluster-name "kustoclusterrptest4" '
                 '--name "DataConnections8" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/put/KustoDataConnectionsCreateOrUpdate
    def test_data_connection_event_hub_create(self):
        self.cmd('az kusto data-connection event-hub create '
                 '--cluster-name "kustoclusterrptest4" '
                 '--name "DataConnections8" '
                 '--database-name "KustoDatabase8" '
                 '--location "westus" '
                 '--consumer-group "testConsumerGroup1" '
                 '--event-hub-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/patch/KustoDataConnectionsUpdate
    def test_data_connection_event_hub_update(self):
        self.cmd('az kusto data-connection event-hub update '
                 '--cluster-name "kustoclusterrptest4" '
                 '--name "DataConnections8" '
                 '--database-name "KustoDatabase8" '
                 '--location "westus" '
                 '--consumer-group "testConsumerGroup1" '
                 '--event-hub-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/delete/KustoDataConnectionsDelete
    def test_data_connection_delete(self):
        self.cmd('az kusto data-connection delete -y '
                 '--cluster-name "kustoclusterrptest4" '
                 '--name "kustoeventhubconnection1" '
                 '--database-name "KustoDatabase8" '
                 '--resource-group "kustorptest"')

    # EXAMPLE: /DataConnections/post/KustoDataConnectionValidation
    def test_data_connection_event(self):
        self.cmd('az kusto data-connection event-hub data-connection-validation '
                 '--cluster-name "kustoclusterrptest4" '
                 '--database-name "KustoDatabase8" '
                 '--name "DataConnections8" '
                 '--consumer-group "testConsumerGroup1" '
                 '--event-hub-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" '
                 '--resource-group "kustorptest"')
