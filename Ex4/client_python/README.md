# OPP Exercise No.3

## Welcome to our third exersice
<sub>code written by Denis Chernoglaz</sub>

In this project we practice graph algorithms such as :
 - Dijekstra's algorithm for finding shortest path 
 - Travel Sales Problem algorithm for reaching every node on the graph with shortest road travel
 - Graph center node
 - Graph connectivity to see if the graph is connected or saperated

also we practiced Python GUI in this project with the help of Tkinter library


## Implementation :

As we know ,graph is a mathematical object that contains 2 sets , G = <V,E> 
V is a set of vertices and E is a set of Edges
we wanted to implement this object so we wont spend process time on traversing all of the data
so we used this methods to reach O(1) with this directed graph (can be undirected too if for every edge you add the opposite edge)

- NodeData graph - I used Dictionary<Integer,NodeData> , Dictionary receives key and returns a node object
  that contains all the information of the node such as : key , string info , tag (for algorithms internal use)
  weight , and coordinates (x,y,z) , Dictionary also counts the nodes as we insert them
- EdgeData graph - we used Dictionary<Integer,Dictionary<Integer,EdgeData>> , first hashmap receives a key 
  this key is the source node key and it returns a hashmap of destinations because every node can have
  different destinations , so after we insert the src key we inserting destination key and we receive EdgeData object
  that contains all the information on that edge such as : source key , destination key , weight (double) , string info , tag (for internal use)
  and the general Dictionary also count the edges
  
  
  see picture below to understand more :
  
     ![name-of-you-image](https://github.com/Denis-Dev-2020/OPP_Ex2/blob/main/Ex02Pics/Imple.png)
  
  
  
  
  
  
## Algorithms :
  
  - shortestPath - Dijekstra's Algorithm for shortest path works as follow 
                   While Q is not empty, pop the node V, that is not already in S, from Q with the smallest distdist (V).
                   In the first run, source node ss will be chosen because distdist(ss) was initialized to 0. In the next run,
                   the next node with the smallest distdist value is chosen. Add node vv to SS, to indicate that vv has been visited
                   Update distdist values of adjacent nodes of the current node vv as follows: for each new adjacent node uu,
                   if dist (V) + weight(u,v) < dist (u), there is a new minimal distance found for u, so update distdist (u) to the new minimal distance value;
                   otherwise, no updates are made to distdist (u).
                   The algorithm has visited all nodes in the graph and found the smallest distance to each node. 
                   distdist now contains the shortest path tree from source s.
                   Note: The weight of an edge (u,v) is taken from the value associated with (u,v) on the graph.   [complexity Theta(|E|+|V|log|V|)]
  
  - shortestPathDist - We use shortestPath to count the total distance by adding each passed edge and returning it  [complexity Theta(|E|+|V|log|V|)]

  - center - first we find ecentricity for each node
             ecentricity is
             e(v) = max{d(u,v)/u belongs to V(G)};v belongs to V
             d(u,v) is the shortest path from u to v
             then radius, r(G) = min {e(v)/v belongs to V(g)}
                               = min {e(1),e(2),...,e(last)}
             if r(g) = e(v)  then v is the central point of G [complexity O(n*(|E|+|V|log|V|))]
             
  - tsp - TSP is a well known NP hard problem and we tried to optimize the algorithm as much as we could
          we need to traverse every node and the node graph to see if we should use him or other node to reach
          every node on the graph , we starting by finding all the possible pairs (1,1),(1,2),..,(2,1),(2,2)..
          thats  n x n = n^2  then we eliminate the same vertices (1,1)(2,2) we have n of those
          then we check first if there an edge connecting for every pair O(1) that will eliminate lots of pairs
          and the we get all of the possible permutations with the help of getPermutations function
          after all that we check every option and calculate minimum path and return that path after all
          the modification it is still complex problem we do it around O(n!)
          
          PLEASE DO NOT TEST ON BIG GRAPH CAUSE OF COMPLEXITY


  - load - get all the data from json file and put it inside our general graph "_DWG"   O(n)

  - save - saves the current graph and edges as it is with all the changes     O(n)
  
## Execute :

  2 ways :
  
   1. just run main.py and the GUI will open automaticly then you can load a path to "data/A3.json"
      or other json file , you put it in the pink entry box near "Load" button
     
   2. you can run it with an argument of A3.json file (for example) without "data/" before but
      be sure to put data folder inside src folder with json files , then run it like that:
      python3.9 main.py A3.json
  
  
## Testing :
  included Unittest file
  We have conducted several tests on all of our algorithms with great results
  we attached a JUnit test file that check all of our operations with several different
  graphs , on other test we checked the speed of our algorithms for example here the 
  Dijekstra's shortest distance algorithm :
  
  - for 1000 nodes graph we received the speed of msec(1387.239)
  
  - for 10000 nodes graph we received the speed of msec(2694.942)


 That was a bit slower then the previous assigment
  
  
## GUI :
  
  We have 5 buttons , 2 for loading and saving graph and 3 for algorithms (dijekstra , center , tsp)
  we show the paths and the center on the frame each with different color 
  if you have problem with overlaying and refreshing just *minimize* the window and *maximize* again and
  it will work smoothly
  
  when you open the program first please press on the "Load Graph" first
  you can also view everything together and you can de-active button by pressing it again and refreshing the page
  
  
  
  
## Screenshots :
 
![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex3/blob/main/Ex03/src/Ex03Pics/Dije.png)
      
![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex3/blob/main/Ex03/src/Ex03Pics/TSP.png)
            
![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex3/blob/main/Ex03/src/Ex03Pics/Center.png)
                  
![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex3/blob/main/Ex03/src/Ex03Pics/Run.png)
                        
![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex3/blob/main/Ex03/src/Ex03Pics/Run2.png)

  
  
  
  
  
  
  
  

