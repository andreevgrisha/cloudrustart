Это вебприложение слушает порт **8000** и умеет три метода:

`GET /hostname`
 возвращает имя хоста сервера

`GET /author`
 возвращает значение переменной окружения AUTHOR или, если она не задана - сообщение 'Author not set'.

`GET /id`
 возвращает значение переменной окружения UUID или, если она не задана - сообщение 'UUID not set'.

Обратите внимание, что необходимо задать переменные
`AUTHOR`
 и
`UUID`
 перед запуском скрипта этого вебприложения:
```
export AUTHOR="Your Author Name"
export UUID="Your UUID"
```

Запуск скрипта:

`python webserver.py`

После запуска доступ к веприложение в браузере по url

http://localhost:8000/hostname
http://localhost:8000/author
http://localhost:8000/id

* *создано при помощи ChatGPT EasyCode VSCode extension* *

билд докер-образа 

`docker build -t andreevg/flaskwebapp:0.0.1 .`