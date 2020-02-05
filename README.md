Small demo application connecting with Spotify by REST.\
Using Postgres db for authorization.\
Python version: 3.7



# Local development environment

    python -m venv venv
    source ./venv/bin/activate
    pip install .
    run #to run application
    

#Package that are using here
    Click==7.0
    demo==0.1
    Flask==1.1.1
    Flask-SQLAlchemy==2.4.1
    itsdangerous==1.1.0
    Jinja2==2.11.0
    MarkupSafe==1.1.1
    python-dotenv==0.10.5
    spotify-demo==0.1
    SQLAlchemy==1.3.13
    Werkzeug==0.16.1
    
    
#Creating .env 
    export CLIENT_ID                   # Client Id for Spotify connection
    export CLIENT_SECRET               # secret for Spotify connection
    
    
    export DB_NAME                     # database name
    export DB_PASSWORD                 # database password
    export DB_PORT                     # database port
    


#Things to add

    add tests using pytest package
    configure properly database connection
    add Dockerfile to build application, after that add another container for PostgreSQL

# REST-POSTGRES-Spotify
# REST-Postgres-Flask-Spotify-demo
