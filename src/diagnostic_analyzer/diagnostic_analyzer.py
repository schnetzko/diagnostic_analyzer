file_path = "../../tests/integration/ATE_diagnostic.log"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

