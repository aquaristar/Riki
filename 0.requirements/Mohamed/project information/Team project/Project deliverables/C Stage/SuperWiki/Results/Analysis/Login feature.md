# Login system

* Written by Samuel Cho
* 11/12/2017

## Turn-on user login feature

You can turn on the login feature with `PRIVATE = True`.
Also, you must add `users.json`. Read the rest of this page.

## loginmanager

Flask supports loginmanager. 

* (1) links the Flask's user_login() function with loginmanager. Remember 'wiki' is prepended because wiki440 uses [[Flask/blueprint]].

```
from flask_login import LoginManager

loginmanager = LoginManager() 
loginmanager.login_view = 'wiki.user_login' # (1)
```

## users.json load and access

wiki440 stores user information in `users.json`. Let's see how this file is loaded and accessed.

### get_users() function in web/__init__.py

get_users() function instantiates UserManager object. 

```
def get_users():
    users = getattr(g, '_users', None)
    if users is None:
        users = g._users = UserManager(current_app.config['USER_DIR'])
    return users
```

UserManager class requires the directory that the users.json is located.
I changed the location from `CONTENT_DIR` to `USER_DIR` in `config.py`. Also created the user directory.

```
CONTENT_DIR = 'YOURWIKI/content'
USER_DIR = 'YOURWIKI/user'
```

The `users.json` file can contain this information as an example. I created the file in the user directory. This json file means that a user "name" has password "1234".

```
{
  "name": {
    "active": true, 
    "authentication_method": "cleartext", 
    "password": "1234", 
    "authenticated": true, 
    "roles": []
  }
}
```

### Access the user

When you click `Login` and invoke `/user/login` API, you will execute this code. You should give "name" and its password "1234" to login.

```
@bp.route('/user/login/', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = current_users.get_user(form.name.data)
        login_user(user)
        user.set('authenticated', True)
        flash('Login successful.', 'success')
        return redirect(request.args.get("next") or url_for('wiki.index'))
    return render_template('login.html', form=form)
```

Flask understands the `users.json` to return True from `form.validate_on_submit()` because of the LoginForm class. And you will see "Login successful" message.

This is the LoginForm class.

```
class LoginForm(Form):
    name = TextField('', [InputRequired()])
    password = PasswordField('', [InputRequired()])

    def validate_name(form, field):
        user = current_users.get_user(field.data)
        if not user:
            raise ValidationError('This username does not exist.')

    def validate_password(form, field):
        user = current_users.get_user(form.name.data)
        if not user:
            return
        if not user.check_password(field.data):
            raise ValidationError('Username and password do not match.')
```

### Limitation of wiki440

As you notice, no user related APIs are not implemented. This can be one of your stage B features. 

```
@bp.route('/user/')
def user_index():
    pass


@bp.route('/user/create/')
def user_create():
    pass


@bp.route('/user/<int:user_id>/')
def user_admin(user_id):
    pass


@bp.route('/user/delete/<int:user_id>/')
def user_delete(user_id):
    pass
```