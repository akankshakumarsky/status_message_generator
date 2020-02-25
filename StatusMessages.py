import csv
from itertools import islice

messages = []
provider_id = "bbc.co.uk"
with open('C:/Users/AKR18/OneDrive - Sky/Documents/Status Messages_Script.csv','rt') as fd:
    for row in islice(csv.reader(fd), 1, None):
        # print(f"{row[0]} {row[1]}")
        messages.append(f"""<?xml version="1.0" encoding="UTF-8"?>
<StatusMessage conversationID="123456789"
 assetID="GLAA2020000000000018"
 providerID="{provider_id}"
 xmlns="URN:NNDS:VAM:STATUS"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <message>
                <realm>{row[0]}</realm>
                <code>{row[1]}</code>
                <levelType>{row[2]}</levelType>
                <shortText>{row[3]}</shortText>
                <longText>{row[4]}</longText>
                <messageDateTime>2020-02-18T06:30:03</messageDateTime>
        </message>
</StatusMessage>\n""")

for i in range(len(messages)):
     f = open(f"C:/Users/AKR18/OneDrive - Sky/Documents/Status Messages{i}.xml", "w")
     f.write(messages[i])
     f.close()


