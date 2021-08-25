# Lahman-Baseball-Operational-System

## Overview ##
### •	Built a Flask web application based on Lahman Baseball Database that can implement a set of REST resources and functions for create, retrieve, update and delete resources. The web application is capable of managing specific paths for SQL and Neo4j databases.

### The web application that support specific paths for SQL and Neo4j databases are:
### ● POST, GET with query parameters on: 
####  ○ /FantasyTeam
####  ○ /FantasyPlayer
####  ○ /FantasyManager 
####  ○ /FantasyLeague
####  ○ /FantasyTeam/{teamID}/FantasyPlayer
####  ○ /FantasyLeague/{leagueID}/FantasyTeam 
### ● GET, PUT, DELETE on
####  ○ /FantasyTeam/{teamID}
####  ○ /FantasyTeam/{teamID}/FantasyPlayer/{playerID} 
####  ○ /FantasyManager/{uni}
####  ○ /FantasyManager/{uni}/FantasyTeam/{teamID}
####  ○ /FantasyManager/{uni}/FantasyLeague/{leagueID}

### The paths on Neo4j are:
### ● Social links: Neo4j Only
####  ○ GET, POST: /FantasyManager/{uni}/Follows
####  ○ GET, POST: /FantasyManager/{uni}/Likes
