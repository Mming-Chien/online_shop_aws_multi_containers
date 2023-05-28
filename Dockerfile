# Pull official base Python Docker image
FROM python:3.9-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set work directory
WORKDIR /code 
RUN chmod 777 /code/
# Install dependencies 
RUN pip3 install --upgrade pip
RUN pip3 install wheel 
RUN pip3 install pyproject-toml
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
CMD  ["./wait-for-it.sh","db:5432","--","uwsgi","--ini","/code/config/uwsgi/uwsgi.ini"]

# Copy the django project
COPY . /code/ 


