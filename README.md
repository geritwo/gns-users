# GNS Users

## App
Boilerplate user management with REST API

Notes:
- Wanted to use Flask to create server easily but what about no UI
- Aimed to create nice API endpoints, how to manage authentication? Went to hardest part first
- Had to do as great artists and [see best example](https://github.com/miguelgrinberg/REST-auth/blob/master/api.py)
- Aimed to use advanced DB management but not familiar with SQLAlchemy

# How to scale
- Basic setup - vertical scaling: define optimal server instance type for web application, need to reconfigure, not scale for adjustments
- Horizontal scaling: With proper load balancing, launch more instances - auto-scale with container services like ECS
- Horizontal scaling based on instance CPU or memory load
- Caching with CDN: if it is a web service, all CRUD operations may be hard to cache but for login and content retrieval CDN may help
- Can to scale database to match increased backend load, e.g. RDS: multiple DB instances
- Use Message Queue e.g. Rabbit MQ or AWS SQS, between front-end app ad API or back-end and DB