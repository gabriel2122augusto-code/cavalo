#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py ler
python manage.py inserir_comp_exigencias
python manage.py inserir_dados
