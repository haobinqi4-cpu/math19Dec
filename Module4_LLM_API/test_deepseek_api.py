"""
Test script to verify DeepSeek API connectivity as an alternative
"""

import requests
import os

def test_deepseek_api_connection():
    """Test basic API connectivity with DeepSeek API"""
    
    # Get API key from the DeepSeek.md file
    api_key = "sk-fd26f4bdfb894f9683832ff055039728"
    
    # DeepSeek API endpoint
    endpoint = "https://api.deepseek.com/v1/chat/completions"
    
    # Test prompt
    prompt = "Hello, this is a test message. Please respond with 'API connection successful' if you receive this."
    
    # Request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    print("Testing DeepSeek API connection...")
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
    test_deepseek_api_connection()