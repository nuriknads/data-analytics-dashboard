import os
import subprocess
from datetime import datetime, timedelta
import random

# Начальная и конечная дата
start_date = datetime(2024, 8, 1)
end_date = datetime.now()

commit_count = 60  # количество коммитов
delta = (end_date - start_date) / commit_count
current_date = start_date

# список сообщений коммитов
messages = [
    "Added chart view",
    "Fixed data serialization bug",
    "Refactored dashboard API",
    "Updated README",
    "Improved query performance",
    "Added filtering feature",
    "Updated UI styling",
]

for i in range(commit_count):
    # создаём или изменяем dummy файл
    with open("dummy_file.txt", "a", encoding="utf-8") as f:
        f.write(f"Коммит {i+1} — {current_date.strftime('%Y-%m-%d')}\n")

    # git add
    subprocess.run(["git", "add", "dummy_file.txt"])

    # случайное время
    commit_datetime = current_date + timedelta(
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    commit_date_str = commit_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # дата для коммита
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = commit_date_str
    env["GIT_AUTHOR_DATE"] = commit_date_str

    # выбираем случайное сообщение из списка
    commit_message = random.choice(messages)

    # git commit
    subprocess.run(
        ["git", "commit", "-m", commit_message],
        env=env
    )

    # смещаем дату
    current_date += delta + timedelta(days=random.randint(0, 3))

print("Фейковые коммиты с разными сообщениями созданы!")
