"""Main script."""

from dotenv import load_dotenv
import os
import asyncio
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class Joke(BaseModel):
    title: str
    joke: str

load_dotenv()

# Get API key from environment variable
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

gemini_25_flash = OpenAIModel(
    'google/gemini-2.5-flash-preview',
    provider=OpenAIProvider(
        base_url='https://openrouter.ai/api/v1',
        api_key=OPENROUTER_API_KEY,
    ),
)

async def run():
    """Run"""
    print("Hello, world!")

    system_prompt = """You are a cheeky teen, who loves jokes!
    Always return a title and a joke, in json format.
    The title should be a short title for the joke.

    eg.
    {
        "title": "Why did the chicken cross the road?",
        "joke": "To get to the other side!"
    }
    """
    user_prompt = "Tell me a joke!"

    agent = Agent(
        model=gemini_25_flash,
        system_prompt=system_prompt,
        output_type=Joke,
    )

    response = await agent.run(user_prompt)
    print(f"Title: {response.output.title}")
    print(f"Joke: {response.output.joke}")

if __name__ == "__main__":
    asyncio.run(run())
