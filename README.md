# spatial_plotting
to plot spatial maps
to  install basemap: https://www.lfd.uci.edu/~gohlke/pythonlibs/

https://download.lfd.uci.edu/pythonlibs/q4trcu4l/basemap-1.2.2-cp39-cp39-win_amd64.whl

to make virtual environments:
    install pipenv: $ sudo apt install pipenv
    to create virtual environment: pipenv --python 3.8
    to activate pipenv environment: pipenv shell

    to install requirements: make install_requirements

to make docker file:

to build docker file:

to generate documentation:
    pdoc your_project
    

[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]
numpy = "==1.20.3"
netCDF4 = "==1.5.6"
matplotlib = "==3.4.2"
Pillow = "==8.2.0"
basemap = {git = "https://github.com/matplotlib/basemap/archive/master.zip"}

[dev-packages]
isort = "==5.8.0"
black = "==21.5b2"
flake8 = "==3.9.2"
safety = "==1.10.3"
pdoc3 = "==0.8.1"

[requires]
python_version = "3.9.1"
