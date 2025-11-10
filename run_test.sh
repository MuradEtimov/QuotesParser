#!/bin/bash

# 1️⃣ Создаём временное виртуальное окружение
python3 -m venv temp_env

# 2️⃣ Активируем виртуальное окружение
source temp_env/bin/activate

# 3️⃣ Устанавливаем зависимости
pip install --upgrade pip
pip install -r requirements.txt

# 4️⃣ Запускаем основной скрипт
python Exel_lol.py

# 5️⃣ Деактивируем окружение
deactivate

# 6️⃣ (Опционально) можно удалить временное окружение после работы
# rm -rf temp_env

echo "Correct"
