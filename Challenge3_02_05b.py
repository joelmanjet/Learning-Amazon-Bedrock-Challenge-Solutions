#Imports
import boto3
from langchain.llms.bedrock import Bedrock

#Create the bedrock client
boto3_client = boto3.client('bedrock-runtime')

#setting model inference parameters
infrence_modifier = {
  "temperature" : 0.3,
  "top_p" : 1,
  "max_tokens_to_sample" : 10000
      }

#Create the llm
llm = Bedrock(
  model_id = "anthropic.claude-instant-v1",
  client = boto3_client,
  model_kwargs = infrence_modifier
)

#Generate the response
response = llm.invoke("""
    Human: Write an email from Mark, Hiring Manager, 
    welcoming a new employee "John Doe" to the company on his first day.
    
    Answer: """)

#Display the result
print(response)
