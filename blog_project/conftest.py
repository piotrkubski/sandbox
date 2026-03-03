import pytest
from blog.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.fixture
def user():
    user = User.objects.create_user(
        username="user",
        email="",
        password="password",
    )
    return user

@pytest.fixture
def short_post(user):
    post = Post.objects.create(
        title="short post",
        content='word ' * 100,
        author=user,
    )
    return post

@pytest.fixture
def long_post(user):
    post = Post.objects.create(
        title="long post",
        content='word ' * 1500,
        author=user,
    )
    return post