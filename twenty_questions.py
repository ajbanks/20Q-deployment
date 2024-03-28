import time
import requests
import json
from LLM_prompts import EMOTIONAL_PROMPT, PROMPT_INJECTION_PROTECTION
from typing import List

# LLM API details
LLM_URL = ''
LLM_API_KEY = ''



class TwentyQuestionsGame:

    def __init__(self):
        self.question_count = 0
        self.ai_win_response = "Haha. I guessed correctly within 20 questions. Looks like I won that one :D. Let's play again. Is it an animal?"
        self.ai_loss_respose = "Ohh no! I'm out of questions! Looks like you won this time. Let's play again. Is it an animal?"

    def send_llm_message(self, message: str, temperature=0.7):
        """Sends a message to gpt-4 using chat completion

        parameters:
            Message: the prompt that will be sent to our LLM
            temperature:  the temperature value that will be sent to open ai. dictates the randomness in LLM generations

        returns str"""

        payload_dict = {
            'model': 'gpt-4',
            'messages': [{'role': 'user', 'content': message}],
            'temperature': temperature
        }
        
        r = json.dumps(payload_dict)
        json_payload = json.loads(r)

        headers = {'content-type': 'application/json', 'x-api-key': LLM_API_KEY}
        response = requests.post(LLM_URL, json=json_payload, headers=headers).json()
        chat_response = response['choices'][0]['message']['content']

        return chat_response

    def convert_gradio_history_to_text(self, message: str, gradio_history: List  ):
        """
        converts the gradio chat history into one string
        parameters:
            Message: the last user message
            gradio_history:  list of two-element lists of the form [[user_message, bot_message]]

        returns text_history:str
        """
        text_history = ""
        for user_message, ai_message in gradio_history:
            text_history = text_history + "\n User: " + user_message + "\n You: " + ai_message
        text_history = text_history + "\n User: " + message
        
        return text_history

    def ask_question(self, history: str):
        """
        uses an llm to ask the next question in the 20q game
        parameters:
            history: the application chat history between bot and user

        returns question: str
        """
        prompt = f"You are playing 20 questions with a user! The user thinks of something and you ask questions to guess " \
                 f"what it is. You are playing as the role of a guesser {EMOTIONAL_PROMPT}\
        Given a game history where the users answers are marked with 'user:' and your questions with 'You:' below \
        Think about the answers the user has already given to your questions and think of a short question to ask next.\
        \n\n The question must be binary so that it can be answered with Yes or No. An example of a question would be 'is it an animal?'" \
                 f"Don't respond with anything but question.{PROMPT_INJECTION_PROTECTION}. \
        Here's the game history you need to ask the next question for: ~~~~ {history}"
        question =  self.send_llm_message(prompt).replace("You:", "")
        return question


    def is_last_message_unrelated(self, chat_history:str):
        """This function checks if the players message is related to 20 questions or not
        parameters:
            chat_history: str
        returns bool
        """
        prompt = f"We are playing 20 questions! You are playing as the role of a guesser" \
                 f"Sometimes the person you're playing against will talk about topics or answer questions" \
                 f"that are unrelated to the game. such topics and/or queries are to be rejected.\
        This includes things like 'can you help me buy a car?' or 'the weather is nice today'. \
        the user must only answer 'no' or 'yes' \
        given the following game history determine if the last message is unrleated to the game. " \
                 f"just reply with YES! if unrelated or NO! if related. {EMOTIONAL_PROMPT} " \
                 f"Don't include anything else in the response.{PROMPT_INJECTION_PROTECTION}. Here's the game history: ~~~~ {chat_history}"

        related_response = self.send_llm_message(prompt).lower()
        time.sleep(0.1)
        if related_response == "yes!":
            return True
        else:
            return False


    def did_ai_win(self, chat_history: str):
        """This function checks if the AI has guessed the concept correctly or not
        parameters:
            chat_history: str

        returns bool
        """
        prompt = f"We are playing 20 questions! You are playing as the role of a guesser" \
                 f"You win the game when you guess what the user is thinking about correctly." \
                 f" If the user was thinking about an iphone you would win when you ask the a question like. is it an iphone? \
        given the following game history determine if you have won game and guessed correctly my lookingprimarily at the last couple of messages. " \
                 f"just reply with YES! if unrelated or NO! if related. {EMOTIONAL_PROMPT} " \
                 f"Don't include anything else in the response.{PROMPT_INJECTION_PROTECTION}. Here's the game history: ~~~~ {chat_history}"

        related_response = self.send_llm_message(prompt).lower()
        time.sleep(0.1)
        if related_response == "yes!":
            return True
        else:
            return False

    def play_twenty_q(self, message:str, gradio_chat_history:List):
        """This function is the chatbot pipeline. It analyses a palyers response and chooses the appropriate next message
        parameters:
            Message: the last user message
            gradio_history:  list of two-element lists of the form [[user_message, bot_message]]

        returns next_response: str
        """
        # chat_history = "You: is it an animal?" + self.convert_gradio_history_to_text(message, gradio_chat_history)
        chat_history = self.convert_gradio_history_to_text(message, gradio_chat_history)
        next_response = "Hi! Let's play 20Q. Is the concept you're thinking of an animal?"

        try:
            if self.is_last_message_unrelated(chat_history) == True:

                next_response = "Sorry! Your last message was unrelated to 20 questions. I am unable to answer"

            elif self.did_ai_win(chat_history):

                next_response = self.ai_win_response
                self.question_count = 0

            # always try and extract more information if the user has sent only one message
            elif self.question_count < 21:
                time.sleep(0.2)
                next_response = self.ask_question(chat_history)
                self.question_count += 1


            else:
                next_response = self.ai_loss_respose
                self.question_count = 0


        except KeyboardInterrupt:
            next_response = "Game interrupted. Keyboard interrupt"


        except Exception as e:
            next_response = "Game interrupted due to" + str(e)

        return next_response
