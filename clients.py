import json

import gspread
import pandas as pd
from gspread.client import Client
from gspread.spreadsheet import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials

from settings import settings


class GoogleSheetClient:
    def __init__(self, id_sheets: str, sheets_tab: str) -> None:
        self.scope = settings.SHEETS_SCOPE
        self.id_sheet = id_sheets
        self.sheet_tab = sheets_tab
        self.google_client = None

    def worksheet_authentication(self) -> Client:
        if self.google_client is None:
            credentials = ServiceAccountCredentials.from_json_keyfile_dict(
                json.loads(settings.JSON_KEY_SHEETS), self.scope
            )
            self.google_client = gspread.authorize(credentials)
        return self.google_client

    def get_spreadsheet(self) -> Spreadsheet:
        return self.worksheet_authentication().open_by_key(self.id_sheet)

    def get_by_sheets_tab(self, sheets_tab: str = None) -> pd.DataFrame:
        sheets_tab = sheets_tab or self.sheet_tab
        return pd.DataFrame(
            self.get_spreadsheet().worksheet(sheets_tab).get_all_records()
        )

    def update_all_sheet(self, new_data: pd.DataFrame) -> str:
        spreadsheet = self.get_spreadsheet()
        worksheet = spreadsheet.worksheet(self.sheet_tab)
        existing_records = worksheet.get_all_records()
        existind_data = (
            pd.DataFrame(existing_records)
            if existing_records
            else pd.DataFrame()
        )

        updated_data = pd.concat([existind_data, new_data], ignore_index=True)

        results = worksheet.update(
            [updated_data.columns.values.tolist()]
            + updated_data.values.tolist()
        )

        return f"Cells updated: {results['updatedCells']}"
