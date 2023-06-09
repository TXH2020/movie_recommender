
sudo docker compose run web python manage.py makemigrations --noinput
sudo docker compose run web python manage.py migrate --run-syncdb

sudo docker compose run web python populate_moviegeek.py
sudo docker compose run web python populate_ratings.py
