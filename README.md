# OPP Exercise No.4

## Welcome to our fourth exersice

<sub>code written by Denis Chernoglaz<sub>

In this fourth assigment I was required to fetch data from a server
and work my algorithm to solve optimization problem

fetched data includes :
  pokemons
  agents
  graph
  
the pokemons generated randomaly on a connected graph and agents spawn on different nodes
agents should move towrds each pokemon and reach close enough then the pokemon considered "catched"


## Implementation :
  - wrote in python
  - I used my previous graph algorithms and graph implementaion , check OOP_Ex3 for more info
  - for the pokemon priorety I used a humble solution for the knapsack problem that takes every object
    and sort it by ratio of value/(distance in my case)
  - and agents move only by half of the knapsack problem priority list so they will catch only valuable pokemons
  - to get the best path I used Dijekstra algorithm and the agents move accordingly
  - there are 2 types of pokemons , Ground and Water if the pokemon spawn in the water or in other words
    if the pokemon possition  y > 440 or x > 820 it will be WATER type , otherwise GROUND type
  
  
  
## Algorithms :
  shortestPath - Dijekstra's Algorithm for shortest path works as follow While Q is not empty, pop the node V, 
                 that is not already in S, from Q with the smallest distdist (V). In the first run, source node ss will be chosen because distdist(ss) 
                 was initialized to 0. In the next run, the next node with the smallest distdist value is chosen. Add node vv to SS, to indicate
                 that vv has been visited Update distdist values of adjacent nodes of the current node vv as follows: for each new adjacent node uu, 
                 if dist (V) + weight(u,v) < dist (u), there is a new minimal distance found for u, so update distdist (u) to the new minimal distance value;
                 otherwise, no updates are made to distdist (u). The algorithm has visited all nodes in the graph and found the smallest distance to each node. 
                 distdist now contains the shortest path tree from source s. Note: The weight of an edge (u,v) is taken from the value associated with (u,v) on the graph.
                 [complexity Theta(|E|+|V|log|V|)]

shortestPathDist - We use shortestPath to count the total distance by adding each passed edge and returning it [complexity Theta(|E|+|V|log|V|)]


                                                 
                                                 

## Execute :
  working the best at case 4 use  "java -jar Ex4_Server_v0.0.jar 4"  command to run the server then simple "Bureaucracy.py" would run the code

                                                 
                                                 
## Testing :
  I used my previous task test so it will work also here testing my basic algorithm

                                                 
## Video :

      https://www.youtube.com/watch?v=m0kUNn003rs
                                                 
                                                 
                                                 
## GUI :
  I used the GUI received from the task and customized it , pokemons are actual pokemons that with certain limits change their type
  I put a background image and every detail has an image to describe itself so node are rocks , agent are pokemon hunter and pokemons actual pokemons
                                                 
                                                 
  ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex4/blob/main/Ex4/client_python/images/Screenshot.png)
  
                                                
