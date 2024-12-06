from settings import settings
from clients import GoogleSheetClient
from imapclient import IMAPClient

import imaplib
import email
import pandas as pd
import re

def connect_imap() -> IMAPClient:
    try:
        server = IMAPClient(settings.EMAIL_HOST)
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        return server
    except imaplib.IMAP4.error as e:
        print(f"Error on connecting to IMAP: {e}")
        exit()

def extract_contact_info(body: str) -> dict:
    name_match = re.search(r'Name: (.*?)<br>', body)
    email_match = re.search(r'E-mail: (.*?)<br>', body)
    phone_match = re.search(r'Telefone: (.*?)<br>', body)

    if email_match and phone_match:
        return {
            "nome": name_match.group(1) if name_match else "",
            "email": email_match.group(1),
            "telefone": phone_match.group(1)
        } 
    return None
    
def main() -> None:
    to_sheets = []

    server = connect_imap()
    server.select_folder('INBOX')

    criteria = [settings.CRITERIA, settings.CRITERIA_TO_SEARCH]
    messages = server.search(criteria)

    if not messages:
        print("No messages found")
        return 
        
    for _, data in server.fetch(messages, "RFC822").items():
        msg = email.message_from_bytes(data[b"RFC822"])
        
        body = msg.get_payload(decode=True).decode() if not msg.is_multipart() else ""
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                body = part.get_payload(decode=True).decode()
        
        contact_info = extract_contact_info(body)
        if contact_info:
            to_sheets.append(contact_info)
    
    google_sheets_client = GoogleSheetClient(
        id_sheets=settings.ID_SHEETS, sheets_tab=settings.SHEETS_TAB
    )

    if to_sheets:
        df = pd.DataFrame(to_sheets)
        result = google_sheets_client.update_all_sheet(df)
        print(result)

main()