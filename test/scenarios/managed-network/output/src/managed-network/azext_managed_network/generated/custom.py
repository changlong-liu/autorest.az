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
# pylint: disable=unused-argument

from azure.cli.core.util import sdk_no_wait


def managed_network_mn_list(client,
                            resource_group_name=None,
                            top=None,
                            skiptoken=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             top=top,
                                             skiptoken=skiptoken)
    return client.list_by_subscription(top=top,
                                       skiptoken=skiptoken)


def managed_network_mn_create(client,
                              resource_group_name,
                              managed_network_name,
                              managed_network):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   managed_network_name=managed_network_name,
                                   location=managed_network['location'],
                                   tags=managed_network['tags'],
                                   management_groups=managed_network['management_groups'],
                                   subscriptions=managed_network['subscriptions'],
                                   virtual_networks=managed_network['virtual_networks'],
                                   subnets=managed_network['subnets'])


def managed_network_mn_update(client,
                              resource_group_name,
                              managed_network_name,
                              tags=None):
    parameters = {}
    parameters['tags'] = tags
    return client.begin_update(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name,
                               parameters=parameters)


def managed_network_mn_delete(client,
                              resource_group_name,
                              managed_network_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name)


def managed_network_mn_show_modify(client,
                                   resource_group_name,
                                   managed_network_name):
    return client.get_modify(resource_group_name=resource_group_name,
                             managed_network_name=managed_network_name)


def managed_network_mn_scope_assignment_list(client,
                                             scope):
    return client.list(scope=scope)


def managed_network_mn_scope_assignment_show(client,
                                             scope,
                                             scope_assignment_name):
    return client.get(scope=scope,
                      scope_assignment_name=scope_assignment_name)


def managed_network_mn_scope_assignment_create(client,
                                               scope,
                                               scope_assignment_name,
                                               location,
                                               assigned_managed_network=None):
    parameters = {}
    parameters['location'] = location
    parameters['assigned_managed_network'] = assigned_managed_network
    parameters['scope_assignment_name_fake'] = scope_assignment_name
    return client.create_or_update(scope=scope,
                                   scope_assignment_name=scope_assignment_name,
                                   parameters=parameters)


def managed_network_mn_scope_assignment_update(instance,
                                               scope,
                                               scope_assignment_name,
                                               location,
                                               assigned_managed_network=None):
    if location is not None:
        instance.location = location
    if assigned_managed_network is not None:
        instance.assigned_managed_network = assigned_managed_network
    if scope_assignment_name is not None:
        instance.scope_assignment_name_fake = scope_assignment_name
    return instance


def managed_network_mn_scope_assignment_delete(client,
                                               scope,
                                               scope_assignment_name):
    return client.delete(scope=scope,
                         scope_assignment_name=scope_assignment_name)


def managed_network_mn_group_list(client,
                                  resource_group_name,
                                  managed_network_name,
                                  top=None,
                                  skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managed_network_mn_group_show(client,
                                  resource_group_name,
                                  managed_network_name,
                                  group_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_group_name=group_name)


def managed_network_mn_group_create(client,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    location,
                                    management_groups=None,
                                    subscriptions=None,
                                    virtual_networks=None,
                                    subnets=None,
                                    no_wait=False):
    managed_network_group = {}
    managed_network_group['location'] = location
    managed_network_group['kind'] = "Connectivity"
    managed_network_group['management_groups'] = management_groups
    managed_network_group['subscriptions'] = subscriptions
    managed_network_group['virtual_networks'] = virtual_networks
    managed_network_group['subnets'] = subnets
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_group_name=group_name,
                       managed_network_group=managed_network_group)


def managed_network_mn_group_update(instance,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    location,
                                    management_groups=None,
                                    subscriptions=None,
                                    virtual_networks=None,
                                    subnets=None,
                                    no_wait=False):
    if location is not None:
        instance.location = location
    if "Connectivity" is not None:
        instance.kind = "Connectivity"
    if management_groups is not None:
        instance.management_groups = management_groups
    if subscriptions is not None:
        instance.subscriptions = subscriptions
    if virtual_networks is not None:
        instance.virtual_networks = virtual_networks
    if subnets is not None:
        instance.subnets = subnets
    return instance


def managed_network_mn_group_delete(client,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_group_name=group_name)


def managed_network_managed_network_peering_policy_list(client,
                                                        resource_group_name,
                                                        managed_network_name,
                                                        top=None,
                                                        skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managed_network_managed_network_peering_policy_show(client,
                                                        resource_group_name,
                                                        managed_network_name,
                                                        policy_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_peering_policy_name=policy_name)


def managed_network_managed_network_peering_policy_hub_and_spoke_topology_create(client,
                                                                                 resource_group_name,
                                                                                 managed_network_name,
                                                                                 policy_name,
                                                                                 location,
                                                                                 managed_network_policy,
                                                                                 hub=None,
                                                                                 spokes=None,
                                                                                 mesh=None,
                                                                                 no_wait=False):
    managed_network_policy = {}
    managed_network_policy['location'] = location
    managed_network_policy['properties'] = {}
    managed_network_policy['properties']['type'] = 'HubAndSpokeTopology'
    managed_network_policy['properties']['hub'] = hub
    managed_network_policy['properties']['spokes'] = spokes
    managed_network_policy['properties']['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       managed_network_policy=managed_network_policy)


def managed_network_managed_network_peering_policy_mesh_topology_create(client,
                                                                        resource_group_name,
                                                                        managed_network_name,
                                                                        policy_name,
                                                                        location,
                                                                        managed_network_policy,
                                                                        hub=None,
                                                                        spokes=None,
                                                                        mesh=None,
                                                                        no_wait=False):
    managed_network_policy = {}
    managed_network_policy['location'] = location
    managed_network_policy['properties'] = {}
    managed_network_policy['properties']['type'] = 'MeshTopology'
    managed_network_policy['properties']['hub'] = hub
    managed_network_policy['properties']['spokes'] = spokes
    managed_network_policy['properties']['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       managed_network_policy=managed_network_policy)


def managed_network_managed_network_peering_policy_hub_and_spoke_topology_update(instance,
                                                                                 resource_group_name,
                                                                                 managed_network_name,
                                                                                 policy_name,
                                                                                 location,
                                                                                 hub=None,
                                                                                 spokes=None,
                                                                                 mesh=None,
                                                                                 no_wait=False):
    if location is not None:
        instance.location = location
    instance.properties.type = 'HubAndSpokeTopology'
    if hub is not None:
        instance.properties.hub = hub
    if spokes is not None:
        instance.properties.spokes = spokes
    if mesh is not None:
        instance.properties.mesh = mesh
    return instance


def managed_network_managed_network_peering_policy_mesh_topology_update(instance,
                                                                        resource_group_name,
                                                                        managed_network_name,
                                                                        policy_name,
                                                                        location,
                                                                        hub=None,
                                                                        spokes=None,
                                                                        mesh=None,
                                                                        no_wait=False):
    if location is not None:
        instance.location = location
    instance.properties.type = 'MeshTopology'
    if hub is not None:
        instance.properties.hub = hub
    if spokes is not None:
        instance.properties.spokes = spokes
    if mesh is not None:
        instance.properties.mesh = mesh
    return instance


def managed_network_managed_network_peering_policy_delete(client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          policy_name,
                                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name)
