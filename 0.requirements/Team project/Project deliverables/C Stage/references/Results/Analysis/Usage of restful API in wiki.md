# The usage of RESTFul API in Wiki

* Written by James Bond
* 11/11/2017

CRUD functionalities are included for Pages and Users in the Wiki system as previously discussed in their related classes. Pages are retrieved from the OS directory structure, converting directories and markdown into URLs and HTML. Users are stored in a users.json file which contains any information about them, including roles and either a cleartext or salted hash of a password for authentication. These functions don't rely on any form of statefulness, and neither do the interfaces provided by the system in the form of the HMTL templates included in its installation. 

The HTML makes use of forms using the HTML POST method to send data to parsed by Flask/WTForms and used for the previously mentioned methods. The API is not only just used by the HTML templates, but is also directly able to be called by URL; for example, a known path for a page can be deleted on the server by using the relative route of "/delete/" followed by the path. Some CRUD operations are not fully implemented in this version of Wiki, but all of them are present in the web/routes.py file.