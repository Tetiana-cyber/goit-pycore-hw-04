def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Файл пошкоджено або має неправильний формат даних: {path}")
        return []

    
if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)