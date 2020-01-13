import gspread
from oauth2client.service_account import ServiceAccountCredentials
from wikihow import wikihow_fetch


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("Speadsheet-90944d5c9155.json", scope)
gc = gspread.authorize(credentials)
h = 'Database'
wks = gc.open("%s" % h).sheet1


def wikiadd():
    for x in range(100):
        j = wikihow_fetch()
        wks.append_row([j[0], j[1]])



def removeblanks():
    while True:
        x = int(input())
        if not bool(wks.row_values(x)):
            wks.delete_row(x)

def deleterows():
    while True:
        x = input()
        if not bool(x):
            x = j
        if x == '.':
            x =j+1
        x = int(x)
        wks.delete_row(x)
        j = x

print(wks.get_all_records())
