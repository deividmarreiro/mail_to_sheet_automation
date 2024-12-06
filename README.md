# Mail to Sheet Automation

This project aims to automate the extraction of information from emails and insert the data into a Google Sheets spreadsheet. It collects contact data from received emails and sends it to a specified tab in a spreadsheet.

## System Requirements

- Python 3.13 or higher

- Poetry for dependency management

## Installation

### Clone the repository to your local environment:

```sh
# https
git clone https://github.com/deividmarreiro/mail_to_sheet_automation.git
# or ssh
git clone git@github.com:deividmarreiro/mail_to_sheet_automation.git
cd mail-to-sheet-automation
```

Install Poetry if you haven't done so already.

Install the project dependencies with Poetry:

```sh
poetry install
```

### Configuration

The project uses environment variables for configuring credentials and sensitive information. You can use a .env file for setting these variables, generated from a local.env file.

Create a `.env` file from the `local.env` template provided in the project root:

```sh
cp local.env .env
```

Edit the `.env` file and fill in the required variables:

```yaml
GMAIL_USER=email_user
GMAIL_PASSWORD=email_password
EMAIL_HOST=email_host
ID_SHEETS=id_sheets
SHEETS_SCOPE=https://spreadsheets.google.com/feeds
SHEETS_TAB=tab_name
JSON_KEY_SHEETS='{}'
CRITERIA=criteria
CRITERIA_TO_SEARCH=criteria_to_search
```

### Explanation of Variables

**GMAIL_USER**: The email address used for IMAP authentication.

**GMAIL_PASSWORD**: The email password for IMAP authentication (consider using an app password for added security).

**EMAIL_HOST**: Email server host (e.g., imap.gmail.com).

**ID_SHEETS**: The ID of the Google Sheets document to be updated.

**SHEETS_SCOPE**: Google Sheets permission scope (default: https://spreadsheets.google.com/feeds).

**SHEETS_TAB**: Name of the sheet tab to be used.

**JSON_KEY_SHEETS**: The credentials in JSON format for accessing Google Sheets (must be configured as a string).

**CRITERIA and CRITERIA_TO_SEARCH**: Criteria for searching emails (e.g., sender or subject to identify the correct emails).

### Running the Project

Load the environment variables:

If using dotenv, the `.env` file will be loaded automatically when starting the project.

Run the main script using Poetry:

```sh
poetry run python main.py
```

### Development

This project uses development tools to ensure code quality. You can run these tools using Poetry.

#### Linting and Formatting

```sh
# Ruff is used for linting and checking code style.
# To run Ruff you can use the commands from Makefile:

make lint && make format

```

### Project Structure

**main.py**: Contains the main script that handles email collection and updates the spreadsheet.

**clients.py**: Includes the GoogleSheetClient class that manages communication with Google Sheets.

**settings.py**: Responsible for the project configuration, including loading environment variables.

License

This project is distributed under the MIT license. See the LICENSE file for more details.

