# 🧵 QA Test Case Assistant

Una aplicación web inteligente desarrollada con Streamlit que utiliza IA (OpenAI GPT) para generar automáticamente artefactos de testing a partir de documentos de requerimientos en formato PDF.

## 🚀 Características

- 📄 **Carga de documentos PDF**: Sube documentos de requerimientos en formato PDF
- 🤖 **Generación automática con IA**: Utiliza OpenAI GPT-3.5-turbo para generar contenido de calidad
- 📋 **Múltiples tipos de artefactos**:
  - **User Stories**: Historias de usuario en formato estándar
  - **Test Scenarios**: Escenarios de prueba detallados
  - **Test Cases**: Casos de prueba completos con pasos y resultados esperados
- 💾 **Exportación a CSV**: Descarga los resultados generados en formato CSV
- 🎨 **Interfaz intuitiva**: UI moderna y fácil de usar con Streamlit

## 📁 Estructura del Proyecto

```
qa_assistant_app/
├── app.py                 # Aplicación principal de Streamlit
├── generator.py           # Generador de artefactos usando OpenAI
├── pdf_reader.py          # Extractor de texto de archivos PDF
├── prompts.py            # Prompts optimizados para cada tipo de testing
├── utils.py              # Utilidades para manejo de archivos CSV
├── requirements.txt      # Dependencias del proyecto
├── outputs/              # Directorio para archivos CSV generados
└── README.md            # Este archivo
```

## 🛠️ Instalación

### Prerrequisitos

- Python 3.8 o superior
- Clave API de OpenAI

### Pasos de instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd qa_assistant_app
   ```

2. **Crea un entorno virtual (recomendado):**

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

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu clave API de OpenAI:**

   **En macOS/Linux:**
   ```bash
   export OPENAI_API_KEY="tu_clave_api_aquí"
   ```

   **En Windows (PowerShell):**
   ```powershell
   $env:OPENAI_API_KEY="tu_clave_api_aquí"
   ```

   **En Windows (Command Prompt):**
   ```cmd
   set OPENAI_API_KEY=tu_clave_api_aquí
   ```
   
   O crea un archivo `.env` en el directorio raíz:
   ```
   OPENAI_API_KEY=tu_clave_api_aquí
   ```

## 🚀 Uso

1. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```

2. **Abre tu navegador** en `http://localhost:8501`

3. **Sube un documento PDF** con los requerimientos

4. **Selecciona el tipo de artefacto** que deseas generar:
   - User Stories
   - Test Scenarios  
   - Test Cases

5. **Haz clic en "Generate"** y espera a que la IA procese el documento

6. **Descarga los resultados** en formato CSV

## 📋 Tipos de Artefactos Generados

### User Stories
Genera historias de usuario siguiendo el formato estándar:
```
As a <role>, I want to <goal> so that <benefit>
```

### Test Scenarios
Crea múltiples escenarios de prueba detallados para cada requerimiento, incluyendo casos positivos, negativos y edge cases.

### Test Cases
Genera casos de prueba completos con:
- ID único
- Título descriptivo
- Pasos detallados
- Resultados esperados

## 🛡️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para aplicaciones web en Python
- **[OpenAI](https://openai.com/)**: API de inteligencia artificial para generación de contenido
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: Extracción de texto de documentos PDF
- **[Pandas](https://pandas.pydata.org/)**: Manipulación y análisis de datos
- **[LangChain](https://langchain.com/)**: Framework para aplicaciones con LLM

## 📝 Ejemplo de Uso

1. Sube un PDF con requerimientos como:
   ```
   El sistema debe permitir a los usuarios registrarse con email y contraseña.
   Los usuarios deben poder recuperar su contraseña mediante email.
   ```

2. Selecciona "User Stories" y obtendrás:
   ```
   1. As a new user, I want to register with my email and password so that I can access the system.
   2. As a registered user, I want to recover my password via email so that I can regain access to my account.
   ```

## 🤝 Contribuciones

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
| `OPENAI_API_KEY` | Tu clave API de OpenAI | Sí |

### Personalización de Prompts

Puedes modificar los prompts en `prompts.py` para adaptar la generación a tus necesidades específicas.

## 🐛 Reportar Problemas

Si encuentras algún problema, por favor abre un issue en GitHub con:
- Descripción del problema
- Pasos para reproducirlo
- Capturas de pantalla (si aplica)
- Versión de Python y dependencias

## 👨‍💻 Autor

Desarrollado con ❤️ para facilitar el trabajo de los equipos de QA.

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

---

# 🧵 QA Test Case Assistant (English Version)

An intelligent web application built with Streamlit that uses AI (OpenAI GPT) to automatically generate testing artifacts from PDF requirement documents.

## 🚀 Features

- 📄 **PDF Document Upload**: Upload requirement documents in PDF format
- 🤖 **AI-Powered Generation**: Uses OpenAI GPT-3.5-turbo to generate quality content
- 📋 **Multiple Artifact Types**:
  - **User Stories**: User stories in standard format
  - **Test Scenarios**: Detailed test scenarios
  - **Test Cases**: Complete test cases with steps and expected results
- 💾 **CSV Export**: Download generated results in CSV format
- 🎨 **Intuitive Interface**: Modern and easy-to-use UI with Streamlit

## 📁 Project Structure

```
qa_assistant_app/
├── app.py                 # Main Streamlit application
├── generator.py           # Artifact generator using OpenAI
├── pdf_reader.py          # PDF text extractor
├── prompts.py            # Optimized prompts for each testing type
├── utils.py              # CSV file handling utilities
├── requirements.txt      # Project dependencies
├── outputs/              # Directory for generated CSV files
└── README.md            # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd qa_assistant_app
   ```

2. **Create a virtual environment (recommended):**

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

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your OpenAI API key:**

   **On macOS/Linux:**
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

   **On Windows (PowerShell):**
   ```powershell
   $env:OPENAI_API_KEY="your_api_key_here"
   ```

   **On Windows (Command Prompt):**
   ```cmd
   set OPENAI_API_KEY=your_api_key_here
   ```
   
   Or create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 🚀 Usage

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** at `http://localhost:8501`

3. **Upload a PDF document** with requirements

4. **Select the artifact type** you want to generate:
   - User Stories
   - Test Scenarios  
   - Test Cases

5. **Click "Generate"** and wait for the AI to process the document

6. **Download the results** in CSV format

## 📋 Generated Artifact Types

### User Stories
Generates user stories following the standard format:
```
As a <role>, I want to <goal> so that <benefit>
```

### Test Scenarios
Creates multiple detailed test scenarios for each requirement, including positive, negative, and edge cases.

### Test Cases
Generates complete test cases with:
- Unique ID
- Descriptive title
- Detailed steps
- Expected results

## 🛡️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Python web application framework
- **[OpenAI](https://openai.com/)**: AI API for content generation
- **[PyMuPDF](https://pymupdf.readthedocs.io/)**: PDF text extraction
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[LangChain](https://langchain.com/)**: Framework for LLM applications

## 📝 Usage Example

1. Upload a PDF with requirements like:
   ```
   The system must allow users to register with email and password.
   Users must be able to recover their password via email.
   ```

2. Select "User Stories" and you'll get:
   ```
   1. As a new user, I want to register with my email and password so that I can access the system.
   2. As a registered user, I want to recover my password via email so that I can regain access to my account.
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
