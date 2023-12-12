import requests
from requests.auth import HTTPBasicAuth
import json
import asyncio
import configparser
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
from graph import Graph

async def main():
    print('Python Graph Tutorial\n')

    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    await greet_user(graph)

    choice = -1

    while choice != 0:
        print('Please choose one of the following options:')
        print('0. Exit')
        print('1. Display access token')
        print('2. List my inbox')
        print('3. Send mail')
        print('4. Make a Graph call')

        try:
            choice = int(input())
        except ValueError:
            choice = -1

        try:
            if choice == 0:
                print('Goodbye...')
            elif choice == 1:
                await display_access_token(graph)
            elif choice == 2:
                await list_inbox(graph)
            elif choice == 3:
                await send_mail(graph)
            elif choice == 4:
                await make_graph_call(graph)
            else:
                print('Invalid choice!\n')
        except ODataError as odata_error:
            print('Error:')
            if odata_error.error:
                print(odata_error.error.code, odata_error.error.message)

#     # Erhalten Sie ein Token von Azure AD
#     token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
#     token_data = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'resource': 'https://graph.microsoft.com',
#     }
#     token_r = requests.post(token_url, data=token_data)
#     token = token_r.json().get('access_token')
#
#     # Rufen Sie Kalendereinträge ab
#
#     calendar_url = f'https://graph.microsoft.com/v1.0/users/{user_email}/calendar/events'
#     headers = {
#         'Authorization': f'Bearer {token}',
#         'Content-Type': 'application/json',
#     }
#
#     calendar_r = requests.get(calendar_url, headers=headers)
#     calendar_entries = calendar_r.json()
#
#     # Ausgabe der Kalendereinträge
#     for entry in calendar_entries.get('value', []):
#         print(f"Titel: {entry.get('subject')}")
#         print(f"Startzeit: {entry.get('start', {}).get('dateTime')}")
#         print(f"Endzeit: {entry.get('end', {}).get('dateTime')}")
#         print("------")
#
#
# if __name__ == '__main__':
#     hotmail()
#     print('test')
