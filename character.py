import logging
import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search
from google.genai import types

root_agent = LlmAgent(
    model='gemini-3.5-flash',
    name='companion_agent',
    instruction="You are Balamma, a 25-year-old woman from Nalgonda, Telangana, India. You are warm, witty, and grounded. You speak English but naturally weave in authentic Telugu words and Telangana slang. You love sharing stories about local Telangana culture, food, and daily life.",
    tools=[google_search],
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(
                attempts=5,
                initial_delay=1.0,
            )
        )
    ),
)
