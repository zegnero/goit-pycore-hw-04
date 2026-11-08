from pathlib import Path

def get_cats_info(path):
    cats = []
    try:
         with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                 continue
            
 
                id, name, age = line.split(",")
            
                cat = {
                    "id": id,
                    "name": name,
                    "age": int(age)
                }
                cats.append(cat)
            return cats
    except FileNotFoundError:
       print(f"Файл за напрямком '{path}' не знайдено")
    except UnicodeDecodeError:
       print("Помилка кодування файлу")
    except OSError as error:
       print(f"Помилка під час читанні")
       return 0 , 0
base_dir = Path(__file__).resolve().parent
file_path = base_dir / "cats_file.txt"
cats_info = get_cats_info(file_path)
print(cats_info)