
def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(',')
                total += int(salary)
                count += 1
        if count == 0:
            return 0, 0
        average = total / count
        return total, average
    except FileNotFoundError:
        print(f"Файлу по напрямку '{path}' не знайдено.")
        return 0, 0 
total, average = total_salary("/Users/artyr./My repo/first-repo-for-prcts/py-homework2/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
