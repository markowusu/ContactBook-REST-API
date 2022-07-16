# ContactBook-REST-API
Dockerfile
Builds the Django container. The container is built from a standard python Docker image and will run Django's
--

colletstatic when being built.

Running
To run the program from the docker container
run ` docker-compose up `

Commiting to Docker containers 
-- docker exec  -it CONTAINER_ID   bash -- this runs the CLI for the docker file. then you run `pip install -r requirements.txt`

After that you can run a commit instruction 
-- docker commit  CONTAINER_ID  NAME_OF_IMAGE(any prefered name)    

docker-compose.yml
--

Tasked with spinning up two containers: the above container for Django, one for PostgreSQL 
In this configuration, the Django server will be available on port 8000 during production.

Docker can be accessed directly on port 8000. Static files can then be served from the static_files_volume Docker volume.
--

Loads automatically when running a standard docker-compose up. 
--

These values are intended for development purposes as they tweak the container configurations in the following way:
--

*Make the Postgres container accessible externally on port 5432
*Make the site available  at http://localhost:8000


.env
--

Contains environment variables for the containers. 
--

Several variables are included for configuring Postgres and Django secrets.
--

The ADMIN_EMAIL must be set to an email that will recieve notification on upload when upload is successful.

Troubleshooting
The Django container reports "exited with code 3"
You probably forgot to replace the string "appname" with the actual name you passed to django-admin startproject. 
ModuleNotFoundError: No module named 'appname'


| url        |               |          |
| ------------- |:-------------:| -----:|
| GET  `http://localhost:8000/contacts`     | returns lits of 20 contacts in the db per page |  |
| GET `http://localhost:8000/contacts/{id}` | return the user and its contacts via id 
| POST `http://localhost:8000/contacts`     | to create a new contact with {first_name,last_name,phone_number}  as body      |    |
| POST `http://localhost:8000/contacts/upload-csv`     | this is used to upload the csv-file
| DELETE `http://localhost:8000/contacts/{id}`   | It  deletes by id   |   |

Architecture:
I did not really use any achicture design in this implementation but future updates may require a hexagonal architecture(Ports and Adapters)--

But I implemented Single responsiblity and minization of reasons of change.

Unit Test:
No performed due to time constraints at my end. Future updates may include testing.

Email service : 
I used Twillio for sending email to any ADMIN_EMAIL set in the .evn file.


API DOCS
--

For API docs vist `http://localhost:8000/docs` this provides you with the swagger docs for for each of the endpoints in the application.
