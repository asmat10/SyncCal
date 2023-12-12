import pymongo
from pymongo import MongoClient
from repository.dbConfig import db_connection_test

def save_to_mongodb(entry):
    # Hier den Code hinzufügen, um 'entry' in MongoDB zu speichern
    # Verwenden Sie dazu die MongoClient-Instanz und die entsprechende Datenbank und Sammlung in Ihrer MongoDB
    # Beispiel:
    # client = MongoClient("Ihre MongoDB URI")
    # db = client["Ihre Datenbank"]
    # collection = db["Ihre Sammlung"]
    # collection.insert_one(entry)

    client = MongoClient("mongodb+srv://admin:admin@cluster0.7mczdvg.mongodb.net/?retryWrites=true&w=majority")
    db = client["SyncCalDB"]
    collection = db["SyncCalCollection"]
    collection.insert_one(entry)
    pass

def importer_service(events):
    for event in events:
        print(events)
        for key, value in event.items():
            print(f"{key}: {value}")

    # Daten aus dem Kalender holen
    calendar_entries = []

    # Prints the start and name of the next 10 events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        summary = event['summary']
        location = event.get('location', '')
        creator_email = event['creator']['email']
        organizer_email = event['organizer']['email']
        eventId = event['id']
        status = event['status']
        htmlLink = event['htmlLink']

        calendar_entries.append({
            'Startzeit': start,
            'Endzeit': end,
            'Zusammenfassung': summary,
            'Ort': location,
            'Ersteller_Email': creator_email,
            'Organizer_Email': organizer_email,
            'Event_ID': eventId,
            'Status': status,
            'HTML_Link': htmlLink
        })

    for events in calendar_entries:
        print(f'__________________________ \n Startzeit: {events["Startzeit"]},\n Endzeit: {events["Endzeit"]},\n '
              f'Zusammenfassung: {events["Zusammenfassung"]},\n Ort: {events["Ort"]},\n Ersteller_Email: {events["Ersteller_Email"]},\n '
              f'Organizer_Email: {events["Organizer_Email"]},\n Event_ID: {events["Event_ID"]},\n Status: {events["Status"]},\n HTML_Link: {events["HTML_Link"]} \n'
              f' __________________________')
        print(calendar_entries)


        # Hier werden wir später die Liste zum speichern an die DB senden, vor erst starten wir damit nur den Ping test
        db_connection_test();
        save_to_mongodb(events)


