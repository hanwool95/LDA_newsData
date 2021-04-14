import csv, codecs


title_only = []

full_content_only = []

with codecs.open('full_data.csv', 'r') as f:
    rdr = csv.reader(f)
    next(rdr)
    for line in rdr:
        title_only.append(line[1])
        full_content_only.append(line[5])

f = open("full_content_only.txt", 'w')
for line in full_content_only:
    data = line + "\n"
    f.write(data)
f.close()

f = open("title_only.txt", 'w')
for line in title_only:
    data = line + "\n"
    f.write(data)
f.close()