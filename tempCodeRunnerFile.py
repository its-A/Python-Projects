with open("r/Users/eugeniaportillo/Library/Mobile\ Documents/com\~apple\~TextEdit/Documents/raw_sales.csv.txt", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("Header:", header)
    print("\nRaw rows:\n")
    for row in reader:
        print(row)