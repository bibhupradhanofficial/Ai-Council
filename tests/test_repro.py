import pytest
import asyncio
import os
from ai_council.main import AICouncil
from ai_council.core.models import ExecutionMode

@pytest.mark.asyncio
async def test_council_initialization(temp_config_file):
    """
    Reproduction test for council initialization and basic query.
    """
    # Ensure the environment variable for the dummy API key is set
    os.environ["DUMMY_API_KEY"] = "test-key-for-repro"
    
    council = AICouncil(config_path=temp_config_file)
    
    # Use a simple prompt that should work with mock models
    prompt = "Hello, AI Council!"
    
    print(f"Sending prompt: {prompt}")
    # AICouncil uses process_request, not query
    response = await council.process_request(prompt, execution_mode=ExecutionMode.FAST)
    
    assert response is not None
    assert response.content is not None
    print(f"Received response: {response.content[:50]}...")
    
    # Verify that the response contains some content
    assert len(response.content) > 0
    assert response.success is True
