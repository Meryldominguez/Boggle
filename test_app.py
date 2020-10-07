import boggle
from unittest import TestCase
from flask import session, json, request
from app import app

class RootRouteTest(TestCase):
    """tests for the / route in app.py"""
    def setUp(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                    change_session.clear()
            boggle_game = boggle.Boggle()
    def tearDown(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                    change_session.clear()
    def test_session(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['plays'], 1)
            self.assertEqual(session['high_score'], 0)
    def test_home_view(self):
        with app.test_client() as client:
        # can now make requests to flask via `client`
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle time', html)

class CheckWordTest(TestCase):
    """
    docstring
    """
    def test_check_word(self):
        with app.test_client() as client:
        # can now make requests to flask via `client`
            with client.session_transaction() as session:
                session['board']=[["T","E","S","T"]]
                print(session["board"])
                resp = client.post('/check-word', data={'word':'test'})
                html = resp.get_data(as_text=True)
                print(html)

            self.assertEqual(resp.data,{'word':'test'})

            self.assertEqual(resp.status_code, 200)

            self.assertIn('test', html)

class ScoreTest(TestCase):
    """
    docstring
    """
