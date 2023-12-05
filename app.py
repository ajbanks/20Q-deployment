import gradio as gr
from twenty_questions import Twenty_Questions_Game
import random

twenty_question_game = Twenty_Questions_Game()

def twenty_questions(message, history):
    random_num = random.randrange(1,100)
    result = f"this is a test result {random_num}"
    # twenty_question_game.next_round(message, history)
    return result


demo = gr.ChatInterface(
    fn=twenty_questions,
    inputs=gr.Textbox(placeholder="Let's play 20Q!"),
    outputs="response",
    interpretation="default",
    allow_flagging="never",
    analytics_enabled=False
)

demo.launch(
    server_port=8080,
    # server_name="0.0.0.0",
    enable_queue=False,
)
