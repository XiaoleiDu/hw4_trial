Introduction to Jetbot server system

In side the main folder:
    persist_db folder: 
        contains all the tables and files for the mysql server. It ensures that the server, onced brought up, will retain all the necessary files and data. 

    init_db.py: 
        initialize all the tables of mysql database through python program, contains all the tables that need to be created and all the data that need to be inserted. It only need to be run once at the beginning of bringing up the whole server.

    credentials.env: 
        contains username/password information for the mysql server. 

    docker-compose.yml: 
        defines how the mysql server internal ports and external ports are. Helps combine the mysql server into web server.

    webserver folder:
        contains all files to setup webserver 


In side of th webserver folder:
    src forlder:
       contains all the script part of server
    dockerfile: 
        expose port, calls the server python file

In side of src folder:  
    templates folder:
        contains all the html and css
    requirements.txt: 
        defines the required structures/protocols to be used in this web server.

    rest_server.py: 
        contains the main code that defines the different routes of all the html pages (jetBot tracker, jetBot tracker etc.) and also defines the functions that writes the data from mysql into txt files such that the data may be displayed on the html pages including jetbot tracker. It serves as the main file of all the connections

In side of templates folder:
    public foler:
        contains all the css and image for html

    did_login.html(admin portal): 
        after successful login of the user, this page can be directed to from "go to admin portal" button, user can see all the user status and be able to void/verify user.

    gotoAdminPortal.html(main page): 
        the main page that apperas after the user submitted login information and is verified. It contains routes to go to admin portal, jetBot controller, jetBot tracker, jetBot register and logout.

    invalid_credentials.html: 
        contains a message that tells user that wrong information of login, and offers a link to goback to login page.

    j_controller.html(jetBot controller): 
        jetBot controllerthat serves as to control jetBot with the click of the various buttons. Also a route to return to the main page is offered in terms of the goback button

    j_tracker.html(jetBot tracker): 
        jetbot tracker, at the click of button the status of moves are displayed. Also a route to the main page is offered.

    redriectjetbotcontroller.html:
        a webpage that redirect the user to jetBot controller once they are done inputting jetBot id.

    register.html(Sign Up): 
        page to signup a user where the input information will be put into the database with pending status.

    show_login.html(login in): 
        the main login page, gets data input and compare with that in database to verify a user. 

    try_again.html: 
        user is directed here if they register their username and password with special characters, and the page asks them to go back and try again.

    submitjetbotid.html(multiple jetBot handling): 
        takes the jetbot id that the user submits, stores it in to table and later display it j_tracker.html

In side of public foler:
    style.css: 
        css file that defines the style of the website, beening use by all html.
    
    moves.txt: 
        stores data grabbed from database to display on the html page of j_tracker
        
    user.txt: 
        intermediate file that stores the current user read from database to display on website

    users.txt: 
         intermediate file that stores all users data read from database to display on website

		