# COMPSCI-235-FLIX

## Description
A Web application that collect thousands of movies for user to watch, comment and bookmark.

THe application makes use of Python's Flask framework, Jinja templating library and WTForms.
Architectural design patterns and principles including Repository, Dependency Inversion and Single Responsibility have been used to design the application. The application uses Flask Blueprints to maintain a separation of concerns between application functions. Testing includes unit and end-to-end testing using the pytest tool. 

**Installation via requirements.txt**

```shell
$ cd COMPSCI-235-FLIX
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```
When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *COMPSCI-235-FLIX* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

## Configuration

The *COMPSCI-235-FLIX/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.


## Testing

Testing requires that the ***PATH*** value in file *COMPSCI-235-FLIX/TEST_DATA_PATH.py* be edited. You should set this to the absolute path of the *COMPSCI-235-FLIX/tests/data* directory. 

E.g.
 
`PATH = "C:\\File_You_Put_This_Project\\COMPSCI-235-FLIX\\tests\\data"`



You can then run tests from within PyCharm Configuration, or in terminal via:
````shell
$  python -m pytest
```` 




