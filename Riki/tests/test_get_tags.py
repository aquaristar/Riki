'''
Author: Steve Brownfield
Date: 03/17/2018
'''

from wiki.core import Page
from tests import WikiBaseTestCase

PAGE_CONTENT = u"""\
title: TestGetTagsPageTitle
tags: testTag1, testTag2

Hello, we are testing the wiki get_tags function?
"""

class TestGetTags(WikiBaseTestCase):
    '''
        This tests the get_tags function of the wiki core of the wiki system.
        First we create a temp file called testGetTages.md with some tags, then
        call the get_tags function to see if it returns the proper tags.
    '''

    def setUp(self):
        super(TestGetTags, self).setUp()
        self.page_path = self.create_file('testGetTages.md', PAGE_CONTENT)
        self.page = Page(self.page_path, 'testGetTages')

    def test_get_tags(self):
        assert("testTag1" in self.wiki.get_tags())
        assert("testTag2" in self.wiki.get_tags())

    def tearDown(self):
        try:
            self.wiki.delete("testGetTages")
        except:
            print("Error deleting temp file: testGetTages.md")

