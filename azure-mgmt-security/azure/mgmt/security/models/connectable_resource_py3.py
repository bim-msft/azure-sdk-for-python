# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnectableResource(Model):
    """Describes the allowed inbound and outbound traffic of an Azure resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The Azure resource id
    :vartype id: str
    :ivar inbound_connected_resources: The list of Azure resources that the
     resource has inbound allowed connection from
    :vartype inbound_connected_resources:
     list[~azure.mgmt.security.models.ConnectedResource]
    :ivar outbound_connected_resources: The list of Azure resources that the
     resource has outbound allowed connection to
    :vartype outbound_connected_resources:
     list[~azure.mgmt.security.models.ConnectedResource]
    """

    _validation = {
        'id': {'readonly': True},
        'inbound_connected_resources': {'readonly': True},
        'outbound_connected_resources': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'inbound_connected_resources': {'key': 'inboundConnectedResources', 'type': '[ConnectedResource]'},
        'outbound_connected_resources': {'key': 'outboundConnectedResources', 'type': '[ConnectedResource]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ConnectableResource, self).__init__(**kwargs)
        self.id = None
        self.inbound_connected_resources = None
        self.outbound_connected_resources = None
