# 🎯 QA Assistant - Demo Guide

## 🚀 Quick Start Demo

Esta guía te ayudará a probar la aplicación QA Assistant paso a paso.

### 📋 Antes de Empezar

Necesitarás una API key de al menos uno de estos proveedores:
- **OpenAI** (recomendado para comenzar)
- **Google Gemini**

### 🔑 Obtener tu API Key

#### Opción 1: OpenAI (Recomendado)
1. 🌐 Ve a: https://platform.openai.com/
2. ⚙️ Haz clic en el ícono de configuración (esquina superior derecha)
3. 🔑 Selecciona "API keys" en el menú lateral
4. ➕ Presiona "Create new secret key"
5. 📋 Copia tu clave (empieza con `sk-`)

#### Opción 2: Google Gemini
1. 🌐 Ve a: https://aistudio.google.com/app/apikey
2. ➕ Haz clic en "Create API key"
3. 📋 Copia tu clave (empieza con `AIza`)

### 🏃‍♂️ Pasos para Probar

1. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```

2. **Configura tu API Key:**
   - Selecciona tu proveedor (OpenAI o Gemini)
   - Pega tu API key en el campo correspondiente
   - Verifica que aparezca ✅ "API key format looks correct"

3. **Selecciona un modelo:**
   - Para pruebas: `gpt-3.5-turbo` o `gemini-pro`
   - Para documentos grandes: `gpt-4-turbo-preview`

4. **Sube un PDF de prueba** o usa este texto de ejemplo:
   ```
   El sistema debe permitir a los usuarios registrarse con email y contraseña.
   Los usuarios deben poder recuperar su contraseña mediante email.
   El sistema debe validar la fortaleza de las contraseñas.
   Los usuarios deben poder actualizar su perfil personal.
   ```

5. **Selecciona qué generar:**
   - 📝 **User Stories**: Para historias de usuario
   - 🧪 **Test Scenarios**: Para escenarios de prueba
   - 📋 **Test Cases**: Para casos de prueba detallados

6. **Haz clic en "🚀 Generate"** y espera los resultados

### ✨ Qué Esperar

**User Stories:**
```
1. As a new user, I want to register with my email and password so that I can access the system.
2. As a registered user, I want to recover my password via email so that I can regain access.
3. As a user, I want the system to validate my password strength so that my account is secure.
```

**Test Scenarios:**
```
1. User registration with valid email and strong password
2. User registration with already existing email address
3. Password recovery with valid registered email
4. Login attempt with correct credentials
```

**Test Cases:**
```
ID: TC-001
Title: User Registration with Valid Credentials
Steps:
1. Navigate to registration page
2. Enter valid email address
3. Enter strong password
4. Click register button
Expected Result: User account is created successfully
```

### 🔍 Troubleshooting

**Si obtienes errores:**

1. **"API key format may be incorrect"**
   - Verifica que tu clave OpenAI empiece con `sk-`
   - Verifica que tu clave Gemini empiece con `AIza`

2. **"Error al generar artefactos"**
   - Revisa tu conexión a internet
   - Verifica que tu API key sea válida y tenga créditos

3. **"Please enter your API key"**
   - Asegúrate de pegar la API key en el campo correspondiente

### 💡 Consejos

- **Documentos pequeños** (< 12K chars): Cualquier modelo funciona bien
- **Documentos grandes** (> 24K chars): Usa GPT-4-turbo-preview
- **Costo vs Calidad**: GPT-3.5-turbo es más económico, GPT-4 más preciso
- **Seguridad**: Tus API keys solo se usan durante la sesión

### 🎉 ¡Listo!

Ahora puedes generar artefactos de testing profesionales usando IA. 
¡Prueba con tus propios documentos de requisitos!
