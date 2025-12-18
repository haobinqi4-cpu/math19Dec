"""
Test script to verify Moonshot AI (Kimi) API connectivity as an alternative
"""

import requests
import os

def test_moonshot_api_connection():
    """Test basic API connectivity with Moonshot AI API"""
    
    # Get API key from the GenAIkey.md file
    api_key = "4835c309-05ab-4f21-a67b-6a5e8c7d657c"
    
    # Moonshot AI endpoint from the documentation
    endpoint = "https://api.moonshot.cn/v1/chat/completions"
    
    # Test prompt
    prompt = "Hello, this is a test message. Please respond with 'API connection successful' if you receive this."
    
    # Request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "model": "moonshot-v1-8k",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    print("Testing Moonshot AI API connection...")
    print(f"Endpoint: {endpoint}")
    print(f"API Key (first 8 chars): {api_key[:8]}...")
    
    try:
        # Send request
        response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            llm_response = data['choices'][0]['message']['content']
            print("Success! API Response:")
            print("-" * 40)
            print(llm_response)
            print("-" * 40)
            return True
        else:
            print(f"API Error: {response.status_code}")
            print(response.text)
            return False
            
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return False

if __name__ == "__main__":
    test_moonshot_api_connection()