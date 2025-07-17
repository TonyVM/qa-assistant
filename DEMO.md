# 🎯 QA Assistant - Demo Guide

## 🚀 Quick Start Demo

This guide will help you test the QA Assistant application step by step.

### 📋 Before You Start

You'll need an API key from at least one of these providers:
- **OpenAI** (recommended for beginners)
- **Google Gemini**

### 🔑 Getting Your API Key

#### Option 1: OpenAI (Recommended)
1. 🌐 Go to: https://platform.openai.com/
2. ⚙️ Click the settings icon (top right corner)
3. 🔑 Select "API keys" from the sidebar menu
4. ➕ Press "Create new secret key"
5. 📋 Copy your key (starts with `sk-`)

#### Option 2: Google Gemini
1. 🌐 Go to: https://aistudio.google.com/app/apikey
2. ➕ Click "Create API key"
3. 📋 Copy your key (starts with `AIza`)

### 🏃‍♂️ Testing Steps

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Configure your API Key:**
   - Select your provider (OpenAI or Gemini)
   - Paste your API key in the corresponding field
   - Verify that ✅ "API key format looks correct" appears

3. **Select a model:**
   - For testing: `gpt-3.5-turbo` or `gemini-pro`
   - For large documents: `gpt-4-turbo-preview`

4. **Upload a test PDF** or use this sample text:
   ```
   The system must allow users to register with email and password.
   Users must be able to recover their password via email.
   The system must validate password strength.
   Users must be able to update their personal profile.
   ```

5. **Select what to generate:**
   - 📝 **User Stories**: For user stories
   - 🥒 **Gherkin User Stories**: For BDD format stories 🆕
   - 🧪 **Test Scenarios**: For test scenarios
   - 📋 **Test Cases**: For detailed test cases

6. **Click "🚀 Generate"** and wait for results

---

# 🎯 QA Assistant - Guía de Demo

## 🚀 Demo de Inicio Rápido

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
   - 🥒 **Gherkin User Stories**: Para historias en formato BDD 🆕
   - 🧪 **Test Scenarios**: Para escenarios de prueba
   - 📋 **Test Cases**: Para casos de prueba detallados

### ✨ What to Expect

**User Stories:**
```
1. As a new user, I want to register with my email and password so that I can access the system.
2. As a registered user, I want to recover my password via email so that I can regain access.
3. As a user, I want the system to validate my password strength so that my account is secure.
```

**Gherkin User Stories:**
```gherkin
Feature: User Registration
  As a new user
  I want to register with my email and password
  So that I can access the system

  Scenario: Successful registration with valid data
    Given I am on the registration page
    When I enter a valid email and strong password
    And I click the register button
    Then I should see a confirmation message
    And I should receive a verification email
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

---

### ✨ Qué Esperar

**User Stories:**
```
1. As a new user, I want to register with my email and password so that I can access the system.
2. As a registered user, I want to recover my password via email so that I can regain access.
3. As a user, I want the system to validate my password strength so that my account is secure.
```

**Gherkin User Stories:**
```gherkin
Feature: Registro de Usuario
  Como nuevo usuario
  Quiero registrarme con mi email y contraseña
  Para poder acceder al sistema

  Scenario: Registro exitoso con datos válidos
    Given estoy en la página de registro
    When ingreso un email válido y contraseña fuerte
    And hago clic en el botón de registro
    Then debería ver un mensaje de confirmación
    And debería recibir un email de verificación
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

**If you get errors:**

1. **"API key format may be incorrect"**
   - Verify your OpenAI key starts with `sk-`
   - Verify your Gemini key starts with `AIza`

2. **"Error generating artifacts"**
   - Check your internet connection
   - Verify your API key is valid and has credits

3. **"Please enter your API key"**
   - Make sure to paste the API key in the corresponding field

4. **"Document too large"**
   - Try with a smaller PDF
   - Use GPT-4-turbo-preview for large documents

---

### 🔍 Solución de Problemas

**Si obtienes errores:**

1. **"API key format may be incorrect"**
   - Verifica que tu clave OpenAI empiece con `sk-`
   - Verifica que tu clave Gemini empiece con `AIza`

2. **"Error al generar artefactos"**
   - Revisa tu conexión a internet
   - Verifica que tu API key sea válida y tenga créditos

3. **"Please enter your API key"**
   - Asegúrate de pegar la API key en el campo correspondiente

4. **"Documento muy grande"**
   - Prueba con un PDF más pequeño
   - Usa GPT-4-turbo-preview para documentos grandes

### 💡 Consejos

- **Documentos pequeños** (< 12K chars): Cualquier modelo funciona bien
- **Documentos grandes** (> 24K chars): Usa GPT-4-turbo-preview
- **Costo vs Calidad**: GPT-3.5-turbo es más económico, GPT-4 más preciso
- **Seguridad**: Tus API keys solo se usan durante la sesión

### 🎉 ¡Listo!

Ahora puedes generar artefactos de testing profesionales usando IA. 
¡Prueba con tus propios documentos de requisitos!
