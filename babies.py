import re

html_file = open('baby1990.html', 'r')
content = html_file.read()
year_match = re.search(r'<h3 align="center">Popularity in (\d\d\d\d)</h3>', content)
if year_match:
    year = year_match.group(1)
print(year)

ranks_bnames_gnames = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', content)
print(ranks_bnames_gnames[:20])
