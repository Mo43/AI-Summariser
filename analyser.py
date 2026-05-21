import os
import fitz
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, tool

load_dotenv()

#free cloud model hugging face 
model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct") 

#smart agent
agent = CodeAgent(tools=[], model=model)

print("\n--- Triggering the AI Agent ---")
response = agent.run("x")
print("\nAgent Response:")
print(response)













