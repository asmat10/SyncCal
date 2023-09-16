from controller.googleWebclient import get_calendar_entries
from service.importer import importer_service

if __name__ == '__main__':
    calendar_entries = get_calendar_entries()
    importer_service(calendar_entries)