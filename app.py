import gradio as gr
from twenty_questions import Twenty_Questions_Game
import random

twenty_question_game = Twenty_Questions_Game()

def twenty_questions(message, history):
    """list of two-element lists of the form [[user_message, bot_message"""
    chat_message = twenty_question_game.play_twenty_q(message, history)
    return chat_message


demo = gr.ChatInterface(
    fn=twenty_questions,
    description="Play 20Q with our AI by answering it's questions!",
    title="20 questions game",
    textbox=gr.Textbox(placeholder="Is it an animal?")
)

demo.launch(
    server_port=8080)
#     # server_name="0.0.0.0"
# )
