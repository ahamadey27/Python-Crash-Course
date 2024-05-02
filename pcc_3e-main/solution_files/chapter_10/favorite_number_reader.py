from pathlib import Path
import json

path = Path('pcc_3e-main/solution_files/chapter_10/favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")