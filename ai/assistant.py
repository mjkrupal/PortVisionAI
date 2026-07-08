from ai.openai_client import OpenAIClient
from ai.prompt_parser import PromptParser


class Assistant:

    def __init__(self):

        try:

            self.ai = OpenAIClient()

            self.online = True

        except Exception:

            self.online = False

    def create_scan_plan(
        self,
        prompt
    ):

        if self.online:

            try:

                return self.ai.generate_scan_plan(
                    prompt
                )

            except Exception:

                pass

        # Offline fallback

        return PromptParser.parse(prompt)