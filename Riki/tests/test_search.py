'''
Author: Steve Brownfield
Date: 03/16/2018
'''

from wiki.core import Page
from tests import WikiBaseTestCase

PAGE_CONTENT = u"""\
title: TestSearchPageTitle
tags: one, two

Hello, we are testing the wiki search?

"""

class TestSearch(WikiBaseTestCase):
    '''
        This tests the search functionality of the wiki system.
        First we create a temp file called testsearch.md and then
        try to find that file with the wiki search function.
    '''

    def setUp(self):
        super(TestSearch, self).setUp()
        self.page_path = self.create_file('testsearch.md', PAGE_CONTENT)
        self.page = Page(self.page_path, 'testsearch')

    def test_search(self):
        self.matches = []
        self.matches = self.wiki.search("TestSearchPageTitle")
        assert self.matches[0].meta == self.page.meta

    def tearDown(self):
        try:
            self.wiki.delete("testsearch")
        except:
            print("Error deleting temp file: testsearch.md")
