## Productionize-Flask application

#####Issues in simple flask development
1. All types of logic(db access, processing, ml logic) inside routes
2. No proper segregation of logics
3. Hard to debug
4. Hard to maintain in production environment

#####Solution : Follow MVC 

![Application Flow](application_flow.png)

Here `red lines` means no direct communication between the layers.

In this series i will try to explain steps to productionize simple flask application with MVC architecture to separate logic between different layers. This helps to track issues and maintain code in production environment.

In this repo you can find a boiler plate code with proper layer segregation.

#####Step_1
very simple flask application

#####Step_2
flask application with database initialization and migration

#####Step_3
flask application with proper MVC architecture/layer separation

#####Note: Idea of this repo is to provide boilerplate to productionize flask. Existing code is not working. I will work on writing small app in sometime.




