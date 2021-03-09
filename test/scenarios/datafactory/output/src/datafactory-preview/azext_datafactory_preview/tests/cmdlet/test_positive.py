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

    # EXAMPLE: /Factories/get/Factories_ListByResourceGroup
    def test_list2(self):
        self.cmd('az datafactory list '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/get/Factories_List
    def test_list(self):
        self.cmd('az datafactory list')

    # EXAMPLE: /Factories/get/Factories_Get
    def test_show(self):
        self.cmd('az datafactory show '
                 '--name "myFactory" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/put/Factories_CreateOrUpdate
    def test_create(self):
        self.cmd('az datafactory create '
                 '--location "East US" '
                 '--zones "earth" "moon" '
                 '--name "myFactory" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/patch/Factories_Update
    def test_update(self):
        self.cmd('az datafactory update '
                 '--name "myFactory" '
                 '--tags exampleTag="exampleValue" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/delete/Factories_Delete
    def test_delete(self):
        self.cmd('az datafactory delete -y '
                 '--name "myFactory" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/post/Factories_ConfigureFactoryRepo
    def test_configure_factory_repo(self):
        self.cmd('az datafactory configure-factory-repo '
                 '--factory-resource-id "/subscriptions/12345678-1234-1234-1234-12345678abc/resourceGroups/myResourceGroup/providers/Microsoft.DataFactory/factories/myFactory" '
                 '--factory-vsts-configuration "FactoryVSTSConfiguration" "project" "" "ADF" "repo" "/" "master" '
                 '--location-id "East US"')

    # EXAMPLE: /Factories/post/Factories_GetDataPlaneAccess
    def test_get_data_plane_access(self):
        self.cmd('az datafactory get-data-plane-access '
                 '--name "myFactory" '
                 '--access-resource-path "" '
                 '--expire-time "2018-11-10T09:46:20.2659347Z" '
                 '--permissions "r" '
                 '--profile-name "DefaultProfile" '
                 '--start-time "2018-11-10T02:46:20.2659347Z" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Factories/post/Factories_GetGitHubAccessToken
    def test_get_git_hub_access_token(self):
        self.cmd('az datafactory get-git-hub-access-token '
                 '--name "myFactory" '
                 '--git-hub-access-code "some" '
                 '--git-hub-access-token-base-url "some" '
                 '--git-hub-client-id "some" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Triggers/get/Triggers_ListByFactory
    def test_trigger_list(self):
        self.cmd('az datafactory trigger list '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Triggers/get/Triggers_Get
    def test_trigger_show(self):
        self.cmd('az datafactory trigger show '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/put/Triggers_Create
    def test_trigger_create(self):
        self.cmd('az datafactory trigger create '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--properties "{{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{{\\"parameters\\":{{\\"OutputBlobNameList\\":[\\"exampleoutput.csv\\"]}},\\"pipelineReference\\":{{\\"type\\":\\"PipelineReference\\",\\"referenceName\\":\\"examplePipeline\\"}}}}],\\"typeProperties\\":{{\\"recurrence\\":{{\\"endTime\\":\\"2018-06-16T00:55:13.8441801Z\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39:13.8441801Z\\",\\"timeZone\\":\\"UTC\\"}}}}}}" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/put/Triggers_Update
    def test_trigger_update(self):
        self.cmd('az datafactory trigger update '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--description "Example description" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/delete/Triggers_Delete
    def test_trigger_delete(self):
        self.cmd('az datafactory trigger delete -y '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/post/Triggers_GetEventSubscriptionStatus
    def test_trigger_get_event_subscription_status(self):
        self.cmd('az datafactory trigger get-event-subscription-status '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/post/Triggers_QueryByFactory
    def test_trigger_query_by_factory(self):
        self.cmd('az datafactory trigger query-by-factory '
                 '--factory-name "myFactory" '
                 '--parent-trigger-name "myTrigger" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /Triggers/post/Triggers_Start
    def test_trigger_start(self):
        self.cmd('az datafactory trigger start '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/post/Triggers_Stop
    def test_trigger_stop(self):
        self.cmd('az datafactory trigger stop '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/post/Triggers_SubscribeToEvents
    def test_trigger_subscribe_to_event(self):
        self.cmd('az datafactory trigger subscribe-to-event '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /Triggers/post/Triggers_UnsubscribeFromEvents
    def test_trigger_unsubscribe_from_event(self):
        self.cmd('az datafactory trigger unsubscribe-from-event '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup" '
                 '--name "myTrigger"')

    # EXAMPLE: /IntegrationRuntimes/get/IntegrationRuntimes_ListByFactory
    def test_integration_runtime_list(self):
        self.cmd('az datafactory integration-runtime list '
                 '--factory-name "myFactory" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/get/IntegrationRuntimes_Get
    def test_integration_runtime_show(self):
        self.cmd('az datafactory integration-runtime show '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/put/IntegrationRuntimes_Create
    def test_integration_runtime_self_hosted_create(self):
        self.cmd('az datafactory integration-runtime self-hosted create '
                 '--factory-name "myFactory" '
                 '--description "A selfhosted integration runtime" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/patch/IntegrationRuntimes_Update
    def test_integration_runtime_update(self):
        self.cmd('az datafactory integration-runtime update '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup" '
                 '--auto-update "Off" '
                 '--update-delay-offset "\\"PT3H\\""')

    # EXAMPLE: /IntegrationRuntimes/delete/IntegrationRuntimes_Delete
    def test_integration_runtime_delete(self):
        self.cmd('az datafactory integration-runtime delete -y '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetConnectionInfo
    def test_integration_runtime_get_connection_info(self):
        self.cmd('az datafactory integration-runtime get-connection-info '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetMonitoringData
    def test_integration_runtime_get_monitoring_data(self):
        self.cmd('az datafactory integration-runtime get-monitoring-data '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetStatus
    def test_integration_runtime_get_status(self):
        self.cmd('az datafactory integration-runtime get-status '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_ListAuthKeys
    def test_integration_runtime_list_auth_key(self):
        self.cmd('az datafactory integration-runtime list-auth-key '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_RegenerateAuthKey
    def test_integration_runtime_regenerate_auth_key(self):
        self.cmd('az datafactory integration-runtime regenerate-auth-key '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--key-name "authKey2" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_RemoveLinks
    def test_integration_runtime_remove_link(self):
        self.cmd('az datafactory integration-runtime remove-link '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--linked-factory-name "exampleFactoryName-linked" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Start
    def test_integration_runtime_start(self):
        self.cmd('az datafactory integration-runtime start '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime2" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Stop
    def test_integration_runtime_stop(self):
        self.cmd('az datafactory integration-runtime stop '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime2" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_SyncCredentials
    def test_integration_runtime_sync_credentials(self):
        self.cmd('az datafactory integration-runtime sync-credentials '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Upgrade
    def test_integration_runtime_upgrade(self):
        self.cmd('az datafactory integration-runtime upgrade '
                 '--factory-name "myFactory" '
                 '--name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')

    # EXAMPLE: /datafactory linked-integration-runtime/post/IntegrationRuntimes_CreateLinkedIntegrationRuntime
    def test_linked_integration_runtime_create(self):
        self.cmd('az datafactory linked-integration-runtime create '
                 '--name "myDatafactoryLinkedIntegrationRuntime" '
                 '--data-factory-location "West US" '
                 '--data-factory-name "e9955d6d-56ea-4be3-841c-52a12c1a9981" '
                 '--subscription-id "061774c7-4b5a-4159-a55b-365581830283" '
                 '--factory-name "myFactory" '
                 '--integration-runtime-name "myIntegrationRuntime" '
                 '--resource-group "myResourceGroup"')
