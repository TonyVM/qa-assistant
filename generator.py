from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from prompts import PROMPTS
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


class AIModelGenerator:
    def __init__(self, model_provider="openai", model_name=None, api_key=None):
        self.model_provider = model_provider.lower()
        self.model_name = model_name
        self.api_key = api_key
        self.llm = self._initialize_model()

    def _initialize_model(self):
        """Inicializa el modelo según el proveedor seleccionado"""
        if self.model_provider == "openai":
            # Priorizar API key pasada como parámetro
            api_key = self.api_key or os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY no encontrada. Por favor ingresa tu API key."
                )

            model = self.model_name or "gpt-3.5-turbo"
            return ChatOpenAI(model=model, temperature=0.3, api_key=api_key)

        elif self.model_provider == "gemini":
            # Priorizar API key pasada como parámetro
            api_key = self.api_key or os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError(
                    "GOOGLE_API_KEY no encontrada. Por favor ingresa tu API key."
                )

            model = self.model_name or "gemini-pro"
            return ChatGoogleGenerativeAI(
                model=model, temperature=0.3, google_api_key=api_key
            )

        else:
            raise ValueError(f"Proveedor no soportado: {self.model_provider}")

    def generate_artifacts(self, text: str, artifact_type: str) -> str:
        """Genera artefactos de testing usando LangChain"""
        try:
            # Obtener el prompt base
            base_prompt = PROMPTS.get(artifact_type, "")
            if not base_prompt:
                raise ValueError(f"Tipo de artefacto no soportado: {artifact_type}")

            # Crear el template del prompt
            prompt_template = ChatPromptTemplate.from_messages(
                [
                    (
                        "human",
                        "{base_prompt}\n\nTexto del requerimiento:\n{requirement_text}",
                    )
                ]
            )

            # Manejo inteligente del tamaño del texto
            # Los modelos modernos pueden manejar más contexto
            max_chars = self._get_max_context_length()

            if len(text) > max_chars:
                # Si el texto es muy largo, usar los primeros párrafos más relevantes
                limited_text = self._smart_truncate(text, max_chars)
            else:
                limited_text = text

            # Crear la cadena de procesamiento
            chain = prompt_template | self.llm

            # Ejecutar la generación
            response = chain.invoke(
                {"base_prompt": base_prompt, "requirement_text": limited_text}
            )

            cleaned_response = self._clean_response(response.content, artifact_type)

            return cleaned_response

        except Exception as e:
            return f"Error al generar artefactos: {str(e)}"

    def _get_max_context_length(self):
        """Retorna el límite máximo de caracteres según el modelo"""
        model_limits = {
            "gpt-3.5-turbo": 12000,  # ~3k tokens
            "gpt-4": 24000,  # ~6k tokens
            "gpt-4-turbo-preview": 100000,  # ~25k tokens
            "gemini-pro": 20000,  # ~5k tokens
            "gemini-pro-vision": 20000,
        }
        return model_limits.get(self.model_name, 12000)

    def _smart_truncate(self, text: str, max_chars: int) -> str:
        """Trunca el texto de manera inteligente preservando párrafos completos"""
        if len(text) <= max_chars:
            return text

        # Dividir por párrafos (doble salto de línea)
        paragraphs = text.split("\n\n")

        result = ""
        for paragraph in paragraphs:
            # Si agregar este párrafo no excede el límite, agregarlo
            if len(result + paragraph + "\n\n") <= max_chars:
                result += paragraph + "\n\n"
            else:
                # Si es el primer párrafo y es muy largo, truncar por oraciones
                if not result:
                    sentences = paragraph.split(". ")
                    for sentence in sentences:
                        if len(result + sentence + ". ") <= max_chars:
                            result += sentence + ". "
                        else:
                            break
                break

        return result.strip()

    def _clean_response(self, response: str, artifact_type: str) -> str:
        """Limpia la respuesta del modelo removiendo texto introductorio"""
        lines = response.strip().split("\n")
        cleaned_lines = []

        if artifact_type == "User Stories":
            # Buscar líneas que empiecen con número seguido de punto
            for line in lines:
                stripped = line.strip()
                if stripped and (
                    stripped[0].isdigit()
                    or stripped.startswith("- ")
                    or stripped.lower().startswith("as ")
                ):
                    cleaned_lines.append(line)

        elif artifact_type == "Test Scenarios":
            # Buscar líneas numeradas o con viñetas
            for line in lines:
                stripped = line.strip()
                if stripped and (
                    stripped[0].isdigit()
                    or stripped.startswith("- ")
                    or stripped.startswith("* ")
                ):
                    cleaned_lines.append(line)

        elif artifact_type == "Test Cases":
            # Buscar líneas que empiecen con ID:, Title:, Steps:, Expected Result:
            in_test_case = False
            for line in lines:
                stripped = line.strip()
                if (
                    stripped.startswith("ID:")
                    or stripped.startswith("Title:")
                    or stripped.startswith("Steps:")
                    or stripped.startswith("Expected Result:")
                    or (stripped and stripped[0].isdigit() and ":" in stripped)
                    or in_test_case
                ):
                    cleaned_lines.append(line)
                    in_test_case = True
                elif stripped == "":
                    # Preservar líneas vacías dentro de test cases
                    if in_test_case:
                        cleaned_lines.append(line)
                else:
                    in_test_case = False

        # Si no se encontraron líneas válidas, devolver respuesta original
        if not cleaned_lines:
            return response

        return "\n".join(cleaned_lines).strip()


def generate_test_artifacts(
    text: str,
    type_: str,
    model_provider: str = "openai",
    model_name: str = None,
    api_key: str = None,
) -> str:
    """
    Función de compatibilidad para mantener la interfaz existente
    """
    generator = AIModelGenerator(model_provider, model_name, api_key)
    return generator.generate_artifacts(text, type_)


def get_available_models():
    """Retorna los modelos disponibles por proveedor"""
    return {
        "openai": ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
        "gemini": ["gemini-pro", "gemini-2.5-flash"],
    }
