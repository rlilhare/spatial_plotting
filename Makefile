run_spatial_plot:
	python src/spatial_plot_temperature.py

install_requirements:
	pip install -r .\requirements.txt && curl https://download.lfd.uci.edu/pythonlibs/q4trcu4l/basemap-1.2.2-cp39-cp39-win_amd64.whl --output .\basemap-1.2.2-cp39-cp39-win_amd64.whl && python -m pip install .\basemap-1.2.2-cp39-cp39-win_amd64.whl && rm .\basemap-1.2*
