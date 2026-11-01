def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(",")
                total += int(salary)
                count += 1
            average = total / count if count else 0
            return total, average
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except ValueError:
        print(f"Файл пошкоджено або має неправильний формат даних: {path}")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")