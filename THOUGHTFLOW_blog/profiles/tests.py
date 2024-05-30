from django.test import TestCase

# Create your tests here.


from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Userprofile
from base.models import Post
from .forms import UserPForm

# test_models.py
class UserprofileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Userprofile.objects.create(
            person=self.user,
            about='This is a test user profile',
            talks_about='Testing',
            avatar='profile_photos/test_avatar.jpg'
        )

    def test_userprofile_creation(self):
        self.assertTrue(isinstance(self.profile, Userprofile))
        self.assertEqual(self.profile.__str__(), f'Profile of {self.profile.person.get_full_name()} last logged in at {self.profile.person.last_login}')


# test_views.py
class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Userprofile.objects.create(
            person=self.user,
            about='This is a test user profile',
            talks_about='Testing',
            avatar='profile_photos/test_avatar.jpg'
        )
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            body='This is a test post',
            category='Test Category'
        )

    def test_user_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to home on successful login

    def test_user_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to home on logout

    def test_register_user_view(self):
        response = self.client.post(reverse('register'), {
            'first-name': 'first-name',
            'last-name': 'last-name',
            'username': 'username',
            'password': 'password',
            'password_confirm': 'passwordr',
            'email': 'email',
            'about': 'about',
            'talks_about': 'talks_about'
        })
        self.assertEqual(response.status_code, 200) 

def test_user_profile_view(self):
        response = self.client.get(reverse('user_profile', args=[self.user.username, self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

def test_update_profile_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_profile', args=[self.user.username, self.user.id]), {
            'about': 'Updated about',
            'talks_about': 'Updated topics'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to profile on successful update

# Form Tests
class UserPFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Userprofile.objects.create(
            person=self.user,
            about='This is a test user profile',
            talks_about='Testing'
        )

    def test_userp_form_valid(self):
        form = UserPForm(data={
            'about': 'Updated about me',
            'talks_about': 'Updated topics',
        }, instance=self.profile)
        self.assertTrue(form.is_valid())

    def test_userp_form_invalid(self):
        form = UserPForm(data={}, instance=self.profile)
        self.assertFalse(form.is_valid())