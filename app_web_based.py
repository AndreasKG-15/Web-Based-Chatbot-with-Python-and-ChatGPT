import gradio as gr
import openai



# NEVER upload this to github or any public repository
openai.api_key = 'api_key'

messages = []
# own attempt at creating system level prompt
#messages.append({'role': 'system', 'content': 'Function as a quiz host asking questions about Python interview prep, multiple choice with 5 choices but only 1 correct answer regardless of whether the answer is correct or not, present the result and then ask another question' })
# course curator's prompt
messages.append({'role': 'system', 'content': 'You are a quiz. Present the user with multiple-choice question to practice for a Python interview, they have to respond by typing a, b, c, d or e. Wait until the user responds before presenting new question.' })

def respond(history, new_message):
    
    # add the user input to the messages
    messages.append({'role': 'user', 'content': new_message})
    # api call
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turbo-instruct', messages = messages)
    # obtain response text
    assistant_message = response.choices[0].message
    messages.append(assistant_message)
    
    return history + [[new_message, assistant_message.content]]

with gr.Blocks() as my_bot:
    chatbot = gr.Chatbot()
    user_input = gr.Text()
    
    
    
    user_input.submit(respond, [chatbot, user_input], chatbot)
my_bot.launch()