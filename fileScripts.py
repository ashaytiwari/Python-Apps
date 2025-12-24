contents = ['Text 10', 'Text 20', 'Text 30']
fileNames = ['doc.txt', 'report.txt', 'content.txt']

for content, fileName in zip(contents, fileNames):
    file = open(f"files/{fileName}", "w")
    file.write(content)

print('Script Run Successfully!')