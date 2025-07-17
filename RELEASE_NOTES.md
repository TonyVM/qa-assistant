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

## Versión 1.0.0 (Rama Master)
**Fecha de Lanzamiento**: 11 de julio, 2025

### Características
- ✅ Carga de PDF y extracción de texto
- ✅ Generación de User Stories
- ✅ Generación de Test Scenarios  
- ✅ Generación de Test Cases
- ✅ Integración básica con OpenAI
- ✅ Funcionalidad de exportación CSV
- ✅ Interfaz simple de Streamlit

### Detalles Técnicos
- **Proveedor de IA**: Solo OpenAI
- **Modelo**: GPT-3.5-turbo (fijo)
- **Dependencias**: Requerimientos básicos
- **Interfaz**: Selección simple con radio buttons

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
## Version 1.2.0-beta (Feature Branch: gherkin-user-stories)
**Release Date**: July 13, 2025 (In Development)

### 🆕 New Features
- ✅ **Gherkin User Stories**: BDD-style story generation
- ✅ **Complete Gherkin Syntax**: Feature, Scenario, Given, When, Then, And, But
- ✅ **Specialized CSV Export**: Structured format for Gherkin features
- ✅ **BDD Documentation**: Complete guides and examples
- ✅ **Framework Integration**: Ready for Cucumber, Behave, SpecFlow

### 🔧 Technical Improvements
- ✅ **Advanced Parser**: Intelligent feature and scenario analysis
- ✅ **Optimized Prompts**: Gherkin-specific generation
- ✅ **Validation Scripts**: Gherkin format testing
- ✅ **Living Documentation**: Executable scenarios

### Use Cases
- **BDD Teams**: Behavior-driven development workflows
- **Test Automation**: Framework-ready scenarios
- **Documentation**: Living, executable specifications
- **Collaboration**: Business-technical team alignment

---

## Versión 1.2.0-beta (Rama Feature: gherkin-user-stories)
**Fecha de Lanzamiento**: 13 de julio, 2025 (En Desarrollo)

### 🆕 Nuevas Características
- ✅ **Gherkin User Stories**: Generación de historias estilo BDD
- ✅ **Sintaxis Gherkin Completa**: Feature, Scenario, Given, When, Then, And, But
- ✅ **Exportación CSV Especializada**: Formato estructurado para features de Gherkin
- ✅ **Documentación BDD**: Guías completas y ejemplos
- ✅ **Integración con Frameworks**: Listo para Cucumber, Behave, SpecFlow

### 🔧 Mejoras Técnicas
- ✅ **Parser Avanzado**: Análisis inteligente de features y scenarios
- ✅ **Prompts Optimizados**: Generación específica para Gherkin
- ✅ **Scripts de Validación**: Testing de formato Gherkin
- ✅ **Documentación Viva**: Scenarios ejecutables

### Casos de Uso
- **Equipos BDD**: Flujos de desarrollo guiado por comportamiento
- **Automatización de Pruebas**: Scenarios listos para frameworks
- **Documentación**: Especificaciones vivas y ejecutables
- **Colaboración**: Alineación entre equipos de negocio y técnicos

## Versión 1.1.0 (Rama Feature: langchain-multi-model)
**Fecha de Lanzamiento**: 11 de julio, 2025

### Nuevas Características
- ✅ **Soporte multi-modelo**: OpenAI + Google Gemini
- ✅ **Integración LangChain** para mejor manejo de IA
- ✅ **Selección dinámica de modelo** en la UI
- ✅ **Gestión de API keys** con validación
- ✅ **Optimización de tamaño de contexto** con truncado inteligente
- ✅ **Limpieza de respuestas** para eliminar texto introductorio
- ✅ **Tutoriales paso a paso** para ambos proveedores

### Mejoras
- 🔄 **Mejores prompts** para salida más limpia
- 🔄 **Manejo de errores mejorado**
- 🔄 **Configuración en sidebar** para mejor UX
- 🔄 **Validación de API key en tiempo real**
- 🔄 **Límites de contexto específicos por modelo**

### Mejoras Técnicas
- **Proveedores de IA**: OpenAI + Google Gemini
- **Framework**: LangChain para acceso unificado a IA
- **Modelos**: GPT-3.5/4, Gemini-1.5-flash/pro
- **Características inteligentes**: Truncado de contexto, post-procesamiento de respuestas
- **UI**: Sidebar mejorado con tutoriales y validación

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
