# cse138-project1
 The source code for a web server that provides a REST interface, 
 along with a Docker file to create a container that runs it.  
 The web server is built in python, using the Django framework.
 
 ## Capabilities
 
 It supports three endpoints, `/hello`, `hello/<name>`, and `/echo/<msg>`.
 
 `/hello` supports the GET method and no other.  
 On success, returns the string `Hello, world!` and status code 200.
 
 `hello/<name>` supports the POST method and no other.  
 On success, returns the string `Hello, <name>` and status code 200.
 
 `/echo/<msg>` supports the POST message and no other.  
 On success, returns the string `POST message receieved: <msg>` and status code 200.
 
 ## Limitations
 
 Invalid HTTP methods return the string `This method is unsupported. and the status code 405.`  
 Invalid endpoints return status code 404.  



Written for CSE 138 Fall 20 with Professor Peter Alvaro at UCSC.
