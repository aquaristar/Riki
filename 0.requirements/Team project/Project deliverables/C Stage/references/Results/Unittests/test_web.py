from . import WikiBaseTestCase

import os

from flask import current_app
from flask import Flask
from flask import g
from flask import app
from wiki.web.user import UserManager
from wiki.web.user import User
class WebContentTestCase(WikiBaseTestCase):
    """
        Various test cases around web content.
    """

    def test_index_missing(self):
        """
            Assert the wiki will correctly play the content missing
            index page, if no index page exists.
        """
        rsp = self.app.get('/')
        assert b"You did not create any content yet." in rsp.data
        assert rsp.status_code == 200


TEST_FILE_PATH = 'tests/'

class TestUserManager(WebContentTestCase):

    def setUp(self):
        super(TestUserManager, self).setUp()

    def test_invalid_authentication_method(self):
        m = UserManager(TEST_FILE_PATH)
        self.assertRaises(NotImplementedError, m.add_user, m, 'bobby', 12345, authentication_method='this will cause an error')

        ...


class TestUser(WebContentTestCase):
    def setUp(self):
        super(TestUser, self).setUp()

    def test_get(self):
        m = UserManager(TEST_FILE_PATH)
        u = m.get_user('name')
        self.assertIsNotNone(u.get('password'))

        ...

