from prettyconf import config


class Settings:
    EMAIL_USER = config("EMAIL_USER", default="")
    EMAIL_PASSWORD = config("EMAIL_PASSWORD", default="")
    EMAIL_HOST = config("EMAIL_HOST", default="")
    ID_SHEETS = config("ID_SHEETS", default="")
    SHEETS_SCOPE = config("SHEETS_SCOPE", default="")
    SHEETS_TAB = config("SHEETS_TAB", default="")
    JSON_KEY_SHEETS = config("JSON_KEY_SHEETS", default="")
    CRITERIA = config("CRITERIA", default="")
    CRITERIA_TO_SEARCH = config("CRITERIA_TO_SEARCH", default="")


settings = Settings()
