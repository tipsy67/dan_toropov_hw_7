# dan_toropov_hw_8

Домашняя работа по курсу Docker

Для работы программы необходимо:

1. установленный docker
2. создать .env по примеру .env.example
3. sudo docker-compose up -d --build #команда для сборки и запука контейнеров
4. sudo docker-compose exec app python manage.py csu #команда для создания суперпользователя 
   логин пользователя и пароль можно изменить в файле /users/management/commands/csu.py
4. фикстуры лежат в каталоге /data/fixtures