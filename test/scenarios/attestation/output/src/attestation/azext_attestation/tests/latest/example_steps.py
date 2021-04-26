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


# EXAMPLE: AttestationProviders_Create
@try_manual
def step_create_provider(test, checks):
    if checks is None:
        checks = []
    test.cmd('az attestation create-provider '
             '--resource-group "{resourceGroupName}" '
             '--provider-name "myattestationprovider"',
             checks=checks)


# EXAMPLE: AttestationProviders_Update
@try_manual
def step_attestation_provider_update(test, checks):
    if checks is None:
        checks = []
    test.cmd('az attestation attestation-provider update '
             '--resource-group "{resourceGroupName}" '
             '--provider-name "myattestationprovider" '
             '--tags Property1="Value1" Property2="Value2" Property3="Value3"',
             checks=checks)
