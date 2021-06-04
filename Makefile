run_spatial_plot:
	python3 main.py

install_requirements:
	pip install -r requirements.txt && sudo apt-get install libgeos-dev && pip install https://github.com/matplotlib/basemap/archive/master.zip && rm -rf plot

formatting:
	safety check
	isort .
	black .
	flake8 .

install_requirements_dev:
	pip install -r requirements_dev.txt