# install pkgs gspread, pyopenssl, oauth2client, tabulate
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tabulate import tabulate

# scope of access
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# variable to store info from JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name("idp-2022-leaderboard-0efee2c8a655.json", scope)

# make a var to interface with sheets
googleSheet = gspread.authorize(credentials)

index = 0 # we want to use sheet 1
wks = googleSheet.open("TestSheet").get_worksheet(index)

# test input
username = input("What is your name: ")
score = int(input("What is your score: "))

# add new row to google sheet
wks.append_row([username, score])

index = 1 # changes sheet to sheet 2
wks = googleSheet.open("TestSheet").get_worksheet(index)
leaderboard = []
for i in range (2,7,1):
    leaderboard.append(wks.row_values(i))

headers = wks.row_values(1)

print(tabulate(leaderboard, headers, tablefmt="github"))