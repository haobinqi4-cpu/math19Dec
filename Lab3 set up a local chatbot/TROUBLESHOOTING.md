# Troubleshooting Guide - Local Chatbot

## Common Issues and Solutions

### Issue 1: "Invalid API key" Error

**Symptoms**: 
- Chat messages fail with "Invalid API key" or "API authentication failed"
- Model listing works (returns 200) but chat completions fail (401)

**Diagnosis**:
```bash
python3 test_api.py
```

**Likely Cause**: 
Your API key can authenticate but may lack permissions for chat completions, or there may be endpoint-specific restrictions.

**Solutions**:

1. **Verify API Key Permissions**
   - Run `python3 test_api.py` to check which endpoints work
   - If model listing works but chat fails, this is a permissions issue

2. **Check API Key Status**
   - Ensure your API key hasn't expired
   - Verify the key is active in HKBU Gen AI Platform

3. **Contact HKBU IT Support**
   - Email: hotline@hkbu.edu.hk
   - Request verification of API key permissions for chat completions
   - Ask if your account needs additional permissions

4. **Try Different Models**
   - Some models may have different permission requirements
   - Test with `gpt-5-mini` or `gemini-2.5-flash` (smaller models)

### Issue 2: Server Won't Start

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install -r requirements.txt
```

Or use the setup script:
```bash
./setup.sh
```

### Issue 3: Port Already in Use

**Error**: `Address already in use` or `Port 5000 is in use`

**Solution**:
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or change port in scripts/server.py:
# app.run(debug=True, host='0.0.0.0', port=8080)
```

### Issue 4: Connection Refused

**Error**: Cannot connect to `http://localhost:5000`

**Solutions**:
1. Check if server is running: `ps aux | grep server.py`
2. Check server logs for errors
3. Verify firewall isn't blocking port 5000
4. Try accessing via `http://127.0.0.1:5000`

### Issue 5: CORS Errors in Browser Console

**Error**: `CORS policy: No 'Access-Control-Allow-Origin' header`

**Solution**: 
This should already be handled by Flask-CORS. If you see this error:
1. Restart the server
2. Clear browser cache
3. Check that Flask-CORS is installed: `pip install flask-cors`

### Issue 6: Chat History Not Saving

**Symptoms**: Saved chats don't appear in history list

**Solutions**:
1. Check `chatHistory/` directory exists and is writable
2. Check browser console for JavaScript errors
3. Verify file permissions: `chmod 755 chatHistory/`

### Issue 7: Models Not Loading

**Error**: Model dropdown is empty or models fail to load

**Solutions**:
1. Check `/api/models` endpoint: `curl http://localhost:5000/api/models`
2. Verify server is running
3. Check browser network tab for failed requests

### Issue 8: Slow Responses

**Symptoms**: Chat responses take very long or timeout

**Solutions**:
1. Try a faster model (e.g., `gpt-5-mini` instead of `gpt-5`)
2. Reduce `max_tokens` in the request
3. Check your internet connection
4. Test API directly: `python3 test_api.py`

## Diagnostic Commands

### Test API Connection
```bash
python3 test_api.py
```

### Test Server Setup
```bash
python3 test_setup.py
```

### Check Server Logs
```bash
# If running in foreground, logs appear in console
# If running in background, check the log file or restart in foreground
python3 scripts/server.py
```

### Test API Endpoints Directly
```bash
# Test models endpoint
curl http://localhost:5000/api/models

# Test chat endpoint (will fail if API key has permission issues)
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5","messages":[{"role":"user","content":"Hello"}],"max_tokens":50}'
```

## Getting Help

### Check Documentation
1. [README.md](README.md) - Full documentation
2. [QUICKSTART.md](QUICKSTART.md) - Quick start guide
3. [../Data/howtoaccess.md](../Data/howtoaccess.md) - API documentation

### Run Diagnostics
```bash
# Full system check
python3 test_setup.py

# API connection test
python3 test_api.py
```

### Contact Support
- **HKBU IT Support**: hotline@hkbu.edu.hk
- **Platform**: https://genai.hkbu.edu.hk/
- **API Documentation**: See `../Data/howtoaccess.md`

## Known Limitations

1. **API Key Permissions**: Some API keys may only have read access (model listing) but not write access (chat completions). This requires contacting HKBU IT.

2. **Model Availability**: Not all models may be available for all users. Check available models via `/api/models` endpoint.

3. **Rate Limits**: The API may have rate limits. If you hit rate limits, wait a few minutes before retrying.

4. **Timeout Issues**: Some models (especially larger ones) may take longer to respond. Increase timeout if needed.

