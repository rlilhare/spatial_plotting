run_spatial_plot:
	python3 main.py

install_requirements:
	pip install -r requirements_docs.txt && sudo apt-get update && sudo apt-get install libgeos-dev && pip install https://github.com/matplotlib/basemap/archive/master.zip

formatting:
	safety check
	isort .
	black .
	flake8 .

generate_documentation:
	pdoc --html --output-dir docs --force . 

open_documentation:
	open docs/index.html

install_requirements_dev:
	pip install -r requirements_dev.txt

docker_build:
	docker build . -t rlilhare/spatial_plotting

docker_run:
	docker run -d --name spatial_plotting --mount type=bind,source="$$(pwd)/",target=/spatial_plotting rlilhare/spatial_plotting

docker_shell:
	docker exec -it rlilhare/spatial_plotting /bin/bash

docker_stop:
	docker stop rlilhare/spatial_plotting

docker_remove:
	docker rm rlilhare/spatial_plotting

docker_push:
	docker push rlilhare/spatial_plotting:latest

download_basemap:
	wget https://github.com/matplotlib/basemap/archive/master.zip && unzip master.zip 

install_geos:
	cd basemap-master && cd geos-3.3.3 && env GEOS_DIR=/usr/local ./configure && make && make check && make install
# cd basemap-master && cd geos-3.3.3 && ./configure && make && make check && make install

cleanup_basemap:
	rm -rf basemap-master && pip install https://github.com/matplotlib/basemap/archive/master.zip && rm master.zip