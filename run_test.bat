@echo off
REM Создаем виртуальное окружение
python -m venv temp_env

REM Активируем виртуальное окружение
call temp_env\Scripts\activate

REM Обновляем pip и устанавливаем зависимости
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Запускаем скрипт
python Exel_lol.py

REM Деактивируем виртуальное окружение
deactivate

echo Correct
pause
