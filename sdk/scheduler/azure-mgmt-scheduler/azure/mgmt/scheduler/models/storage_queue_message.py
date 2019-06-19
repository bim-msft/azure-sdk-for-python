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


class StorageQueueMessage(Model):
    """StorageQueueMessage.

    :param storage_account: Gets or sets the storage account name.
    :type storage_account: str
    :param queue_name: Gets or sets the queue name.
    :type queue_name: str
    :param sas_token: Gets or sets the SAS key.
    :type sas_token: str
    :param message: Gets or sets the message.
    :type message: str
    """

    _attribute_map = {
        'storage_account': {'key': 'storageAccount', 'type': 'str'},
        'queue_name': {'key': 'queueName', 'type': 'str'},
        'sas_token': {'key': 'sasToken', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageQueueMessage, self).__init__(**kwargs)
        self.storage_account = kwargs.get('storage_account', None)
        self.queue_name = kwargs.get('queue_name', None)
        self.sas_token = kwargs.get('sas_token', None)
        self.message = kwargs.get('message', None)