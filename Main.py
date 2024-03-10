import unittest
# Creating unit tests.

# 1 Choose four distinct user stories.
## 1) As a user, I need to have the app send me a push notification not only when someone has sent me a message but also to keep me on track with my study schedule. 
## 2) As a user I want the app to be exclusive to Uni students
## 3) As a Student, I need the application to have some kind of authentication using university e-mail or student IDs so that only genuine users from the respective universities would be able to get access.
## 4) As a user I need to be able to send messages to other users

class User():
    """This is my build for a user of the application"""
    def __init__(self, student_id=None, school=None, email=None, send_message=None):
        """
        Initializes a user with optional student ID, school, and email.
        
        Args:
            student_id (int): The student ID of the user.
            school (str): The school/uni of the user.
            email (str): The email address of the user.
        """
        self.school = school
        self.student_id = student_id 
        self.email = email
        self.notification_received = False
        self.access = False
        self.send_message = send_message 

    def uni_student(self):
        """
        Grants access to the user if they belong to a university.
        """
        self.access = True
    def can_access(self):
        """
        Checks if the user can access the app based on their school.
        
        Returns:
            bool: True if the user's school is 'Háskóli' or 'Uni', False otherwise.
        """
        if self.school == "Háskóli" or self.school == "Uni":
            return True
        if self.school == "Menntaskóli":
            return False
        self.uni_student()
    def receive_message(self):
        """
        Sets the notification_recievred to True when the user receives a message.
        """
     
        self.notification_received = True 
    def schedule_update(self):
        """
        Sets the notification_recievred to True when the users schedule gets updated.
        """
        self.notification_received = True
    def auth_user_id(self):
        """
        Authenticates the user's student ID.
        
        Returns:
            bool: True if the student ID is an integer, False otherwise.
        """
        if type(self.student_id) == str:
            return False
        elif type(self.student_id) == int:
            return True
    def auth_user_email(self):
        """
        Validates the user's email address.
        
        Returns:
            bool: True if the student email is a string, False otherwise.
        """
        if type(self.email) == str:
            return True
        elif type(self.email) == int:
            return False
    def send_message_conformation(self):
        if self.send_message == "":
            return False
        elif self.send_message is None:
            return False
        else:
            return True
        
        

## User Story 1)
class TestPushNotifications(unittest.TestCase):
    """
    This class tests the push notifications
    that the user receives.
    There are three functions which test various notifications the system should be able to perform.
    """
    def test_message_notification(self):
        """
        this method tests the systems ability to send the user push notification
        upon receiving a message, either from other users or even from the system Admin.
        """
        user = User()
        user.receive_message()
        self.assertTrue(user.notification_received)
        """Assert that the result indicates success"""

    def test_schedule_notif(self):
        """
        this method tests the systems ability to send the user push notification
        when the user has something coming up, things the system should be able to notify about.
        1. 
        """
        user = User()
        user.schedule_update()
        self.assertTrue(user.notification_received)
        """Assert that the result indicates success"""


## Task 2
class TestExclusivity(unittest.TestCase):
    """
    Tests for app exclusivity based on the user's school.
    """
    def test_exclusivity(self):
        """
        Test if only uni students can access the app.
        """
        non_uni_user= User(school="Menntaskóli")
        uni_user = User(school="Háskóli")
        self.assertFalse(non_uni_user.can_access())
        """Assert that the result indicates failure"""
        self.assertTrue(uni_user.can_access())
        """Assert that the result indicates success"""

## Task 3 
class TestLoginAuth(unittest.TestCase):
    """
    Tests for user authentication based on student ID and email.
    """
    def test_student_id(self):
        """
        Test if user authentication based on student ID works correctly.
        """
        real_user = User(student_id=333000)
        fake_user = User(student_id="hello")
        """Here I created two hypothetical users, one with a valid student id and one not"""
        self.assertTrue(real_user.auth_user_id())
        """Assert that the result indicates success"""
        self.assertFalse(fake_user.auth_user_id())
        """Assert that the result indicates failure"""
    def test_email(self):
        """
        Test if user authentication based on email works correctly.
        """
        real_user = User(email="Student@ru.is")
        fake_user = User(email=58008)
        """Here I created two hypothetial users, one with a valid studetn id and one not"""
        
        self.assertFalse(fake_user.auth_user_email())
        """Assert that the result indicates failure"""
        self.assertTrue(real_user.auth_user_email())
        """Assert that the result indicates Success"""

## Task 4
class TestSendMessages(unittest.TestCase):
    """
    Tests for sending messages functionality.
    """

    def test_send_message(self):
        """
        Test if a user can successfully send a message to another user.
        """
        user1 = User(send_message="New message")
        user1.send_message_conformation()
        self.assertTrue(user1.send_message)
        
    def test_send_message_failure(self):
        """
        Test if a user fails to send a message due to invalid recipient.
        """
        user1 = User(send_message="")
        self.assertFalse(user1.send_message_conformation())

if __name__ == "__main__":
    unittest.main()