import json

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
)

from ai.prompt_templates import SYSTEM_PROMPT


class OpenAIClient:

    def __init__(self):

        if not OPENAI_API_KEY:

            raise ValueError(
                "OPENAI_API_KEY is missing."
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def generate_scan_plan(
        self,
        prompt: str
    ):

        response = self.client.chat.completions.create(

            model=OPENAI_MODEL,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0

        )

        content = response.choices[0].message.content

        return json.loads(content)