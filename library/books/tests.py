from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title="A good title",
            subtile="An excellent subtitle",
            author="Tom",
            isbn="1234123412341",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtile, "An excellent subtitle")
        self.assertEqual(self.book.author, "Tom")
        self.assertEqual(self.book.isbn, "1234123412341")
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")