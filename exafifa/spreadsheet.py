from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

from exafifa.const import SCOPES, SERVICE_ACCOUNT_FILE, SPREADSHEET_ID


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)


def spreadsheets_operations(operation, position, data=[[]]):
    """Reads, writes or deletes data from a spreadsheet."""

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        if operation == "read":
            result = (
                sheet.values()
                .get(spreadsheetId=SPREADSHEET_ID, range=position)
                .execute()
            )
            values = result.get("values", [])
            return values

        elif operation == "write":
            sheet.values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=position,
                valueInputOption="RAW",
                body={"values": data},
            ).execute()
            return "Exito!"

        elif operation == "delete":
            sheet.values().clear(
                spreadsheetId=SPREADSHEET_ID, range=position,
            ).execute()
            return "Deleted!"

    except HttpError as err:
        print(err)
        return "Error!"
