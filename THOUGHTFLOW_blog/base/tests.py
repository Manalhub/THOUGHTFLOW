from django.test import TestCase

# Create your tests here.

# test_models.py
from django.contrib.auth.models import User

from profiles.models import Userprofile
from .models import Post, Category, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            body='This is a test post',
            category='Test Category'
        )

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(self.post.__str__(), self.post.title)
    
    
    def test_post_get_absolute_url(self):
        url = self.post.get_absolute_url()
        self.assertEqual(url, f"/read_post/{self.post.id}/{self.post.slug}/")

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.title)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            body='This is a test post',
            category='Test Category'
        )
        self.comment = Comment.objects.create(
            author='Commenter',
            comment_p=self.post,
            body='This is a test comment'
        )

    def test_comment_creation(self):
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(self.comment.__str__(), f"Comment by {self.comment.author} on {self.comment.comment_p}")

# test_views.py
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment, User

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Userprofile.objects.create(person=self.user)
        self.category = Category.objects.create(title='Test Category')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='This is a test post',
            category='Test Category'
        )
        self.comment = Comment.objects.create(
            author='Commenter',
            comment_p=self.post,
            body='This is a test comment'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_categories_view(self):
        response = self.client.get(reverse('post_categories', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_post'), {
            'title': 'Another Test Post',
            'body': 'This is another test post',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful post creation

    def test_read_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('read_post', args=[self.post.id, self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_update_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_post', args=[self.post.id]), {
            'title': 'Updated Test Post',
            'body': 'This is an updated test post'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful post update

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful post deletion

    def test_delete_comment_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful comment deletion

    def test_update_comment_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_comment', args=[self.comment.id]), {
            'body': 'Updated comment body'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful comment update

# test_forms.py
from .forms import POSTForm, COMForm
from .models import Post, Comment

class PostFormTest(TestCase):
    def test_post_form_valid(self):
        form = POSTForm(data={
            'title': 'Test Title',
            'body': 'Test body',
            'image': None
        })
        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        form = POSTForm(data={})
        self.assertFalse(form.is_valid())

class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form = COMForm(data={
            'body': 'Test comment body'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = COMForm(data={})
        self.assertFalse(form.is_valid())
