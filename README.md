

# Playing 20q against an LLM 

The game is 20 questions - whereby you, the user, think of something (i.e. a dog, a coffee, a display, a football) and the AI has to guess what you are thinking of. 
The AI can ask up to 20 yes/no questions to find out what you are thinking of. You must answer yes or no truthfully. 
 
Note: 
- The AI should only play 20 questions, and should respond with an apologetic response when asked about something unrelated. 
- You are not required to train or fine tune an LLM.

## Local deployment

1. Install dependencies

```bash
pip install -r requirements.txt
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
pip install -r cdk_requirements.txt
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
