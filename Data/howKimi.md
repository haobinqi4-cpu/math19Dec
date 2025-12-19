# Moonshot AI (Kimi) API Documentation

## Overview

Moonshot AI provides HTTP-based API services and is compatible with OpenAI SDK for most APIs. This documentation covers how to use the Kimi Chat API.

**Official Documentation**: https://platform.moonshot.cn/docs/api/chat

## Basic Information

### Public Service Endpoint

The base URL for Moonshot API is:
```
https://api.moonshot.cn/v1
```

### Authentication

All API requests require authentication using an API key. Include your API key in the request headers:

```
Authorization: Bearer YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual API key from the Moonshot platform.

## Quick Start

### Single Turn Conversation

Moonshot API is compatible with OpenAI SDK. You can use OpenAI's official SDKs for Python and Node.js.

#### Python Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

#### Node.js Example

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_MOONSHOT_API_KEY',
  baseURL: 'https://api.moonshot.cn/v1',
});

const response = await client.chat.completions.create({
  model: 'moonshot-v1-8k',
  messages: [
    { role: 'user', content: 'Hello!' }
  ],
});

console.log(response.choices[0].message.content);
```

#### cURL Example

```bash
curl https://api.moonshot.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_MOONSHOT_API_KEY" \
  -d '{
    "model": "moonshot-v1-8k",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

**Note**: 
- Python version should be at least 3.7.1
- Node.js version should be at least 18
- OpenAI SDK version should be at least 1.0.0

### Multi-Turn Conversation

For multi-turn conversations, you can pass the conversation history in the messages array:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a high-level programming language..."},
    {"role": "user", "content": "Can you give me an example?"}
]

response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=messages
)

print(response.choices[0].message.content)
```

**Important**: As the conversation progresses, the number of tokens increases linearly. Consider optimization strategies such as keeping only the most recent conversation turns.

## API Reference

### Chat Completion

#### Request Endpoint

```
POST https://api.moonshot.cn/v1/chat/completions
```

#### Request Headers

```
Content-Type: application/json
Authorization: Bearer YOUR_API_KEY
```

#### Request Body

```json
{
  "model": "moonshot-v1-8k",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 1000,
  "stream": false
}
```

#### Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| model | string | Yes | Model identifier (e.g., "moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k") |
| messages | array | Yes | Array of message objects with role and content |
| role | string | Yes | Message role: "system", "user", or "assistant" |
| content | string | Yes | Message content |
| temperature | number | No | Sampling temperature (0-2), default 1 |
| max_tokens | integer | No | Maximum tokens to generate |
| stream | boolean | No | Whether to stream the response, default false |
| top_p | number | No | Nucleus sampling parameter |
| frequency_penalty | number | No | Frequency penalty (-2.0 to 2.0) |
| presence_penalty | number | No | Presence penalty (-2.0 to 2.0) |

#### Available Models

- `moonshot-v1-8k`: 8K context window
- `moonshot-v1-32k`: 32K context window
- `moonshot-v1-128k`: 128K context window

#### Response Format (Non-Stream)

```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "moonshot-v1-8k",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 8,
    "total_tokens": 18
  }
}
```

#### Response Format (Stream)

When `stream: true`, the response is sent as Server-Sent Events (SSE):

```
data: {"id":"chatcmpl-xxx","object":"chat.completion.chunk","created":1234567890,"model":"moonshot-v1-8k","choices":[{"index":0,"delta":{"role":"assistant","content":"Hello"},"finish_reason":null}]}

data: {"id":"chatcmpl-xxx","object":"chat.completion.chunk","created":1234567890,"model":"moonshot-v1-8k","choices":[{"index":0,"delta":{"content":"!"},"finish_reason":null}]}

data: [DONE]
```

#### Streaming Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

stream = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "user", "content": "Tell me a story"}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Vision Models

Moonshot API supports vision models that can process images. When using vision models, the `message.content` field changes from a string to a list of objects.

### Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/image.jpg"
                    }
                }
            ]
        }
    ]
)
```

### Image Content Field Description

When using vision models, `message.content` is a list where each element has:

| Field | Type | Description |
|-------|------|-------------|
| type | string | Content type: "text" or "image_url" |
| text | string | Text content (when type is "text") |
| image_url | object | Image URL object (when type is "image_url") |

The `image_url` object contains:

| Field | Type | Description |
|-------|------|-------------|
| url | string | URL of the image (supports data URLs with base64 encoding) |

## List Models

### Request Endpoint

```
GET https://api.moonshot.cn/v1/models
```

### Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

models = client.models.list()
for model in models.data:
    print(model.id)
```

## Error Handling

The API uses standard HTTP status codes:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Invalid or missing API key
- `403 Forbidden`: API key doesn't have permission
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

Error response format:

```json
{
  "error": {
    "message": "Error description",
    "type": "invalid_request_error",
    "code": "invalid_api_key"
  }
}
```

## Additional Features

### Tool Use (Function Calling)

Moonshot API supports tool/function calling capabilities. See the official documentation for details.

### Partial Mode

Supports partial response mode for faster initial responses.

### File Interface

Supports file upload and processing for document Q&A.

### Token Calculation

Use the token calculation endpoint to estimate token usage before making requests.

### Balance Query

Query your account balance and usage statistics.

## Migration from OpenAI

Since Moonshot API is compatible with OpenAI SDK, you can easily migrate:

1. Change the `base_url` to `https://api.moonshot.cn/v1`
2. Replace your OpenAI API key with your Moonshot API key
3. Update model names to Moonshot models (e.g., `moonshot-v1-8k`)

Most OpenAI SDK code should work without modification.

## Best Practices

1. **Token Management**: Monitor token usage, especially in multi-turn conversations
2. **Error Handling**: Implement proper error handling and retry logic
3. **Rate Limiting**: Be aware of rate limits and implement appropriate backoff strategies
4. **Streaming**: Use streaming for better user experience in interactive applications
5. **Context Window**: Choose the appropriate model based on your context length requirements

## Resources

- **Official Documentation**: https://platform.moonshot.cn/docs/api/chat
- **Platform**: https://platform.moonshot.cn
- **OpenAI SDK (Python)**: https://github.com/openai/openai-python
- **OpenAI SDK (Node.js)**: https://github.com/openai/openai-node

## Notes

- This documentation is based on the Moonshot AI platform documentation
- API specifications may change, refer to the official documentation for the latest information
- Always keep your API keys secure and never commit them to version control


