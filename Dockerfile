# working with docker base image python 3.11
FROM python:3.11

#Set the working directory inside the container to /code
# All subsequent commands will run from this directory
WORKDIR /code
#Copy the requirements.txt file from the local machine to the container at /code/requirements.txt
COPY ./requirements.txt /code/requirements.txt
#install Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
#copy the rest of the application code from the local directory to /code/app in the container
COPY . /code/app
#Expose port 8080 to allow external access to the application
EXPOSE 8090
# Command to start the FastAPI application using uvicorn
 ## The app.main:app indicates:
 ##   - 'app' (folder name)
 ##   - 'main' (main.py file)
 ##   - 'app' (FastAPI instance inside main.py)
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8090"]