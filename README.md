# GNS Users

## Part 1. REST API for user management and authentication

I used Flask because I have wanted to try it for long but since I was not experienced with REST API design - I mainly 
used, not created any APIs for Python devtools - I decided I'd go as I would naturally go with it and Googled heavily.

Did it in 3 sittings, you may see it from the commit history. To sum it up:

1. I wanted to use Flask to create server easily but didn't know how to create simple backend with no UI. I aimed to create the API endpoints first and then DB I was not familiar with authentication or how the requests should be handled so I had to look up
[a suitable example](https://github.com/miguelgrinberg/REST-auth/blob/master/api.py) and tailored it to the assignment.
2. I created the API endpoint outline then went on to create an authentication flow - for this I had to briefly study [Flask httpauth](https://flask-httpauth.readthedocs.io/en/latest/). Later I refined the API endpoints to accept multiple methods thus make it more simple with less endpoints.
3. During the second sitting I completed the user management (list, add) by studying [Flask SQLAlchemy DB model](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/?highlight=session#inserting-records) and figured out how to make authentication work.
4. Finally I had some debugging to do and find out how to update the model with login timestamps.

## Part 2. - Architectural Analysis

For the application to withstand production-level load it is crucial to define how it should be deployed. The microservice architecture is the most suitable to scale and adapt to increased traffic and load.

The two basic types of microservice scaling are horizontal and vertical. 
- Vertical scaling in our case means that we need to specify the necessary resources (server instance type, CPU, RAM, storage) to run the web service. This may change as it is developed and gets new functionality and at some extent increasing the host's capacity may help serve bigger traffic but this is not flexible.
- Horizontal scaling means that we place the service behind a load balancer and launch multiple instances depending on the actual load (CPU, memory) - with setting the proper benchmark for scaling in our out. This can be solved easily with many container orchestration systems e.g. AWS ECS or Kubernetes. 

_DB scaling:_ I'd start with not using SQLite but a proper database and on a different server. In order to withstand higher load, type of scaling can be applied at the database level as well with multiple DB replicas (e.g. in AWS RDS).

_Message queues:_ if the architecture makes it possible message queues (e.g. RabbitMQ, AWS SNS/SQS) can be used to queue requests to avoid possible timeouts for the API calls. 

_CDN:_ For web services the server load can be reduced by applying a Content Delivery Network where the selected server locations (regions) have to be close to the userbase. This can significantly decrease the server/backend load and also protect the service against DOS attacks.
