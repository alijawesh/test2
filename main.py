import csv
import requests
import pandas as pd

with open('Bilag_2_-_CVR_Datast.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    CVRdata = []
    for row in csvreader:
        CVRdata.append(row)

theLinkForCVR = []
df = pd.DataFrame()

for x in CVRdata:
    CVR = x[0][2:]

    theCVRLink = 'http://cvrapi.dk/api?search=xxxxxxxx&country=dk'
    theCVRLink = theCVRLink.replace('xxxxxxxx', str(CVR))
    theLinkForCVR.append(theCVRLink)

    r = requests.get(theCVRLink)
    myData = r.json()
    indices = [1, 2, 3, 4, 5, 6, 7, 8, 9,11, 12, 13, 14, 15]
    selected_data = {k: v for i, (k, v) in enumerate(myData.items()) if i in indices}

    df = pd.concat([df, pd.DataFrame(selected_data, index=[0])], ignore_index=True)


df.to_csv('CVR_Datast.csv', index=False)
print(df)