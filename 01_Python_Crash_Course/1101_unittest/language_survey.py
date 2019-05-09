from survey import AnonymousSurvey

question = "What language do you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at anytime to quit:\n")
while True:
    response = input('Language:')
    if response == 'q':
        break
    my_survey.store_respones(response)

print('\nThank you to everyone')
my_survey.show_result()    