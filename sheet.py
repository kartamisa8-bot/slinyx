import gspread


# Authenticate with your Google Sheets API credentials
gc = gspread.service_account(filename='./data/credentials.json')

# Open the desired spreadsheet and worksheet
spreadsheet = gc.open_by_url(url="https://docs.google.com/spreadsheets/d/1yP2EXq4ijU98LTJfpDPZTv22j8TDj4puD3mNeVyVGj4/edit?usp=sharing")
worksheet = spreadsheet.worksheet("Учётность состава")  # assuming it's the first worksheet

# Find the row index of "Старшая Администрация" section
start_index = worksheet.find(" Старшая Администрация").row

# Find the row index of the last row in "Старшая Администрация" section
end_index =worksheet.find(" Старшая Администрация").row -1

# Specify the row you want to move
source_row_index = start_index + 1  # Assuming you want to move the first row in "Старшая Администрация" section

# Copy the data from the source row
source_row_values = worksheet.row_values(source_row_index)

# Insert a new row at the end of "Руководство" section
worksheet.insert_row(source_row_values, index=end_index)

# Delete the original row
#worksheet.delete_row(source_row_index + 1)  # Adding 1 because row index starts from 1, not 0

# vk_hyperlink = '=HYPERLINK("' + vk + '", "VK")' if vk else ""
# discord_hyperlink = '=HYPERLINK("' + str(discord) + '", "Discord")' if discord else ""
# forum_hyperlink = '=HYPERLINK("' + forum + '", "Forum")' if forum else ""