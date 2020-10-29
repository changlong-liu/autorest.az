# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Factories/put/Factories_CreateOrUpdate
@try_manual
def step__factories_put_factories_createorupdate(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory create '
             '--location "East US" '
             '--zones "earth" '
             '--zones "moon" '
             '--name "{myFactory}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Factories/get/Factories_Get
@try_manual
def step__factories_get_factories_get(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory show '
             '--name "{myFactory}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Factories/get/Factories_List
@try_manual
def step__factories_get_factories_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Factories/get/Factories_ListByResourceGroup
@try_manual
def step__factories_get_factories_listbyresourcegroup(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Factories/patch/Factories_Update
@try_manual
def step__factories_patch_factories_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory update '
             '--name "{myFactory}" '
             '--tags exampleTag="exampleValue" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Factories/post/Factories_ConfigureFactoryRepo
@try_manual
def step__factories_post(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory configure-factory-repo '
             '--factory-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DataFacto'
             'ry/factories/{myFactory}" '
             '--factory-vsts-configuration account-name="ADF" collaboration-branch="master" last-commit-id="" '
             'project-name="project" repository-name="repo" root-folder="/" tenant-id="" '
             '--location-id "East US"',
             checks=checks)


# EXAMPLE: /Factories/post/Factories_GetDataPlaneAccess
@try_manual
def step__factories_post_factories_getdataplaneaccess(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory get-data-plane-access '
             '--name "{myFactory}" '
             '--access-resource-path "" '
             '--expire-time "2018-11-10T09:46:20.2659347Z" '
             '--permissions "r" '
             '--profile-name "DefaultProfile" '
             '--start-time "2018-11-10T02:46:20.2659347Z" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Factories/post/Factories_GetGitHubAccessToken
@try_manual
def step__factories_post2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory get-git-hub-access-token '
             '--name "{myFactory}" '
             '--git-hub-access-code "some" '
             '--git-hub-access-token-base-url "some" '
             '--git-hub-client-id "some" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/put/IntegrationRuntimes_Create
@try_manual
def step__integrationruntimes_put(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime self-hosted create '
             '--factory-name "{myFactory}" '
             '--description "A selfhosted integration runtime" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/get/IntegrationRuntimes_Get
@try_manual
def step__integrationruntimes_get(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime show '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/get/IntegrationRuntimes_ListByFactory
@try_manual
def step__integrationruntimes_get2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime list '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/patch/IntegrationRuntimes_Update
@try_manual
def step__integrationruntimes_patch(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime update '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}" '
             '--auto-update "Off" '
             '--update-delay-offset "\\"PT3H\\""',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_CreateLinkedIntegrationRuntime
@try_manual
def step__integrationruntimes_post(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime linked-integration-runtime create '
             '--name "bfa92911-9fb6-4fbe-8f23-beae87bc1c83" '
             '--data-factory-location "West US" '
             '--data-factory-name "e9955d6d-56ea-4be3-841c-52a12c1a9981" '
             '--subscription-id "061774c7-4b5a-4159-a55b-365581830283" '
             '--factory-name "{myFactory}" '
             '--integration-runtime-name "{myIntegrationRuntime}" '
             '--resource-group "{rg}" '
             '--subscription-id "12345678-1234-1234-1234-12345678abc"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetConnectionInfo
@try_manual
def step__integrationruntimes_post2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime get-connection-info '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetMonitoringData
@try_manual
def step__integrationruntimes_post3(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime get-monitoring-data '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_GetStatus
@try_manual
def step__integrationruntimes_post4(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime get-status '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_ListAuthKeys
@try_manual
def step__integrationruntimes_post5(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime list-auth-key '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_RegenerateAuthKey
@try_manual
def step__integrationruntimes_post6(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime regenerate-auth-key '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--key-name "authKey2" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_RemoveLinks
@try_manual
def step__integrationruntimes_post7(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime remove-link '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--linked-factory-name "exampleFactoryName-linked" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Start
@try_manual
def step__integrationruntimes_post8(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime start '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime2}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Stop
@try_manual
def step__integrationruntimes_post9(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime stop '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime2}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_SyncCredentials
@try_manual
def step__integrationruntimes_post10(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime sync-credentials '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/post/IntegrationRuntimes_Upgrade
@try_manual
def step__integrationruntimes_post11(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime upgrade '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /IntegrationRuntimes/delete/IntegrationRuntimes_Delete
@try_manual
def step__integrationruntimes_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory integration-runtime delete -y '
             '--factory-name "{myFactory}" '
             '--name "{myIntegrationRuntime}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Triggers/put/Triggers_Create
@try_manual
def step__triggers_put_triggers_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger create '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--properties "{{\\"type\\":\\"ScheduleTrigger\\",\\"pipelines\\":[{{\\"parameters\\":{{\\"OutputBlobNameL'
             'ist\\":[\\"exampleoutput.csv\\"]}},\\"pipelineReference\\":{{\\"type\\":\\"PipelineReference\\",\\"refere'
             'nceName\\":\\"examplePipeline\\"}}}}],\\"typeProperties\\":{{\\"recurrence\\":{{\\"endTime\\":\\"2018-06-'
             '16T00:55:13.8441801Z\\",\\"frequency\\":\\"Minute\\",\\"interval\\":4,\\"startTime\\":\\"2018-06-16T00:39'
             ':13.8441801Z\\",\\"timeZone\\":\\"UTC\\"}}}}}}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/put/Triggers_Update
@try_manual
def step__triggers_put_triggers_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger update '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--description "Example description" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/get/Triggers_Get
@try_manual
def step__triggers_get_triggers_get(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger show '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/get/Triggers_ListByFactory
@try_manual
def step__triggers_get_triggers_listbyfactory(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger list '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_GetEventSubscriptionStatus
@try_manual
def step__triggers_post(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger get-event-subscription-status '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_QueryByFactory
@try_manual
def step__triggers_post_triggers_querybyfactory(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger query-by-factory '
             '--factory-name "{myFactory}" '
             '--parent-trigger-name "{myTrigger}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_Start
@try_manual
def step__triggers_post_triggers_start(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger start '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_Stop
@try_manual
def step__triggers_post_triggers_stop(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger stop '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_SubscribeToEvents
@try_manual
def step__triggers_post_triggers_subscribetoevents(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger subscribe-to-event '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/post/Triggers_UnsubscribeFromEvents
@try_manual
def step__triggers_post_triggers_unsubscribefromevents(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger unsubscribe-from-event '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/delete/Triggers_Delete
@try_manual
def step__triggers_delete_triggers_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory trigger delete -y '
             '--factory-name "{myFactory}" '
             '--resource-group "{rg}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Factories/delete/Factories_Delete
@try_manual
def step__factories_delete_factories_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datafactory delete -y '
             '--name "{myFactory}" '
             '--resource-group "{rg}"',
             checks=checks)
