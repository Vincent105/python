import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """針對AnonymousSurvey類進行測試"""
    def test_store_single_response(self):
        """測試單個答案會被妥善儲存"""
        question = "What language do you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_respones('English') 

        self.assertIn('English', my_survey.respones)

    def test_store_three_response(self):
        question = "What language do you first learn to speak?"        
        my_survey = AnonymousSurvey(question)
        
        respones = ['English', 'Spanish', 'Mandarin']
        for respone in respones:
            my_survey.store_respones(respone)

        for respone in respones:     
            self.assertIn(respone, my_survey.respones)            

unittest.main()
