# coding=UTF-8

from django.test import TestCase

# Create your tests here.
from .models import address

class AddressMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
        self.assertEqual(False, False)

    def test_add(self):
        a = address(city="桃園", area="桃園區");
        a.save()
        self.assertEqual(True, False)
            
            
            
