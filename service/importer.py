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


