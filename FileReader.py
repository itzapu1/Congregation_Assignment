from googleapiclient.discovery import build
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/andya/Desktop/credits/creds.json'


class Reader:
    """The reading class will either read a document OR connect to google docs to read from repo;
    Many options and can be flexible"""

    def __init__(self):
        self.spreadsheet_id = '1vcn7qA_MGX3S5rkvjVk8M3Zu5WrbkO0iWR852xajro8'
        self.sheet_id = 0
        self.range_name = 'A1:E13'

        self.credentials = 'C:/Users/andya/Desktop/credits/credentials.json'

    def read_spreadsheet(self):
        with build('sheets', 'v4') as service:
            result = service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id,
                                                         range=self.range_name).execute()
            rows = result.get('values', [])
            print('{0} rows retrieved.'.format(len(rows)))

        return rows
        pass


file_read = Reader()
file_read.read_spreadsheet()
