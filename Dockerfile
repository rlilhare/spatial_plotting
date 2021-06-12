# syntax=docker/dockerfile:1
FROM continuumio/miniconda3:latest

COPY . /spatial_plotting
WORKDIR /spatial_plotting

RUN conda env create -f environment.yml
# SHELL ["conda", "run", "-n", "spatial_plotting", "/bin/bash", "-c"]

RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"] 

RUN conda install -c conda-forge --file requirements.txt -y
RUN conda install -c conda-forge --file requirements_dev.txt -y



CMD ["python", "main.py"] 
