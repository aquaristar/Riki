'''
Author: Steve Brownfield
Date: 03/17/2018
'''

from wiki.core import Page
from tests import WikiBaseTestCase

PAGE_CONTENT = u"""\
title: TestDeletePageTitle
tags: test, testdelete

Hello, we are testing the wiki delete page functionality?

"""

class TestDelete(WikiBaseTestCase):
    '''
        This test if the delete function of the Wiki is functioning properly.
        First creates a temp file called testdelte.md and then trys to delete it.
    '''

    def setUp(self):
        super(TestDelete, self).setUp()

        #need to create a page that we can test delete
        self.page_path = self.create_file('testdelete.md', PAGE_CONTENT)
        self.page = Page(self.page_path, 'TestDeletePageTitle')

    def test_delete(self):
        assert(self.wiki.delete("testdelete"))











