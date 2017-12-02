import win32clipboard as clipboard

clipboard.OpenClipboard()

data = clipboard.GetClipboardData()
lines = data.split("\n")

lists = []

for line in lines:
    line = line.replace("\r", "")
    strList = line.split("\t")
    intList = []
    for s in strList:
        intList.append(int(s))
    lists.append(intList)

clipboard.EmptyClipboard()
clipboard.SetClipboardText(str(lists))

clipboard.CloseClipboard()