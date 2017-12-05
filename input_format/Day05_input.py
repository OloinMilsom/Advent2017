import win32clipboard as clipboard

clipboard.OpenClipboard()

data = clipboard.GetClipboardData()
lines = data.split("\n")

lists = []

for line in lines:
    line = line.replace("\r", "")
    lists.append(int(line))

clipboard.EmptyClipboard()
clipboard.SetClipboardText(str(lists))

clipboard.CloseClipboard()