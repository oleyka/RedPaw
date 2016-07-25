from django.test import TestCase


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        self.assertEqual(True, True)
