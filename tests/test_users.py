import pytest
from django.contrib.auth.models import User


def test_new_user(new_user1):
    print(new_user1.first_name)
    assert new_user1.first_name == "MyName"
    
def test_new_staff_user(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff

