Перед запуском необходимо установить

`ansible-galaxy collection install ansible.posix`

и разрешить первое подключение без ssh-ключа

`export ANSIBLE_HOST_KEY_CHECKING=False`

запуск плейбука

`ansible-playbook -i inventory.ini playbook.yml`