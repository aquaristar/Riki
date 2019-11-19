# How the Wiki System Works.

* Written by Freddie Mercury
* 11/12/2017

The wiki system is simple and directory-based, meaning the location of the markdown files used for each page's formatting and content have a direct mapping to their URL used to request them. These files can be uploaded to the server with an included upload page template or directly to the server (although they would have to follow proper url  conventions this way). The Wiki system is capable of easily indexing pages this way, by simply walking through the root directory. Pages contain metadata such as their title and any tags; these, along with the content body, can all be searched through the indexing methods of the Wiki system. 

All CRUD operations can be performed on Pages and Users, with HTML templates given for pages that can utilize these functions included in the installation. Forms executing these actions are extended from the WTForms library. Pages are displayed by converting markdown to HTML after stripping it of any metadata that the system adds to the top of the file. Users are stored on the server in users.json. The web framework backing Wiki is Flask; the app's config can be changed through config.py. Calling "wiki web" from the content directory will run the server using Flask with the directory content provided and as specified in config.py. 