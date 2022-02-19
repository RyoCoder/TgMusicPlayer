from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQBnuUk2GPUnEz_NWmINXLKmIirfHwWoJUKZ3ZyIvQJsHJzY04gXEK4IRDqaV9Av6IOxzEgJG7gcgqKyAUg1lnQRq-b9vM-onm5Sd-BYBxYaAQ3qk-bVt-Zy_m4jAfibbV82Efcav12etwJ4sTTqHw-GWwsu9OBtkvnMVsun8l5oFdsg6iTDa0aetG7_rJrVJD1BJmewChYfEFUIzQZT9xce4wc9FZ4XaC4EVBRuzyW8XLrme_bvnkl1MI4HWkxqvbkzfe_lRV_iehPdSObPDmZjQnDLaweN7-YFSU4tSrMPcPoPDrjCyueLd8XNgISAa9FJEpQpe42advQn-Vv62uuUAAAAAGzwvKoA")
BOT_TOKEN = getenv("BOT_TOKEN", "1848996908:AAHLepd1iLUlp8qX2ABMk2TVFHIKRWb5yIs")

API_ID = int(getenv("API_ID". "4231409"))
API_HASH = getenv("API_HASH", "c1828f4f9181fb4d9b6deb95e5f05862")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5274723038").split()))

