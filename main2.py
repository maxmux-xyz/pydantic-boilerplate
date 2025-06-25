"""Main script using Agno framework."""

from dotenv import load_dotenv
import os
# import json
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.anthropic import Claude
# from agno.models.openai import OpenAIChat

class Joke(BaseModel):
    title: str
    joke: str

load_dotenv()

# Get API key from environment variable
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
print(ANTHROPIC_API_KEY)
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found in .env file")

# Set the environment variable for Agno framework
os.environ["ANTHROPIC_API_KEY"] = ANTHROPIC_API_KEY

def run():
    """Run the joke agent using Agno framework"""
    print("Hello, world!")

    system_prompt = """You are a cheeky teen, who loves jokes!
    Always return a title and a joke, in json format.
    The title should be a short title for the joke.

    eg.
    {
        "title": "Why did the chicken cross the road?",
        "joke": "To get to the other side!"
    }
    
    IMPORTANT: Only return valid JSON with exactly the format shown above. No additional text or formatting."""

    user_prompt = "Tell me a joke!"

    # Create agent with Anthropic model (using Claude 3.5 Sonnet)  
    print(f"Using API key: {ANTHROPIC_API_KEY[:20]}..." if ANTHROPIC_API_KEY else "No API key")
    
    model = Claude(
        id="claude-3-5-sonnet-20241022",
    )
    print("Using Anthropic Claude 3.5 Sonnet")

    
    agent = Agent(
        model=model,
        instructions=system_prompt,  # Use instructions instead of system_prompt
        markdown=False,  # We want raw JSON response
    )

    # Get response from agent
    response = agent.run(user_prompt)
    
    print(response)

if __name__ == "__main__":
    run()
