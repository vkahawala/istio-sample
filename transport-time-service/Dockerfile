FROM python:3.6

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY service.py /usr/src/app/

# tell the port number the container should expose
EXPOSE 9000

# run the application
CMD ["python", "/usr/src/app/service.py"]