from prettytable import PrettyTable
table=PrettyTable()
table.add_column("S.No",[1,2,3,4,5])
table.add_column("Name",["Alisha","Jenny","Natty","Julie","Alice"])
table.add_row([6,"Yunjin"])
table.align="l"
print(table)