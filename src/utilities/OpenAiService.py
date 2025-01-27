from typing import Optional, List, Dict, Any
from openai import AsyncOpenAI, OpenAI
from openai.types.chat import ChatCompletion
from dotenv import load_dotenv
import os
import openai

class OpenAiService:
    def __init__(
        self,
    ):
        """
        Initialize OpenAI service.
        """
        load_dotenv()
        self.api_key = os.getenv('openai.api_key')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in .env file")
        
        self.default_model = 'gpt-4o-mini'
        openai.api_key = self.api_key
        self.sync_client = OpenAI(api_key=self.api_key)
        self.async_client = AsyncOpenAI(api_key=self.api_key)

    def _prepare_messages(
        self, 
        user_prompt: str, 
        system_prompt: Optional[str] = None
    ) -> List[Dict[str, str]]:
        """
        Prepare messages for OpenAI API.
        """
        if not user_prompt.strip():
            raise ValueError("User prompt cannot be empty")

        messages = []
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt.strip()
            })
        
        messages.append({
            "role": "user",
            "content": user_prompt.strip()
        })
        
        return messages

    def _prepare_request_params(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Prepare request parameters for OpenAI API.
        """
        return {
            "model": model or self.default_model,
            "messages": messages
        }

    def ask(
        self,
        user_prompt: str,
        system_prompt: Optional[str] = None,
        model: Optional[str] = None
    ) -> str:
        """
        Synchronously send a request to OpenAI and get response.
        """
        messages = self._prepare_messages(user_prompt, system_prompt)
        params = self._prepare_request_params(messages, model)
        
        try:
            response: ChatCompletion = self.sync_client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error during OpenAI communication: {str(e)}")

    async def ask_async(
        self,
        user_prompt: str,
        system_prompt: Optional[str] = None,
        model: Optional[str] = None
    ) -> str:
        """
        Asynchronously send a request to OpenAI and get response.
        """
        messages = self._prepare_messages(user_prompt, system_prompt)
        params = self._prepare_request_params(messages, model)
        
        try:
            response = await self.async_client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error during OpenAI async communication: {str(e)}")
