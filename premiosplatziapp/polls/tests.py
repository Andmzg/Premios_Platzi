import datetime

from django.urls.base import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    """Create question whit a date"""
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(pk, choice_text, vote = 0):
    """Create choice whit Pimary Key and vote = 0""" 
    question = Question.objects.get(pk=pk)
    return question.choice_s.create(choice_text=choice_text, votes=votes)

# class QuestionModelTests(TestCase):
    
#     def test_was_published_recently_with_future_questions(self):
#         """was_publiched_recently returns false for questions 
#             whose pub_date is in the future
#         time = timezone.now() + datetime.timedelta(days=1)
#         future_question = Question(question_text="Quien es el mejor CD de platzy?", pub_date = time)"""
#         question = create_question("mejor profesor de plazi?", 30)
#         self.assertIs(question.was_published_recently(), False)
        
    
#     def test_was_published_recently_whit_past_questions(self):
#         """was_published_recently returns True for questions
#         whose pub_case is pasta 1 day """
        
#         question = create_question("mejor profesor de plazi?", -30)
#         self.assertIs(question.was_published_recently(),False)
        
#     def test_was_published_recently_whit_present_questions(self):
#         """was_published_recently returns True for questions
#         whose pub_case is now """
        
#         question = create_question("mejor profesor de plazi?", 0)
#         self.assertIs(question.was_published_recently(),True)
        

class QuestionIndexViewTest(TestCase):
    # def test_no_questions(self):
    #     """Is no question exisst, an approiate message is displayed"""
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "No polls are avalible.")
    #     self.assertQuerysetEqual(response.context["latest_question_list"],[])
        
    # def test_No_future_question(self):
    #     """Display all question except future questions"""
    #     question = create_question("mejor profesor de plazi?", 29)
    #     response = self.client.get(reverse("polls:index"))
    #     """ we can use this self.assertNotIn(question, response.context['latest_question_list'])
    #     but the test works whit temporaly database, so in this database there are not any question
    #     niether this new becouse will create at the future. Para mejor entendiemiento
    #     usaremos la sguiente anotacion."""
    #     self.assertContains(response, "No polls are avalible.")
    #     self.assertQuerysetEqual(response.context["latest_question_list"],[] )
        
    # def test_past_question(self):
    #     """
    #     Question whit a pub_date in the past are diosplayed on the index page
    #     """
    #     question = create_question("mejor profesor de plazi?", -10)
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(response.context["latest_question_list"],[question] )

    # def test_future_question_and_past_question(self):
    #     """
    #     Even if both and past future question exist, only past question are displayed
    #     """
    #     past_question = create_question("past question", -30)
    #     future_question = create_question("Future question", 30)
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(
    #         response.context["latest_question_list"], [past_question]
    #     )
        
    # def test_two_past_questions(self):
    #     """"
    #     the question index page may display multiple quesions.
    #     """
    #     past_question_1 = create_question("past question 1", -30)
    #     past_question_2 = create_question("past question 2", -40)
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(
    #         response.context["latest_question_list"], [past_question_1, past_question_2]
    #     )
        
    # def test_two_future_questions(self):
    #     """
    #     The question page no display any questions.
    #     """
    #     future_question_1 = create_question("Future question 1", 30)
    #     future_question_2 = create_question("Future question 2", 40)
    #     response = self.client.get(reverse("polls:index"))
    #     self.assertQuerysetEqual(
    #         response.context["latest_question_list"], []
    #     )
        
    def test_question_without_choice(self):
        """A question wont be display if not has a choice"""
        question = create_question("Question 1", days = 0)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], []
        )
        
    def test_question_with_choise(self):
        """a question will be display if has a choice"""
        question = create_question("Quiestion 1", days = 0)
        choice_1 = create_choice(question.id, "choice 1")
        choice_2 = create_choice(question.id, "choice 2")
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question]
        )

# class QuestionDetailViewTests(TestCase):

#     def test_futute_question(self):
#         """
#         The datail view of a question with 
#         a pub_date in the future return a 404 error not found
#         """
#         future_question = create_question("Future_question", 30)
#         url = reverse("polls:details", args=(future_question.id, ))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)
    
#     def test_past_question(self):
#         """
#         The datail view of a question with 
#         a pub_date in the vew display qeustion_text
#         """
#         past_question = create_question("past_question", -30)
#         url = reverse("polls:details", args=(past_question.id, ))
#         response = self.client.get(url)
#         self.assertContains(response, past_question.question_text)
        
# class QuestionResultsViewTests(TestCase):
    
#     def questions_without_choice(self):
#         """
#         Our tests would create a Question without Choices and then 
#         test that it’s not published, as well as create a similar 
#         Question with Choices, and test that it is published.
#         """
#         question = create_question("is a new question?", days = 0)
        