import streamlit as st
from pdf_reader import extract_text_from_pdf
from generator import generate_test_artifacts, get_available_models
from utils import save_to_csv

st.set_page_config(page_title="QA Assistant v1.2.0-beta", layout="centered")
st.title("🧵 QA Test Case Assistant")
st.caption("Version 1.2.0-beta - Multi-Model + Gherkin BDD Support")

# Sidebar para configuraciones del modelo
with st.sidebar:
    st.header("🤖 Model Configuration")

    # Selección del proveedor
    model_provider = st.selectbox(
        "Select AI Provider:",
        ["openai", "gemini"],
        help="Choose between OpenAI or Google Gemini models",
    )

    # Obtener modelos disponibles
    available_models = get_available_models()

    # Selección del modelo específico
    model_name = st.selectbox(
        f"Select {model_provider.upper()} Model:",
        available_models[model_provider],
        help=f"Choose the specific {model_provider} model to use",
    )

    st.markdown("---")

    # Sección de API Keys
    st.subheader("🔑 API Key Configuration")

    # Campo para ingresar API key según el proveedor seleccionado
    if model_provider == "openai":
        api_key = st.text_input(
            "OpenAI API Key:",
            type="password",
            placeholder="sk-...",
            help="Enter your OpenAI API key here",
        )

        # Tutorial para OpenAI
        with st.expander("📚 How to get OpenAI API Key"):
            st.markdown(
                """
            **Step 1:** Go to [OpenAI Platform](https://platform.openai.com/)
            
            **Step 2:** Click on the settings icon (⚙️) in the top right corner
            
            **Step 3:** In the left sidebar menu, click on "API keys"
            
            **Step 4:** Click the "Create new secret key" button
            
            **Step 5:** Copy your API key and paste it in the field above
            
            ⚠️ **Important:** Keep your API key secure and don't share it!
            """
            )

    else:  # gemini
        api_key = st.text_input(
            "Google API Key:",
            type="password",
            placeholder="AIza...",
            help="Enter your Google API key here",
        )

        # Tutorial para Gemini
        with st.expander("📚 How to get Google Gemini API Key"):
            st.markdown(
                """
            **Step 1:** Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
            
            **Step 2:** Click the "Create API key" button
            
            **Step 3:** Select your Google Cloud project or create a new one
            
            **Step 4:** Copy your API key and paste it in the field above
            
            ⚠️ **Important:** Keep your API key secure and don't share it!
            """
            )

    # Validación de API key
    if api_key:
        if model_provider == "openai" and api_key.startswith("sk-"):
            st.success("✅ OpenAI API key format looks correct")
        elif model_provider == "gemini" and api_key.startswith("AIza"):
            st.success("✅ Google API key format looks correct")
        else:
            st.warning("⚠️ API key format may be incorrect")
    else:
        st.info(f"💡 Enter your {model_provider.upper()} API key to get started")

# Main interface
uploaded_file = st.file_uploader("Upload a requirements document (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.success("Document processed successfully!")

    # Mostrar información del documento
    with st.expander("📄 Document Information"):
        st.write(f"**Document name:** {uploaded_file.name}")
        st.write(f"**Text length:** {len(text):,} characters")

        # Calcular límite dinámico basado en el modelo seleccionado
        model_limits = {
            "gpt-3.5-turbo": 12000,
            "gpt-4": 24000,
            "gpt-4-turbo-preview": 100000,
            "gemini-pro": 20000,
            "gemini-pro-vision": 20000,
        }

        max_chars = model_limits.get(model_name, 12000)

        if len(text) > max_chars:
            st.warning(
                f"⚠️ Document is large ({len(text):,} characters). "
                f"The model {model_name} can process up to {max_chars:,} characters. "
                f"The text will be intelligently truncated to preserve complete paragraphs."
            )
        else:
            st.info(
                f"✅ Document size is optimal for {model_name} "
                f"({len(text):,}/{max_chars:,} characters)"
            )

    action = st.radio(
        "What do you want to generate?",
        ["User Stories", "Gherkin User Stories", "Test Scenarios", "Test Cases"],
        help="Select the type of testing artifact to generate",
    )

    if st.button("🚀 Generate", type="primary"):
        if not api_key:
            st.error(
                f"⚠️ Please enter your {model_provider.upper()} API key to continue"
            )
        else:
            with st.spinner(
                f"Generating with {model_provider.upper()} {model_name}..."
            ):
                try:
                    results = generate_test_artifacts(
                        text, action, model_provider, model_name, api_key
                    )

                    if results.startswith("Error"):
                        st.error(results)
                    else:
                        st.success("Generation completed!")
                        st.text_area(
                            "Generated Output",
                            results,
                            height=300,
                            help="Review the generated content before downloading",
                        )

                        csv_path = save_to_csv(results, action)

                        # Botones de descarga y nueva generación
                        col1, col2 = st.columns(2)
                        with col1:
                            st.download_button(
                                "📥 Download as CSV",
                                open(csv_path, "rb"),
                                file_name=f"{action.replace(' ', '_').lower()}.csv",
                                type="primary",
                            )
                        with col2:
                            if st.button("🔄 Generate Again"):
                                st.rerun()

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.info("Please check your API key and internet connection.")

# Footer with information
st.markdown("---")

# Sección de ayuda
with st.expander("❓ Need Help?"):
    st.markdown(
        """
    ### 🚀 Getting Started
    
    1. **Choose your AI provider** (OpenAI or Google Gemini) in the sidebar
    2. **Select a model** that fits your document size
    3. **Enter your API key** using the tutorial links in the sidebar
    4. **Upload a PDF** with your requirements
    5. **Select the artifact type** you want to generate
    6. **Click Generate** and wait for the results
    
    ### � Available Artifact Types
    
    - **User Stories**: Traditional user stories in "As a... I want... So that..." format
    - **Gherkin User Stories**: BDD-style user stories with Given/When/Then scenarios
    - **Test Scenarios**: High-level test scenarios covering different cases
    - **Test Cases**: Detailed test cases with steps and expected results
    
    ### 🥒 What is Gherkin?
    
    Gherkin is a business-readable language for BDD (Behavior Driven Development):
    - **Feature**: Describes the software feature
    - **Scenario**: Specific test case
    - **Given**: Initial context/preconditions
    - **When**: Action or event
    - **Then**: Expected outcome
    
    Perfect for teams using Cucumber, Behave, or SpecFlow!
    
    ### �📏 Document Size Guidelines
    
    - **Small documents** (< 12K chars): Use GPT-3.5-turbo or Gemini-pro
    - **Medium documents** (12K-24K chars): Use GPT-4 or Gemini-pro
    - **Large documents** (24K-100K chars): Use GPT-4-turbo-preview
    
    ### 🔒 Security Note
    
    Your API keys are only used during the session and are not stored or logged.
    """
    )

st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        🧵 QA Test Case Assistant | Powered by LangChain<br>
        Supports OpenAI GPT and Google Gemini models
    </div>
    """,
    unsafe_allow_html=True,
)
