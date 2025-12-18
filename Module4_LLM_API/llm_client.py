"""
LLM Client for HKBU Gen AI Services
For MSc Mathematics Students
Demonstrates IPO model for LLM API access
"""

import requests
import json
import os
from typing import List, Dict, Optional


class HKBUGenAIClient:
    """
    Client for accessing HKBU Gen AI services
    Implements Input-Process-Output model with error handling
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize LLM client
        
        Args:
            api_key: HKBU Gen AI API key (if None, reads from environment)
        """
        # INPUT: Get API key
        self.api_key = api_key or os.getenv("HKBU_GENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "API key not found. Set HKBU_GENAI_API_KEY environment variable "
                "or pass api_key parameter"
            )
        
        # Configuration
        self.endpoint = "https://genai.hkbu.edu.hk/v1/chat/completions"
        self.default_model = "gpt-4"
        self.default_temperature = 0.7
        
        print("✓ HKBU Gen AI Client initialized")
    
    def chat(self, 
             prompt: str, 
             model: Optional[str] = None,
             temperature: Optional[float] = None,
             max_tokens: int = 1000,
             system_message: Optional[str] = None) -> str:
        """
        Send a chat message to LLM
        
        INPUT:
            prompt: User message/question
            model: LLM model to use
            temperature: Creativity level (0-1)
            max_tokens: Maximum response length
            system_message: System instructions
        
        PROCESS:
            - Build request payload
            - Send to API
            - Parse response
        
        OUTPUT:
            - LLM response text
        """
        # ===== INPUT VALIDATION =====
        if not prompt:
            raise ValueError("Prompt cannot be empty")
        
        # ===== PROCESS: Build request =====
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        messages.append({"role": "user", "content": prompt})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model or self.default_model,
            "messages": messages,
            "temperature": temperature or self.default_temperature,
            "max_tokens": max_tokens
        }
        
        # ===== PROCESS: Send request =====
        try:
            response = requests.post(
                self.endpoint, 
                headers=headers, 
                json=payload,
                timeout=30
            )
            
            # Check status
            if response.status_code != 200:
                raise Exception(
                    f"API Error {response.status_code}: {response.text}"
                )
            
            # ===== PROCESS: Parse response =====
            data = response.json()
            
            # ===== OUTPUT =====
            return data['choices'][0]['message']['content']
            
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Please try again.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except (KeyError, IndexError) as e:
            raise Exception(f"Unexpected response format: {e}")
    
    def analyze_data(self, data_summary: str, question: str) -> str:
        """
        Ask LLM to analyze data
        
        INPUT: Data summary and specific question
        PROCESS: Format prompt and send to LLM
        OUTPUT: Analysis response
        """
        prompt = f"""
I have the following data summary:

{data_summary}

Question: {question}

Please provide a detailed analysis.
"""
        
        system_message = "You are a data analyst helping with statistical interpretation."
        
        return self.chat(
            prompt=prompt,
            system_message=system_message,
            temperature=0.3  # Lower temperature for factual analysis
        )
    
    def generate_code(self, task_description: str, language: str = "python") -> str:
        """
        Ask LLM to generate code
        
        INPUT: Task description and programming language
        PROCESS: Send code generation request
        OUTPUT: Generated code
        """
        prompt = f"""
Generate {language} code for the following task:

{task_description}

Please provide clean, well-commented code with examples.
"""
        
        system_message = f"You are an expert {language} programmer."
        
        return self.chat(
            prompt=prompt,
            system_message=system_message,
            temperature=0.2  # Low temperature for precise code
        )
    
    def summarize_text(self, text: str, max_words: int = 200) -> str:
        """
        Ask LLM to summarize text
        
        INPUT: Text to summarize
        PROCESS: Send summarization request
        OUTPUT: Summary
        """
        prompt = f"""
Summarize the following text in approximately {max_words} words:

{text}
"""
        
        return self.chat(prompt=prompt, temperature=0.5)
    
    def explain_concept(self, concept: str, level: str = "undergraduate") -> str:
        """
        Ask LLM to explain a concept
        
        INPUT: Concept name and education level
        PROCESS: Request explanation
        OUTPUT: Explanation text
        """
        prompt = f"""
Explain {concept} at a {level} level.

Include:
1. Definition
2. Key concepts
3. Example
4. Practical applications
"""
        
        system_message = "You are a mathematics professor."
        
        return self.chat(
            prompt=prompt,
            system_message=system_message,
            temperature=0.6
        )


# ===================================================================
# Example Usage
# ===================================================================

def example_basic_chat():
    """Example: Basic chat interaction"""
    print("\n=== Example 1: Basic Chat ===")
    
    client = HKBUGenAIClient()
    
    response = client.chat("What is the Central Limit Theorem?")
    print(response)


def example_data_analysis():
    """Example: Data analysis assistance"""
    print("\n=== Example 2: Data Analysis ===")
    
    client = HKBUGenAIClient()
    
    data_summary = """
Dataset: Student Scores
Mean: 85.5
Median: 87.0
Std Dev: 6.2
Min: 76
Max: 95
N: 8
"""
    
    response = client.analyze_data(
        data_summary=data_summary,
        question="What can we infer about the distribution of scores?"
    )
    print(response)


def example_code_generation():
    """Example: Code generation"""
    print("\n=== Example 3: Code Generation ===")
    
    client = HKBUGenAIClient()
    
    task = "Create a function that calculates the correlation coefficient between two lists of numbers"
    
    code = client.generate_code(task)
    print(code)


def example_concept_explanation():
    """Example: Concept explanation"""
    print("\n=== Example 4: Concept Explanation ===")
    
    client = HKBUGenAIClient()
    
    explanation = client.explain_concept(
        concept="Bayesian Inference",
        level="graduate"
    )
    print(explanation)


if __name__ == "__main__":
    print("HKBU Gen AI Client - Examples")
    print("=" * 60)
    
    # Check if API key is set
    if not os.getenv("HKBU_GENAI_API_KEY"):
        print("⚠️  Warning: HKBU_GENAI_API_KEY not set")
        print("Set it with: export HKBU_GENAI_API_KEY='your_key_here'")
        print("\nShowing code structure only (API calls will fail)")
    
    # Run examples
    try:
        example_basic_chat()
        example_data_analysis()
        example_code_generation()
        example_concept_explanation()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure your API key is set correctly.")

