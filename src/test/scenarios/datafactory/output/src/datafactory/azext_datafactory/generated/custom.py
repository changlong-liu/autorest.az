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

from knack.util import CLIError


def datafactory_list(cmd, client,
                     resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def datafactory_show(cmd, client,
                     resource_group_name,
                     factory_name,
                     if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      if_none_match=if_none_match)


def datafactory_create(cmd, client,
                       resource_group_name,
                       factory_name,
                       if_match=None,
                       location=None,
                       tags=None,
                       identity=None,
                       factory_vsts_configuration=None,
                       factory_git_hub_configuration=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for repo_co'
                       'nfiguration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   if_match=if_match,
                                   location=location,
                                   tags=tags,
                                   identity=identity,
                                   repo_configuration=repo_configuration)


def datafactory_update(cmd, client,
                       resource_group_name,
                       factory_name,
                       tags=None,
                       identity=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         tags=tags,
                         identity=identity)


def datafactory_delete(cmd, client,
                       resource_group_name,
                       factory_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name)


def datafactory_configure_factory_repo(cmd, client,
                                       location_id,
                                       factory_resource_id=None,
                                       factory_vsts_configuration=None,
                                       factory_git_hub_configuration=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for repo_co'
                       'nfiguration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.configure_factory_repo(location_id=location_id,
                                         factory_resource_id=factory_resource_id,
                                         repo_configuration=repo_configuration)


def datafactory_get_data_plane_access(cmd, client,
                                      resource_group_name,
                                      factory_name,
                                      permissions=None,
                                      access_resource_path=None,
                                      profile_name=None,
                                      start_time=None,
                                      expire_time=None):
    return client.get_data_plane_access(resource_group_name=resource_group_name,
                                        factory_name=factory_name,
                                        permissions=permissions,
                                        access_resource_path=access_resource_path,
                                        profile_name=profile_name,
                                        start_time=start_time,
                                        expire_time=expire_time)


def datafactory_get_git_hub_access_token(cmd, client,
                                         resource_group_name,
                                         factory_name,
                                         git_hub_access_code,
                                         git_hub_access_token_base_url,
                                         git_hub_client_id=None):
    return client.get_git_hub_access_token(resource_group_name=resource_group_name,
                                           factory_name=factory_name,
                                           git_hub_access_code=git_hub_access_code,
                                           git_hub_client_id=git_hub_client_id,
                                           git_hub_access_token_base_url=git_hub_access_token_base_url)
