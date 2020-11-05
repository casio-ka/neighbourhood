serve:
	python3 manage.py runserver

migrate:
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations $(app)

collectstatic:
	python3 manage.py collectstatic

app:
	#django-admin startapp <name>
	python3 manage.py startapp $(name)

check:
	python3 manage.py check

test:

	coverage run ./manage.py test

report:
	coverage html

superuser:
	./manage.py createsuperuser --username $(name)
