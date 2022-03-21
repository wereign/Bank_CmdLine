from csv import reader, writer
from file import handler
reader,writer = handler.reader,handler.writer
x = ['accounts.bin','bank.bin','history.bin','new.bin','pay.bin']
for _ in x:
    writer({},_)
    print(reader(_))


