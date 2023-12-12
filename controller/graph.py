from configparser import SectionProxy
from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.item.user_item_request_builder import UserItemRequestBuilder
from msgraph.generated.users.item.mail_folders.item.messages.messages_request_builder import (
    MessagesRequestBuilder)
from msgraph.generated.users.item.send_mail.send_mail_post_request_body import (
    SendMailPostRequestBody)
from msgraph.generated.models.message import Message
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.models.email_address import EmailAddress


class Graph:
    settings: SectionProxy
    device_code_credential: DeviceCodeCredential
    user_client: GraphServiceClient

    # Setzen Sie Ihre Anwendungsdaten hier ein
    # client_id = '2553003f-48eb-48c0-abde-ccefbb577a76'
    # client_secret = 'pcn8Q~KigJFRLAIoq2eKVRYzmGL7eX.juyqaHcKg'
    # tenant_id = 'cda893fd-aed1-4db3-835a-d438e5054c12'
    # user_email = 'asmat-simab@hotmail.com'
    # graphUserScopes = User.Read Mail.Read Mail.Send
    def __init__(self, config: SectionProxy):
        self.settings = config
        client_id = self.settings['clientId']
        tenant_id = self.settings['tenantId']
        graph_scopes = self.settings['graphUserScopes'].split(' ')

        self.device_code_credential = DeviceCodeCredential(client_id, tenant_id=tenant_id)
        self.user_client = GraphServiceClient(self.device_code_credential, graph_scopes)


async def get_user_token(self):
    graph_scopes = self.settings['graphUserScopes']
    access_token = self.device_code_credential.get_token(graph_scopes)
    return access_token.token
