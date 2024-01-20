from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core import mail
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_send_verification_code(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser'
        )
        user.send_verification_code()
        self.assertEqual(len(mail.outbox), 1)
        verification_code = user.verification_code
        self.assertIn(verification_code, mail.outbox[0].body)
class UserRegistrationTests(TestCase):
    def test_register_user(self):
        response = self.client.post('/register/', {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('test@example.com', mail.outbox[0].body)
        self.assertIn('testpassword', mail.outbox[0].body)
        self.assertIn('testuser', mail.outbox[0].body)
        self.assertIn('Account Verification Code', mail.outbox[0].subject)
        user = get_user_model().objects.get(email='test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.verification_code, mail.outbox[0].body.split()[-1])

class UserVerificationTests(TestCase):
    def test_verify_user(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='XXXXXXXXXXXX',
            username='XXXXXXXX'
        )
        user.send_verification_code()
        verification_code = user.verification_code
        response = self.client.post('/verify/', {
            'email': 'test@example.com',
            'verification_code': verification_code
        })
        self.assertEqual(response.status_code, 302)
        user = get_user_model().objects.get(email='test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.verification_code, None)
        self.assertEqual(len(mail.outbox), 0)
        self.client.logout()
class UserLoginTests(TestCase):
    def test_login_user(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='XXXXXXXXXXXX',
            username='XXXXXXXX'
        )
        response = self.client.post('/login/', {
            'email': 'test@example.com',
            'password': 'XXXXXXXXXXXX'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 0)
        self.client.logout()
        self.client.login(email='test@example.com', password='XXXXXXXXXXXX')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 0)
        self.client.logout()
        self.client.login(email='test@example.com', password='XXXXXXXXXXXX')
        response = self.client.get('/login/')

class UserPasswordResetTests(TestCase):
    def test_password_reset(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='XXXXXXXXXXXX',
            username='XXXXXXXX'
        )
        response = self.client.post('/password_reset/', {
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('test@example.com', mail.outbox[0].body)
        self.assertIn('testpassword', mail.outbox[0].body)
        self.assertIn('testuser', mail.outbox[0].body)
        self.assertIn('Account Verification Code', mail.outbox[0].subject)
        user = get_user_model().objects.get(email='test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)