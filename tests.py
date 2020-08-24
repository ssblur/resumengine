from django.test import TestCase
from .models import Document, Tag

class SearchTestCase(TestCase):
    def setUp(self):
        self.doc1 = Document.objects.create(document_name = 'orange', document_type = 0, contents = 'grape', visibility = 0)
        tag1 = Tag.objects.create(tag_name = 'orange')
        self.doc2 = Document.objects.create(document_name = 'grape', document_type = 0, contents = 'melon', visibility = 0)
        self.doc2.tags.set([tag1])
        self.doc3 = Document.objects.create(document_name = 'grape', document_type = 0, contents = 'melon', visibility = 0)

    def test_search(self):
        q1 = Document.search('orange')
        assert self.doc1 in q1
        assert self.doc2 in q1
        assert not self.doc3 in q1

        q2 = Document.search('grape')
        assert self.doc1 in q2
        assert self.doc2 in q2
        assert self.doc3 in q2

        q3 = Document.search('melon')
        assert not self.doc1 in q3
        assert self.doc2 in q3
        assert self.doc3 in q3

        q4 = Document.search('a')
        assert self.doc1 in q4
        assert self.doc2 in q4
        assert self.doc3 in q4

        q5 = Document.search('z')
        assert not self.doc1 in q5
        assert not self.doc2 in q5
        assert not self.doc3 in q5
