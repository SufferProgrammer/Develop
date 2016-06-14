from django.test import TestCase
from django.utils import timezone
import datetime
from website.models import Post

class Data(TestCase):
	def test(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future = Post(Created=time)
		self.assertEqual(future.recent_Created(), False)
