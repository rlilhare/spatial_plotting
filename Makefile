run_spatial_plot:
	python3 main.py

install_requirements:
	pip install -r requirements.txt && sudo apt-get install libgeos-dev && pip install https://github.com/matplotlib/basemap/archive/master.zip && rm -rf plot
