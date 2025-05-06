from django.test import TestCase, Client
from django.urls import reverse
from .models import Thing, Review

class ThingModelTest(TestCase):
    def setUp(self):
        self.thing = Thing.objects.create(
            name='Test Thing',
            description='Test Description',
            price=10.00
        )

    def test_thing_creation(self):
        thing = Thing.objects.get(name='Test Thing')
        self.assertEqual(thing.name, 'Test Thing')
        self.assertEqual(thing.description, 'Test Description')
        self.assertEqual(thing.price, 10.00)

    def test_thing_str_representation(self):
        thing = Thing.objects.get(name='Test Thing')
        self.assertEqual(str(thing), 'Test Thing')

class ReviewModelTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            title = 'Test review',
            body = 'Test body',
            rating = 5,
        )

    def test_review_creation(self):
        review = Review.objects.get(title='Test review')
        self.assertEqual(review.title, 'Test review')
        self.assertEqual(review.body, 'Test body')
        self.assertEqual(review.rating, 5)

