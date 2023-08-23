в файле *flaskwebapp/values.yaml* изменяем переменные:

*image.repository:*    имя образа, запускаемого в поде
*replicaCount:*    количество реплик приложения
*env.name.value:*    значение, подставляемое в переменную AUTHOR

устанавливаем в кластер в отдельный неймспейс командой

`helm --namespace backend install flaskwebapp flaskwebapp/`