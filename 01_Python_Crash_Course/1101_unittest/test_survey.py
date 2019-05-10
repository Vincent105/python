import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """針對AnonymousSurvey類進行測試"""
    def setUp(self):
        question = "What language do you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """測試單個答案會被妥善儲存"""
        self.my_survey.store_respones(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.respones)

        self.my_survey.store_respones(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.respones)

    def test_store_three_response(self):
        for respone in self.responses:
            self.my_survey.store_respones(respone)

        for respone in self.responses:     
            self.assertIn(respone, self.my_survey.respones)            

unittest.main()
