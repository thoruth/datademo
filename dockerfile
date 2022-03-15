from jupyter/base-notebook:notebook-6.4.8

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 uninstall jupyterlab -y

RUN mkdir /home/jovyan/workspace
RUN chown jovyan:users /home/jovyan/workspace

COPY jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py