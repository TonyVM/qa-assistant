# QA Assistant - Changelog

## 🥒 Version 1.2.0 - Gherkin User Stories (In Development)
**Date**: July 13, 2025

### ✨ New Features

**🆕 Gherkin User Stories Support**
- **BDD Format**: Generation of user stories in Gherkin format
- **Complete Syntax**: Support for Feature, Scenario, Given, When, Then, And, But
- **BDD Use Cases**: Perfect for teams using Cucumber, Behave, SpecFlow
- **Enhanced Export**: Specialized CSV for features and scenarios
- **Documentation**: Complete guide on Gherkin and BDD

**🔧 Technical Improvements**
- **Advanced Parser**: Intelligent analysis of features and scenarios for CSV
- **Optimized Prompts**: Specific generation for Gherkin format
- **Validation**: Test scripts to validate Gherkin format
- **Living Documentation**: Scenarios serve as executable documentation

---

## 🥒 Versión 1.2.0 - Gherkin User Stories (En desarrollo)
**Fecha**: 13 de julio, 2025

### ✨ Nuevas Características

**🆕 Soporte para Gherkin User Stories**
- **Formato BDD**: Generación de historias de usuario en formato Gherkin
- **Sintaxis completa**: Soporte para Feature, Scenario, Given, When, Then, And, But
- **Casos de uso BDD**: Perfecto para equipos que usan Cucumber, Behave, SpecFlow
- **Exportación mejorada**: CSV especializado para features y scenarios
- **Documentación**: Guía completa sobre Gherkin y BDD

**🔧 Mejoras Técnicas**
- **Parser avanzado**: Análisis inteligente de features y scenarios para CSV
- **Prompts optimizados**: Generación específica para formato Gherkin
- **Validación**: Scripts de prueba para validar formato Gherkin
- **Documentación viva**: Los scenarios sirven como documentación ejecutable

## 🚀 Version 1.1.0 - LangChain Multi-Model Integration
**Date**: July 11, 2025

### ✨ New Features

1. **🔑 Integrated API Keys in Interface**
   - **Direct Input**: Users can enter their API keys in the application
   - **Included Tutorials**: Step-by-step guides to get API keys
   - **Real-time Validation**: Key format verification
   - **Security**: Keys are only used during the session
   - **Flexibility**: Support for environment variables or manual input

2. **📚 Interactive Tutorials**
   - **OpenAI**: Complete guide from platform.openai.com to creating the key
   - **Google Gemini**: Instructions for aistudio.google.com
   - **Visual Captures**: Direct links to correct pages
   - **Visual Validation**: Immediate feedback on key format

3. **Multiple AI Providers**
   - Support for OpenAI (GPT-3.5, GPT-4, GPT-4-turbo)
   - Support for Google Gemini (Gemini-pro, Gemini-2.5-flash)
   - Dynamic selection of provider and model

4. **Enhanced Architecture with LangChain**
   - Robust and scalable implementation
   - Better error handling
   - Modular architecture for easy extension

---

## 🚀 Versión 1.1.0 - LangChain Multi-Model Integration
**Fecha**: 11 de julio, 2025

### ✨ Nuevas Características

1. **🔑 API Keys Integradas en la Interfaz**
   - **Entrada directa**: Los usuarios pueden ingresar sus API keys en la aplicación
   - **Tutoriales incluidos**: Guías paso a paso para obtener API keys
   - **Validación en tiempo real**: Verificación del formato de las claves
   - **Seguridad**: Las claves solo se usan durante la sesión
   - **Flexibilidad**: Soporte para variables de entorno o entrada manual

2. **📚 Tutoriales Interactivos**
   - **OpenAI**: Guía completa desde platform.openai.com hasta crear la clave
   - **Google Gemini**: Instrucciones para aistudio.google.com
   - **Capturas visuales**: Enlaces directos a las páginas correctas
   - **Validación visual**: Feedback inmediato sobre el formato de las claves

3. **Múltiples Proveedores de IA**
   - Soporte para OpenAI (GPT-3.5, GPT-4, GPT-4-turbo)
   - Soporte para Google Gemini (Gemini-pro, Gemini-2.5-flash)
   - Selección dinámica de proveedor y modelo

4. **Arquitectura Mejorada con LangChain**
   - Implementación robusta y escalable
   - Mejor manejo de errores
   - Arquitectura modular para fácil extensión

5. **Respuestas Limpias y Profesionales**
   - **Post-procesamiento automático** que elimina texto introductorio
   - **Prompts optimizados** para respuestas directas
   - **Filtrado inteligente** que preserva solo el contenido útil
   - Elimina frases como "Here are the user stories..." automáticamente

6. **Manejo Inteligente de Documentos Grandes**
   - **Límites dinámicos** según el modelo (12K a 100K caracteres)
   - **Truncado inteligente** que preserva párrafos completos
   - **Feedback visual** sobre el procesamiento del documento

7. **Interfaz de Usuario Mejorada**
   - Sidebar con configuración de modelos y API keys
   - Información detallada del documento
   - Sección de ayuda integrada
   - Mejor feedback visual y manejo de errores

### 🔧 Mejoras Técnicas

1. **Generador de IA Refactorizado**
   - Clase `AIModelGenerator` para mejor organización
   - Soporte para múltiples proveedores
   - Mejor manejo de límites de contexto (4000 caracteres)

2. **Manejo de Errores**
   - Validación de API keys
   - Mensajes de error específicos
   - Graceful fallbacks

3. **Documentación Actualizada**
   - README con instrucciones para múltiples modelos
   - Documentación de APIs keys
   - Guías de configuración por sistema operativo

### 📦 Dependencias Actualizadas

```
streamlit
openai
langchain
langchain-openai      # Nuevo
langchain-google-genai # Nuevo
PyMuPDF
pandas
python-dotenv         # Nuevo
```

## 🔄 Comparación de Versiones

### Versión Anterior (main/master)
- Solo OpenAI GPT-3.5-turbo
- Implementación directa con openai
- Configuración básica

### Nueva Versión (feature/langchain-multi-model)
- Múltiples proveedores (OpenAI + Gemini)
- Arquitectura LangChain
- UI mejorada con configuración
- Mejor manejo de errores
- Documentación completa

## 🚀 Próximos Pasos

1. **Testing**: Verificar funcionamiento con ambos proveedores
2. **Optimización**: Ajustar prompts para cada modelo
3. **Features**: Considerar streaming, cache, etc.
4. **Deploy**: Preparar para deployment en cloud

## 📝 Notas de Migración

Para usar la nueva versión:
1. Instalar nuevas dependencias: `pip install -r requirements.txt`
2. Configurar API keys según el proveedor elegido
3. La interfaz es compatible, solo con mejoras UI
4. Los archivos CSV mantienen el mismo formato
