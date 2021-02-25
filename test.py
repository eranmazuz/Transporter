import pandas as pd


xl_file = pd.read_excel('H:\Project\Transporter\TestFiles\כפילות במספר אישי.xlsx',sheet_name=0)


for sheet_name in xl_file.sheet_names:
    a = xl_file.parse(sheet_name)
    print(a['מספר אישי'])
