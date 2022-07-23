from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.
class BlogTests(Testcase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@gmail.com',
        password='secret'
      )
    self.post = Post.objects.create(
        title='A good title',
        slug='a-good-slug',
        body='Nice body content',
        author=self.user,
      )
  def test_string_representation(self):
    post=Post(title='A good title')
    self.assertEqual(str(post), post.title)
  def test_postt_content
