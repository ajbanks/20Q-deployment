

# Lead ML Engineer - technical task - LLM 


We would like you to create an application that can play 20 Questions, using a State-of-the-art AI model to guess the answer. 
Rules of the game: 
The game is 20 questions - whereby you, the user, think of something (i.e. a dog, a coffee, a display, a football) and the AI has to guess what you are thinking of. 
The AI can ask up to 20 yes/no questions to find out what you are thinking of. You must answer yes or no truthfully. 
Task 
This is an exercise designed to test your ability to design an end-to-end solution, rather than optimising for a specific task, so it is recommended not to spend too much time fine-tuning each step of the following process. 
1. Create an architecture diagram for a solution to this problem - think carefully about how you would deploy this in a cost effective manner in a cloud environment. Cloud best practices (e.g. serverless where possible and relevant) will be appreciated - AWS preferred but not strictly required. If possible, make reference to the named services you would use at each step. 
2. Discuss the following 
a. How do different components interact with each other and why you have chosen this approach - include a short discussion of the other options 
considered and why you did not choose them. 
b. Explain the decisions behind the model and components you decided might best suit this task 
c. Briefly explain any deployment steps necessary and why you chose this method.
3. Produce code and running instructions for this (email zip file or link to a GH repo). We are looking for your ability to write production ready code in Python. 
The resulting submission should be able to be played with a reasonable speed. Some latency is understandable but should not be excessive. 
Note: 
- The AI should only play 20 questions, and should respond with an apologetic response when asked about something unrelated. 
- You are not required to train or fine tune an LLM. You should be able to do this challenge using an LLM available over API (see below) or self hosted. - We will not deploy your submission in our own environment, therefore it is not necessary for you to deploy to the cloud and provide us a link. We will however take careful consideration of submitted code and infrastructure as code - so having a loosely working submission is useful for us to understand how one would deploy this. - We do not expect you to incur any expense in undertaking this assignment 
In case you require access to a LLM service 
We have provided a free LLM proxy available at the following URL: 
https://candidate-llm.extraction.artificialos.com 
The specification of this API is almost identical to 
https://platform.openai.com/docs/api-reference/ 
The Key exception is that your api key must be passed in a header called: x-api-key rather than the Authorization header. 
The required header is below and your personal key will be provided with your assignment via email: 
x-api-key: <API_CANDIDATE_KEY>



## Local Development

1. Install dependencies

```bash
pip install -r requirements/requirements.txt
```

2. Run the application

```bash
python app.py
```

## Deploying to AWS Lambda

1. install the AWS CDK CLI

```bash
npm install -g aws-cdk
```

2. Install dependencies

```bash
pip install -r requirements/cdk_requirements.txt
```

3. Bootstrap the CDK

_[optional]: export aws profile_
```
export AWS_PROFILE=hf-sm
```

Boostrap project in the cloud
```
cdk bootstrap
```

4. Deploy Gradio application to AWS Lambda

```bash
cdk deploy 
```

1. Delete AWS Lambda again

```bash
cdk destroy
```
