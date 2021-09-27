# pwc-backend-exercise
This codebase contains the solution for the PwC code challenge. The backend is implemented by **Flask** framework. The relational database is implemented by **SQlite3** and the frontend is using **HTML**, CSS library like **Bootstrap**, JavaScript libraries like **jQuery** and **table-sortable**. This codebase is already configured and can be deployed on Google Cloud Platform directly.

# Requirements

The codebase is implemented in Python 3.6.8. Required packages are:
    
    Flask==2.0.1
    gunicorn==20.1.0 
    
## Deploy 

### Deploy on local host 

    cd pwc-backend-exercise
    pip install -r requirements.txt
    Mac/Linux OS:
        export FLASK_APP=main 
        export FLASK_ENV=development
    Windows:
        set FLASK_APP=main 
        set FLASK_ENV=development 
    flask run  
    
### Deploy on Google Cloud Platform 

    cd pwc-backend-exercise
    gcloud app deploy      
          
      
<br>

## Display

The main page is:  
![pwc_image](https://user-images.githubusercontent.com/91405731/134839178-ccf86441-da49-485d-b04e-82c0d30ee009.png)       

<br>

The main page is showing all the companies when loaded. <br>
The users can use the input box to search the business number to check if the company is restricted. And there is a valid check of the business number. <br>
The users can get all restricted companies by clicking the **Show restricted** button. And the results are paginated at 100 items. <br>
Thes users can get all companies by clicking the **Show all** button. And the results are paginated at 100 items.




    
