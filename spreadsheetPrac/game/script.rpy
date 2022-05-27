# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    
    # install pkgs gspread, pyopenssl, oauth2client, tabulate
    import gspread
    # import google.oauth2.credentials
    # import pyOpenSSL
    # import requests
    from oauth2client.service_account import ServiceAccountCredentials
    from tabulate import tabulate

    """def spreadsheetTest():
        URL = "https://script.google.com/macros/s/AKfycbzA1w5BMrhey6Pji3xhn7RbcxAQPuJt9NFPCqplmFrB3nDCseLE/exec"
            # Use requests to send the data.
        requests.post(
                URL,
                json={
                    # These are the fields to send.
                    'time' : totalTime,
                    'heartRate' : hRate,
                }, timeout=2.5)

    """
    def spreadsheetInc():
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
        username = user
        heartRate = hRate
        q1 = qu1


    # add new row to google sheet
        wks.append_row([username, heartRate, q1])

        index = 1 # changes sheet to sheet 2
        wks = googleSheet.open("TestSheet").get_worksheet(index)
        leaderboard = []
        for i in range (2,7,1):
            leaderboard.append(wks.row_values(i))

        headers = wks.row_values(1)

        print(tabulate(leaderboard, headers, tablefmt="github"))
        

label start:

    show eileen happy

    $ user = renpy.input("What is your name: ")
    $ user = renpy.strip(user)

    $ hRate = renpy.input("Enter your heart rate: ")
    $ hRate = renpy.strip(hRate)

    $ qu1 = renpy.input("What did you like about the game: ")
    $ qu1 = renpy.strip(qu1)

    $ spreadsheetTest()

    return