# MySQL + Flask Boilerplate Project

## Project Overview 
Our project is an application that stores information on users looking to sublet their apartment for a set period of time of their choosing (example: summer, semester, few weeks, etc). The user interfaces we've created would be for potential subletters and sublessors. It is anonymous on the front end and would show only a subletter/sublessor’s username. Potential subletters can contact those posting sublet information through direct messaging. Sublessors can create, update, and delete their postings. They also have the ability to add and update their lease information, as well as view their reviews. Subletters are be able to scroll and filter through postings based on price, to look at various off-campus options that meet their needs. All users are be able to see the apartment’s photos, description, and basic roommate and pricing information. Subletters are also able to create, delete and update their own profile info. The application would be open to Northeastern students who are both looking to sublet their apartment out and find a place to sublet. 


This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




