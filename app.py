import gradio as gr
from twenty_questions import Twenty_Questions_Game
import random

twenty_question_game = Twenty_Questions_Game()

def twenty_questions(message, history):
    """
    function that plays the 20q game. Two parameters

    parameters:
        Message: the last user message
        gradio_history:  list of two-element lists of the form [[user_message, bot_message]]

    returns chat_message:str
    """
    bot_message = twenty_question_game.play_twenty_q(message, history)
    history.append((message, bot_message))
    return "", history


# create chatbot using gradio
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(value=[["", "Let's play 20 questions. I'll start! Is it an animal?"]])
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(twenty_questions, [msg, chatbot], [msg, chatbot], queue=False)

demo.launch(
    server_port=8080)
