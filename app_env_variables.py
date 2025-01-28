import openai
import os

# pass the api key
# NEVER upload this to Github
openai.api_key = os.environ.get('OPENAI_API_KEY')


# define the prompt
messages = []
messages.append({'role': 'user', 'content': 'what color is the sky?'})

try:
    # make an api call
    response = openai.completions.create(model = 'gpt-3.5-turbo-instruct', prompt = messages, n = 2)

    # print the response
    print(response.choices[0].message.content)
except openai.AuthenticationError:
    print('no valid token / authentication error')
except openai.BadRequestError as e:
    print('invalid request, read the manual!')
    print(e)