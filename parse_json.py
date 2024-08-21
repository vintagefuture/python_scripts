import json

input_file = "ZBOOKMARK.json"
output_file = "new_hackerfeed.html"

bookmarks_title = "Hacker News"

with open(input_file, "r") as file:
    jsonData = json.load(file)

with open(output_file, 'w') as file:
    file.write(f'<DL><DT><H3>{bookmarks_title}</H3>')
    for entry in jsonData:
        output_line = f'<DT><A HREF="{entry["ZURL"]}" ADD_DATE="{entry["ZTIME"]}">{entry["ZTITLE"]}</A></DT>\n'
        print(output_line)
        file.write(output_line)
    file.write('</DL>')
