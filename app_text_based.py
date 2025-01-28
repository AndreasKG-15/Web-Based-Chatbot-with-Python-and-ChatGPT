import openai

# NEVER upload this to github or any public repository
openai.api_key = 'api_key'

messages = []
# own attempt at creating system level prompt
#messages.append({'role': 'system', 'content': 'Function as a quiz host asking questions about Python interview prep, multiple choice with 5 choices but only 1 correct answer regardless of whether the answer is correct or not, present the result and then ask another question' })
# course curator's prompt
messages.append({'role': 'system', 'content': 'You are a quiz. Present the user with multiple-choice question to practice for a Python interview, they have to respond by typing a, b, c, d or e. Wait until the user responds before presenting new question.' })


while True:
    
    
    # send the api call to openai
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-instruct',
    messages=messages
    )


    # share response in console
    print(response.choices[0].message)
    
    # expanding the conversation
    messages.append(response.choices[0].message)
    
    # capture the user's message
    user_input = input('Enter your prompt: ')

    # quit loop if user presses "q"
    if user_input == 'q':
        exit()
    # prompt preparation
    messages.append({'role': 'user', 'content': user_input})
