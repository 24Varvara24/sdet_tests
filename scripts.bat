rmdir /s /q result
call ./venv/Scripts/activate
pytest --alluredir result
allure serve result
