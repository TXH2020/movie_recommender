# Movie Recommender System

Requirements:
- Linux
- Docker
- Python3(>=3.8)
- git

## Project Setup
Steps to set up the project:
- create a python virtual environment(using python -m venv or virtualenv) 
- `git clone https://github.com/txh2020/movie_recommender.git`
- `sudo docker run --name some-postgres5 -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`
 
Here mysecretpassword is the password found in prs_project settings. If you want another password, modify appropriately and reflect the changes in the docker command.
- `sudo docker exec -it some-postgres5 bash`. Then inside the container(when prompt changes to #root...), type `psql -U postgres`. Then create a database using `create database moviegeek;`. Now you can exit the container.
- Goto the movie_recommender folder and open a terminal there.
- Activate the virtual environment using `source location_of_virtual_environment_folder/bin/activate`
- `pip install -r requirements.txt`
- `cd data`
- `python load_lda_sim.py`
- `cd csv_files`
- `sudo docker cp . some-postgres5:/opt/`
- Issue `cd ..` two times to be in the movie_recommender directory.
- `python manage.py makemigrations`
- `python manage.py migrate --run-syncdb`
- `python data_loader.py`. This took 9min on a Linux VM with 4Gb RAM 2cpus.
- `python manage.py runserver` 
 
