# trains-backend

### запуск

* docker-compose -f docker-compose.local.yaml up --build поднимет окружение бэкенда
* в src/scripts лежат скрипты для генерации тестовых данных
    * Порядок для избежания ошибок:
    * generate_stations_data
    * generate_routes_data
    * generate_data_ch
* alembic upgrade head для миграций
* миграция для кликхауза лежит в качестве скрипта в /src/common/db/clickhoouse.py

### git

* pre-commit install
* плодим ветки от dev
* нейминг веток:
    * feature/<feature_name>
    * fix/<fix_name>
    * refactor/<_subject>
* при мерже ревью