#logan cannon
#9/17/2019
#character art
artist = input("Enter an Artist's Name →")
signature = str.format('''
+--------------------+
|        |>          |
|        |\          |
|        | \         |
|        |  \        |
|        |   \       |
|        |    \      |
|  \==============/  |
|   \____________/   |
|{0:^20}|
+--------------------+''',artist)
print(signature)
