"""Posts models"""


# Django imports
from django.db import models


# Local imports
from django.contrib.auth.models import User


class Post(models.Model):
	"""Post models"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	photo = models.ImageField(upload_to="posts/photos")

	crated = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)


	def __str__(self) -> str:
		"""Return title and username"""
		return "{} by @{}".format(self.title, self.user.username)