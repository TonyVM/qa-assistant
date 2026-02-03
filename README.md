# 🧵 QA Assistant

An intelligent web application built with Streamlit that uses **LangChain** and AI (OpenAI GPT and Google Gemini) to automatically generate testing artifacts from PDF requirement documents.

## 🌐 Live Demo

**🚀 Try it now:** [https://smart-tester.streamlit.app/](https://smart-tester.streamlit.app/)

## 🚀 Features

- 📄 **PDF Document Upload**: Upload requirement documents in PDF format
- 🤖 **Multiple AI Providers**: Support for OpenAI GPT and Google Gemini
- 🔑 **Integrated API Keys**: Enter your API keys directly in the interface
- 📚 **Built-in Tutorials**: Step-by-step guides to get API keys
- ⚙️ **Model Selection**: Choose between different models based on your needs
- 🔗 **Powered by LangChain**: Robust and scalable architecture
- 🧹 **Clean Responses**: Automatic post-processing that removes unnecessary introductory text
- 📏 **Intelligent Document Handling**: Smart truncation that preserves complete paragraphs
- 📋 **Multiple Artifact Types**:
  - **User Stories**: User stories in standard format
  - **Gherkin User Stories**: BDD-style user stories with Given/When/Then 🆕
  - **Test Scenarios**: Detailed test scenarios
  - **Test Cases**: Complete test cases with steps and expected results
- 💾 **CSV Export**: Download generated results in CSV format
- 🎨 **Intuitive Interface**: Modern and easy-to-use UI with Streamlit
- 🔒 **Security**: API keys are only used during the session

---

# 🧵 QA Assistant (Español)

Una aplicación web inteligente desarrollada con Streamlit que utiliza **LangChain** e IA (OpenAI GPT y Google Gemini) para generar automáticamente artefactos de testing a partir de documentos de requerimientos en formato PDF.

## 🌐 Demo en Vivo

**🚀 Pruébalo ahora:** [https://smart-tester.streamlit.app/](https://smart-tester.streamlit.app/)

## 🚀 Características

- 📄 **Carga de documentos PDF**: Sube documentos de requerimientos en formato PDF
- 🤖 **Múltiples proveedores de IA**: Soporte para OpenAI GPT y Google Gemini
- 🔑 **API Keys integradas**: Ingresa tus claves API directamente en la interfaz
- 📚 **Tutoriales incluidos**: Guías paso a paso para obtener API keys
- ⚙️ **Selección de modelos**: Elige entre diferentes modelos según tus necesidades
- 🔗 **Powered by LangChain**: Arquitectura robusta y escalable
- 🧹 **Respuestas limpias**: Post-procesamiento automático que elimina texto introductorio innecesario
- 📏 **Manejo inteligente de documentos**: Truncado que preserva párrafos completos
- 📋 **Múltiples tipos de artefactos**:
  - **User Stories**: Historias de usuario en formato estándar
  - **Gherkin User Stories**: Historias de usuario en formato BDD con Given/When/Then 🆕
  - **Test Scenarios**: Escenarios de prueba detallados
  - **Test Cases**: Casos de prueba completos con pasos y resultados esperados
- 💾 **Exportación a CSV**: Descarga los resultados generados en formato CSV
- 🎨 **Interfaz intuitiva**: UI moderna y fácil de usar con Streamlit
- 🔒 **Seguridad**: Las API keys solo se usan durante la sesión

## 🤖 Supported Models and Limits

### OpenAI
- **GPT-3.5-turbo**: ~12,000 characters (fast and efficient)
- **GPT-4**: ~24,000 characters (higher accuracy)
- **GPT-4-turbo-preview**: ~100,000 characters (large documents)

### Google Gemini
- **Gemini-pro**: ~20,000 characters (Google's main model)
- **Gemini-pro-vision**: ~20,000 characters (with visual capabilities)

### Intelligent Document Handling
- **Smart truncation**: Preserves complete paragraphs
- **Dynamic limits**: Adjusted according to selected model
- **Visual feedback**: Clear information about document processing

---

## 🤖 Modelos Soportados y Límites

### OpenAI
- **GPT-3.5-turbo**: ~12,000 caracteres (rápido y eficiente)
- **GPT-4**: ~24,000 caracteres (mayor precisión)
- **GPT-4-turbo-preview**: ~100,000 caracteres (documentos grandes)

### Google Gemini
- **Gemini-pro**: ~20,000 caracteres (modelo principal de Google)
- **Gemini-pro-vision**: ~20,000 caracteres (con capacidades visuales)

### Manejo Inteligente de Documentos
- **Truncado inteligente**: Preserva párrafos completos
- **Límites dinámicos**: Ajustados según el modelo seleccionado
- **Feedback visual**: Información clara sobre el procesamiento del documento

## 📁 Project Structure

```
qa_assistant_app/
├── app.py                 # Main Streamlit application
├── generator.py           # Artifact generator using AI
├── pdf_reader.py          # PDF text extractor
├── prompts.py            # Optimized prompts for each testing type
├── utils.py              # CSV file handling utilities
├── requirements.txt      # Project dependencies
├── outputs/              # Directory for generated CSV files
└── README.md            # This file
```

---

## 📁 Estructura del Proyecto

```
qa_assistant_app/
├── app.py                 # Aplicación principal de Streamlit
├── generator.py           # Generador de artefactos usando IA
├── pdf_reader.py          # Extractor de texto de archivos PDF
├── prompts.py            # Prompts optimizados para cada tipo de testing
├── utils.py              # Utilidades para manejo de archivos CSV
├── requirements.txt      # Dependencias del proyecto
├── outputs/              # Directorio para archivos CSV generados
└── README.md            # Este archivo
```

## 🛠️ Installation and Local Setup

### Prerequisites

- **Python 3.8 or higher** installed on your system
  - To check your Python version: `python --version` or `python3 --version`
  - Download Python from [python.org](https://www.python.org/downloads/) if needed
- **Git** installed (to clone the repository)
  - Download from [git-scm.com](https://git-scm.com/downloads)
- **An account with at least one of these providers:**
  - [OpenAI Platform](https://platform.openai.com/) (for GPT models)
  - [Google AI Studio](https://aistudio.google.com/) (for Gemini models)

### Step-by-Step Installation

#### 1. Download the Code

Open a terminal/command prompt and run:

```bash
git clone https://github.com/TonyVM/qa-assistant.git
cd qa-assistant
```

Alternatively, download the code as ZIP:
- Click the green "Code" button on [GitHub](https://github.com/TonyVM/qa-assistant)
- Select "Download ZIP"
- Extract the ZIP file
- Navigate to the extracted folder in your terminal

#### 2. Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated.

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

You should see `(.venv)` at the beginning of your terminal prompt.

#### 3. Install Dependencies

With the virtual environment activated, install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit (web interface)
- LangChain (AI framework)
- OpenAI and Google libraries
- PDF processing libraries
- And other dependencies

#### 4. Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

If it doesn't open automatically, manually navigate to: **http://localhost:8501**

#### 5. Configure Your API Key

Once the app is running:
1. Look at the sidebar on the left
2. Select your AI provider (OpenAI or Google Gemini)
3. Click on "📚 How to get [Provider] API Key" for step-by-step instructions
4. Paste your API key in the input field
5. Select the model you want to use

**🎉 You're ready to start generating testing artifacts!**

### Troubleshooting

**Issue: `python` command not found**
- Try using `python3` instead
- Ensure Python is added to your system PATH

**Issue: Permission denied when activating virtual environment on Windows**
- Run PowerShell as Administrator
- Execute: `Set-ExecutionPolicy RemoteSigned`

**Issue: Port 8501 already in use**
- Stop other Streamlit instances
- Or use a different port: `streamlit run app.py --server.port 8502`

**Issue: Missing dependencies**
- Ensure you activated the virtual environment
- Run `pip install -r requirements.txt` again

---

## 🛠️ Instalación y Configuración Local

### Prerrequisitos

- **Python 3.8 o superior** instalado en tu sistema
  - Para verificar tu versión de Python: `python --version` o `python3 --version`
  - Descarga Python desde [python.org](https://www.python.org/downloads/) si es necesario
- **Git** instalado (para clonar el repositorio)
  - Descarga desde [git-scm.com](https://git-scm.com/downloads)
- **Una cuenta en al menos uno de estos proveedores:**
  - [OpenAI Platform](https://platform.openai.com/) (para modelos GPT)
  - [Google AI Studio](https://aistudio.google.com/) (para modelos Gemini)

### Pasos de Instalación Detallados

#### 1. Descargar el Código

Abre una terminal/símbolo del sistema y ejecuta:

```bash
git clone https://github.com/TonyVM/qa-assistant.git
cd qa-assistant
```

Alternativamente, descarga el código como ZIP:
- Haz clic en el botón verde "Code" en [GitHub](https://github.com/TonyVM/qa-assistant)
- Selecciona "Download ZIP"
- Extrae el archivo ZIP
- Navega a la carpeta extraída en tu terminal

#### 2. Crear un Entorno Virtual (Recomendado)

Un entorno virtual mantiene las dependencias de tu proyecto aisladas.

**En macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**En Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Deberías ver `(.venv)` al inicio de tu prompt de terminal.

#### 3. Instalar Dependencias

Con el entorno virtual activado, instala todos los paquetes requeridos:

```bash
pip install -r requirements.txt
```

Esto instalará:
- Streamlit (interfaz web)
- LangChain (framework de IA)
- Bibliotecas de OpenAI y Google
- Bibliotecas de procesamiento de PDF
- Y otras dependencias

#### 4. Ejecutar la Aplicación

Inicia el servidor de Streamlit:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado en `http://localhost:8501`

Si no se abre automáticamente, navega manualmente a: **http://localhost:8501**

#### 5. Configurar tu API Key

Una vez que la aplicación esté ejecutándose:
1. Mira la barra lateral a la izquierda
2. Selecciona tu proveedor de IA (OpenAI o Google Gemini)
3. Haz clic en "📚 How to get [Provider] API Key" para ver las instrucciones paso a paso
4. Pega tu API key en el campo de entrada
5. Selecciona el modelo que deseas usar

**🎉 ¡Estás listo para comenzar a generar artefactos de testing!**

### Solución de Problemas

**Problema: comando `python` no encontrado**
- Intenta usar `python3` en su lugar
- Asegúrate de que Python esté agregado al PATH de tu sistema

**Problema: Permiso denegado al activar el entorno virtual en Windows**
- Ejecuta PowerShell como Administrador
- Ejecuta: `Set-ExecutionPolicy RemoteSigned`

**Problema: Puerto 8501 ya en uso**
- Detén otras instancias de Streamlit
- O usa un puerto diferente: `streamlit run app.py --server.port 8502`

**Problema: Dependencias faltantes**
- Asegúrate de haber activado el entorno virtual
- Ejecuta `pip install -r requirements.txt` nuevamente

## 🚀 Usage

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** at `http://localhost:8501`

3. **Configure your API key** in the sidebar:
   - Select the provider (OpenAI or Gemini)  
   - Click on "📚 How to get [Provider] API Key" to see the tutorial
   - Get your API key following the tutorial steps
   - Paste it in the corresponding field

4. **Select the specific model** according to your document

5. **Upload a PDF document** with the requirements

6. **Select the artifact type** you want to generate:
   - User Stories
   - Gherkin User Stories 🆕
   - Test Scenarios  
   - Test Cases

7. **Click "🚀 Generate"** and wait for the AI to process the document

8. **Review the results** and **download in CSV format** if satisfactory

### 🔑 How to Get API Keys

#### OpenAI API Key:
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Click on the settings icon (⚙️) in the top right corner
3. In the left sidebar menu, click on "API keys"
4. Click the "Create new secret key" button
5. Copy your API key (starts with `sk-`)

#### Google Gemini API Key:
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click the "Create API key" button
3. Select your Google Cloud project or create a new one
4. Copy your API key (starts with `AIza`)

---

## 🚀 Uso

1. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```

2. **Abre tu navegador** en `http://localhost:8501`

3. **Configura tu API key** en la barra lateral:
   - Selecciona el proveedor (OpenAI o Gemini)  
   - Haz clic en "📚 How to get [Provider] API Key" para ver el tutorial
   - Obtén tu API key siguiendo los pasos del tutorial
   - Pégala en el campo correspondiente

4. **Selecciona el modelo** específico según tu documento

5. **Sube un documento PDF** con los requerimientos

6. **Selecciona el tipo de artefacto** que deseas generar:
   - User Stories
   - Gherkin User Stories 🆕
   - Test Scenarios  
   - Test Cases

7. **Haz clic en "🚀 Generate"** y espera a que la IA procese el documento

8. **Revisa los resultados** y **descarga en formato CSV** si están satisfactorios

### 🔑 Cómo Obtener API Keys

#### OpenAI API Key:
1. Ve a [OpenAI Platform](https://platform.openai.com/)
2. Haz clic en el ícono de configuración (⚙️) en la esquina superior derecha
3. En el menú lateral izquierdo, haz clic en "API keys"
4. Presiona el botón "Create new secret key"
5. Copia tu API key (empieza con `sk-`)

#### Google Gemini API Key:
1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Haz clic en el botón "Create API key"
3. Selecciona tu proyecto de Google Cloud o crea uno nuevo
4. Copia tu API key (empieza con `AIza`)

## 📋 Generated Artifact Types

### User Stories
Generates user stories following the standard format:
```
As a <role>, I want to <goal> so that <benefit>
```

### Gherkin User Stories 🆕
Generates user stories in BDD (Behavior Driven Development) format using Gherkin:
```gherkin
Feature: User Authentication
  As a customer
  I want to log into my account
  So that I can access my personal information

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter my valid email and password
    And I click the login button
    Then I should be redirected to my dashboard
    And I should see a welcome message

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter an invalid email or password
    And I click the login button
    Then I should see an error message
    And I should remain on the login page
```

**Benefits of Gherkin format:**
- 📖 Readable for both technical and non-technical teams
- 🔄 Executable with tools like Cucumber, Behave, SpecFlow
- 📚 Living documentation that stays updated
- 🤝 Facilitates collaboration between developers, testers and business analysts
- 🎯 Focus on user behavior (BDD)

### Test Scenarios
Creates multiple detailed test scenarios for each requirement, including positive, negative and edge cases.

### Test Cases
Generates complete test cases with:
- Unique ID
- Descriptive title
- Detailed steps
- Expected results

---

## 📋 Tipos de Artefactos Generados

### User Stories
Genera historias de usuario siguiendo el formato estándar:
```
As a <role>, I want to <goal> so that <benefit>
```

### Gherkin User Stories 🆕
Genera historias de usuario en formato BDD (Behavior Driven Development) usando Gherkin:
```gherkin
Feature: User Authentication
  As a customer
  I want to log into my account
  So that I can access my personal information

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter my valid email and password
    And I click the login button
    Then I should be redirected to my dashboard
    And I should see a welcome message

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter an invalid email or password
    And I click the login button
    Then I should see an error message
    And I should remain on the login page
```

**Beneficios del formato Gherkin:**
- 📖 Legible para equipos técnicos y no técnicos
- 🔄 Ejecutable con herramientas como Cucumber, Behave, SpecFlow
- 📚 Documentación viva que se mantiene actualizada
- 🤝 Facilita la colaboración entre desarrolladores, testers y analistas de negocio
- 🎯 Enfoque en el comportamiento del usuario (BDD)

### Test Scenarios
Crea múltiples escenarios de prueba detallados para cada requerimiento, incluyendo casos positivos, negativos y edge cases.

### Test Cases
Genera casos de prueba completos con:
- ID único
- Título descriptivo
- Pasos detallados
- Resultados esperados

## 🛡️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Python web application framework
- **[LangChain](https://langchain.com/)**: Framework for LLM applications and AI orchestration
- **[OpenAI](https://openai.com/)**: Artificial intelligence API (GPT-3.5, GPT-4)
- **[Google Gemini](https://ai.google.dev/)**: Google's AI models (Gemini Pro)
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: PDF text extraction
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Environment variable management

---

## 🛡️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para aplicaciones web en Python
- **[LangChain](https://langchain.com/)**: Framework para aplicaciones con LLM y orquestación de IA
- **[OpenAI](https://openai.com/)**: API de inteligencia artificial (GPT-3.5, GPT-4)
- **[Google Gemini](https://ai.google.dev/)**: Modelos de IA de Google (Gemini Pro)
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: Extracción de texto de documentos PDF
- **[Pandas](https://pandas.pydata.org/)**: Manipulación y análisis de datos
## 📝 Usage Example

1. Upload a PDF with requirements like:
   ```
   The system must allow users to register with email and password.
   Users must be able to recover their password via email.
   The system must validate password strength.
   Users must be able to update their personal profile.
   The system must send email notifications for important events.
   ```

2. **Select the appropriate model**:
   - For small documents (< 12K characters): GPT-3.5-turbo
   - For medium documents (< 24K characters): GPT-4 or Gemini-pro  
   - For large documents (< 100K characters): GPT-4-turbo-preview

3. Select "User Stories" and you'll get **only** the useful content:
   ```
   1. As a new user, I want to register with my email and password so that I can access the system.
   2. As a registered user, I want to recover my password via email so that I can regain access to my account.
   3. As a user, I want the system to validate my password strength so that my account is secure.
   4. As a registered user, I want to update my personal profile so that my information stays current.
   5. As a user, I want to receive email notifications for important events so that I stay informed.
   ```

   **Note**: The application automatically removes introductory text like "Here are the user stories extracted from..." to deliver only relevant content.

---

## 📝 Ejemplo de Uso

1. Sube un PDF con requerimientos como:
   ```
   El sistema debe permitir a los usuarios registrarse con email y contraseña.
   Los usuarios deben poder recuperar su contraseña mediante email.
   El sistema debe validar la fortaleza de las contraseñas.
   Los usuarios deben poder actualizar su perfil personal.
   El sistema debe enviar notificaciones por email para eventos importantes.
   ```

2. **Selecciona el modelo apropiado**:
   - Para documentos pequeños (< 12K caracteres): GPT-3.5-turbo
   - Para documentos medianos (< 24K caracteres): GPT-4 o Gemini-pro  
   - Para documentos grandes (< 100K caracteres): GPT-4-turbo-preview

3. Selecciona "User Stories" y obtendrás **únicamente** el contenido útil:
   ```
   1. As a new user, I want to register with my email and password so that I can access the system.
   2. As a registered user, I want to recover my password via email so that I can regain access to my account.
   3. As a user, I want the system to validate my password strength so that my account is secure.
   4. As a registered user, I want to update my personal profile so that my information stays current.
   5. As a user, I want to receive email notifications for important events so that I stay informed.
   ```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🔧 Additional Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Only for OpenAI models |
| `GOOGLE_API_KEY` | Your Google API key | Only for Gemini models |

**Note**: You only need to configure the API key for the provider you plan to use.

### Getting API Keys

**OpenAI:**
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Set up billing if necessary

**Google Gemini:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Enable the Gemini API

### Prompt Customization

You can modify the prompts in `prompts.py` to adapt the generation to your specific needs.

### Model Selection

The application allows choosing between different models:
- **For development/testing**: GPT-3.5-turbo or Gemini-pro
- **For production**: GPT-4 (higher accuracy, higher cost)

## 🐛 Bug Reports

If you encounter any issues, please open a GitHub issue with:
- Problem description
- Steps to reproduce
- Screenshots (if applicable)
- Python and dependency versions

## 👨‍💻 Author

Developed with ❤️ to facilitate the work of QA teams.

---

⭐ If you like this project, give it a star on GitHub!

---

# 🧵 QA Assistant (Versión en Español)

Una aplicación web inteligente desarrollada con Streamlit que utiliza IA (OpenAI GPT y Google Gemini) para generar automáticamente artefactos de testing a partir de documentos de requerimientos en formato PDF.

## � Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🔧 Configuración Adicional

### Variables de Entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `OPENAI_API_KEY` | Tu clave API de OpenAI | Solo para modelos OpenAI |
| `GOOGLE_API_KEY` | Tu clave API de Google | Solo para modelos Gemini |

**Nota**: Solo necesitas configurar la API key del proveedor que planeas usar.

### Obtener API Keys

**OpenAI:**
1. Ve a [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Crea una nueva clave API
3. Configura billing si es necesario

**Google Gemini:**
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una nueva API key
3. Habilita la Gemini API

### Personalización de Prompts

Puedes modificar los prompts en `prompts.py` para adaptar la generación a tus necesidades específicas.

### Selección de Modelos

La aplicación permite elegir entre diferentes modelos:
- **Para desarrollo/pruebas**: GPT-3.5-turbo o Gemini-pro
- **Para producción**: GPT-4 (mayor precisión, mayor costo)

## � Reportar Problemas

Si encuentras algún problema, por favor abre un issue en GitHub con:
- Descripción del problema
- Pasos para reproducirlo
- Capturas de pantalla (si aplica)
- Versión de Python y dependencias

## 👨‍💻 Autor

Desarrollado con ❤️ para facilitar el trabajo de los equipos de QA.

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

## 🔧 Additional Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Prompt Customization

You can modify the prompts in `prompts.py` to adapt the generation to your specific needs.

## 🐛 Bug Reports

If you find any issues, please open a GitHub issue with:
- Problem description
- Steps to reproduce
- Screenshots (if applicable)
- Python and dependency versions

## 👨‍💻 Author

Developed with ❤️ to facilitate the work of QA teams.

---

⭐ If you like this project, give it a star on GitHub!
