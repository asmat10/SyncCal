from SyncCal.repository.dbConfig import db_connection_test
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
        summary = event['summary']
        calendar_entries.append({'Startzeit': start, 'Zusammenfassung': summary})

    for entry in calendar_entries:
        print(f'Startzeit: {entry["Startzeit"]}, Zusammenfassung: {entry["Zusammenfassung"]}')


        # Hier werden wir später die Liste zum speichern an die DB senden, vor erst starten wir damit nur den Ping test
        db_connection_test();