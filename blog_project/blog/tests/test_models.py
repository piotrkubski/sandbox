import pytest


@pytest.mark.django_db
def test_word_count(short_post):
    assert short_post.word_count() == 100

@pytest.mark.django_db
def test_reading_time_long_post(long_post):
    assert long_post.reading_time() == 7

@pytest.mark.django_db
def test_reading_time_short_post(short_post):
    assert short_post.reading_time() == 1

@pytest.mark.django_db
def test_is_long(short_post):
    assert short_post.is_long is False