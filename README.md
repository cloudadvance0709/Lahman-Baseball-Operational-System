# Lahman-Baseball-Operational-System

## Overview ##
### Built Operational System that will implement a set of REST resources and functions for create, retrieve, update and delete of the resources. The resources are:
### • FantasyManager
### • FantasyTeam
### • FantasyLeague
### • FantasyPlayer
### • RealWorldPlayer
### Implemented a Flask Web Application capable of managing the paths needs to support on SQL and Neo4j are:
### ● POST, GET with query parameters on: 
###  ○ /FantasyTeam
###  ○ /FantasyPlayer
###  ○ /FantasyManager 
###  ○ /FantasyLeague
###  ○ /FantasyTeam/{teamID}/FantasyPlayer
###  ○ /FantasyLeague/{leagueID}/FantasyTeam 
### ● GET, PUT, DELETE on
###  ○ /FantasyTeam/{teamID}
###  ○ /FantasyTeam/{teamID}/FantasyPlayer/{playerID} 
###  ○ /FantasyManager/{uni}
###  ○ /FantasyManager/{uni}/FantasyTeam/{teamID}
###  ○ /FantasyManager/{uni}/FantasyLeague/{leagueID}

### The paths on Neo4j are:
### ● Social links: Neo4j Only
###  ○ GET, POST: /FantasyManager/{uni}/Follows
###  ○ GET, POST: /FantasyManager/{uni}/Likes
  
Defined the routes and handlers. 


## Demo Video ##
### https://drive.google.com/file/d/1_viAkHPPlxosVyz-st0VNDlika304sdL/view?usp=sharing


## Technologies Used ##
### • Frontend: HTML, CSS, Bootstrap, Javascript, ReactJS
### • Backend: RESTful API, PostgreSQL, Node.js, Express.js, Clarifai API
### • Others: npm packages (Bcrypt, knex, body parser, cors)

## Website Screenshot ![image](https://user-images.githubusercontent.com/46899307/129155446-9e93a923-b096-4e07-ac2e-e2b43bce56ab.png)
