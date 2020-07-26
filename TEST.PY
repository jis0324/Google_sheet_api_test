import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = [
  'https://spreadsheets.google.com/feeds',
  'https://www.googleapis.com/auth/drive',
]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret1.json', scope)
client = gspread.authorize(creds)

sheet = client.open("TEST of HubSpot - IC On-Boarding Form Submissions").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
index = len(list_of_hashes) + 2
sheet.insert_row(row, index)

# gspread.exceptions.APIError: {
#   'errors': [
#       {
#         'domain': 'usageLimits', 
#         'reason': 'accessNotConfigured', 
#         'message': 'Access Not Configured. Drive API has not been used in project 119121033793 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=119121033793 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.', 
#         'extendedHelp': 'https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=119121033793'
#       }
#     ], 
#   'code': 403, 
#   'message': 'Access Not Configured. Drive API has not been used in project 119121033793 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=119121033793 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.'
# }