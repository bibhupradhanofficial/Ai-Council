import sys
import os
import yaml
from pathlib import Path

# Add current directory to path
sys.path.append(os.getcwd())

from ai_council.main import AICouncil
from ai_council.utils.config import AICouncilConfig

def debug_init():
    try:
        # Create a dummy config dict
        config_dict = {
            "execution": {
                "default_mode": "balanced",
                "max_parallel_executions": 5,
                "max_retries": 3,
                "default_timeout_seconds": 60.0,
                "enable_arbitration": True,
                "enable_synthesis": True
            },
            "models": {
                "test-model": {
                    "enabled": True,
                    "provider": "test",
                    "api_key_env": "TEST_API_KEY",
                    "capabilities": ["reasoning"],
                    "cost_per_input_token": 0.00001,
                    "cost_per_output_token": 0.00003,
                    "max_context_length": 8192
                }
            }
        }
        
        # Write to a temp file
        config_file = Path("debug_config.yaml")
        with open(config_file, 'w') as f:
            yaml.dump(config_dict, f)
            
        print(f"Loading config from {config_file.absolute()}")
        config = AICouncilConfig.from_file(config_file)
        print("Config loaded successfully")
        
        print("Initializing AICouncil...")
        council = AICouncil(config_path=config_file)
        print("AICouncil initialized successfully")
        
        # Cleanup
        if config_file.exists():
            config_file.unlink()
            
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_init()
