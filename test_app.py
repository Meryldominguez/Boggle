import boggle
from unittest import TestCase
from flask import session, json, request, jsonify
from app import app

class FlaskTesting(TestCase):
    """tests for the / route in app.py"""
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    
        
    def test_session(self):
        with self.client as client:
            print(client)
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertIn('board', session)
            self.assertIn('plays', session)
            self.assertIn('high_score', session)
            
    def test_home_view(self):
        with self.client as client:
        # can now make requests to flask via `client`
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle time', html)

    def test_check_word(self):
        with self.client as client:
            with client.session_transaction() as session:
                session['board']=[["T","E","S","T"]]
        # HOW DO I TEST WHEN FRONT END IS SENDING JSON AND BACK END ISNT TESTING JSON??
                
                response = client.post('/check-word', data={'word':'test'})

                print(response)
                self.assertEqual(response.data,{'word':'test'})

                
                self.assertEqual(['result'], 'ok')

    def test_post_score(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                boggle_game = boggle.Boggle()
                session['high_score'] = 10
                resp = client.post("/score")
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(session['plays'], 1)
                self.assertEqual(session['high_score'], 0)
    def test_home_view(self):
        with app.test_client() as client:
        # can now make requests to flask via `client`
            resp = client.post('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Boggle time', html)
