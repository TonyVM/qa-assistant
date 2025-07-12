# QA Assistant - Release Notes

## Version 1.0.0 (Master Branch)
**Release Date**: July 11, 2025

### Features
- ✅ PDF upload and text extraction
- ✅ User Stories generation
- ✅ Test Scenarios generation  
- ✅ Test Cases generation
- ✅ Basic OpenAI integration
- ✅ CSV export functionality
- ✅ Simple Streamlit interface

### Technical Details
- **AI Provider**: OpenAI only
- **Model**: GPT-3.5-turbo (hardcoded)
- **Dependencies**: Basic requirements
- **Interface**: Simple radio button selection

---

## Version 1.1.0 (Feature Branch: langchain-multi-model)
**Release Date**: July 11, 2025

### New Features
- ✅ **Multi-model support**: OpenAI + Google Gemini
- ✅ **LangChain integration** for better AI handling
- ✅ **Dynamic model selection** in UI
- ✅ **API key management** with validation
- ✅ **Context size optimization** with smart truncation
- ✅ **Response cleaning** to remove intro text
- ✅ **Step-by-step API tutorials** for both providers

### Improvements
- 🔄 **Better prompts** for cleaner output
- 🔄 **Enhanced error handling**
- 🔄 **Sidebar configuration** for better UX
- 🔄 **Real-time API key validation**
- 🔄 **Model-specific context limits**

### Technical Enhancements
- **AI Providers**: OpenAI + Google Gemini
- **Framework**: LangChain for unified AI access
- **Models**: GPT-3.5/4, Gemini-1.5-flash/pro
- **Smart Features**: Context truncation, response post-processing
- **UI**: Enhanced sidebar with tutorials and validation

---

## Migration Guide

### From v1.0.0 to v1.1.0
1. Update dependencies: `pip install -r requirements.txt`
2. Obtain API keys from OpenAI and/or Google AI Studio
3. Use the new sidebar to configure your preferred AI provider
4. Enjoy enhanced features and better model selection!

### Backward Compatibility
- All v1.0.0 functionality is preserved
- Default behavior remains the same
- New features are opt-in via UI configuration
