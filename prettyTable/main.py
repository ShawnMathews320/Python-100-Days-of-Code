from prettytable import PrettyTable

table = PrettyTable()  # prettyTable object named table

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'r'
print(table)
