# PHASE 1: Input & Config

# 1. Environment setup
FUNCTION InitializeEnvironment()
    # 1.1 Load API key, connect to LLM
    openai_api_key = GET_ENV_VAR("OPENAI_API_KEY")

    # 1.2 Initialize LangChain
    LLM = LangChain.LLM(model="gpt-4-turbo", api_key=openai_api_key)

    # 1.3 Initialize embedding model (needed for Chroma DB)
    EMBEDDING_MODEL = LangChain.Embeddings.OPENAI_EMBEDDING(api_key=openai_api_key)

    RETURN LLM, EMBEDDING_MODEL
END FUNCTION

# 2. Chroma DB setup
FUNCTION SetupTools(EMBEDDING_MODEL)
    # 2.1 Configure Chroma DB
    VECTOR_DB = Chroma.Client.get_collection(
        name="outreach_success_memory",
        embedding_function=EMBEDDING_MODEL
    )

    CHROMA_RETRIEVER = LangChain.VectorStoreRetriever(VECTOR_DB)

    # 2.2 Integrate Google Search API
    SEARCH_TOOL = LangChain.Tool.from_function(
        func=GOOGLE_SEARCH_API.query,
        name="Google Search Tool",
        description="Searches web for company data, products, and news."
    )

    RETURN CHROMA_RETRIEVER, SEARCH_TOOL, VECTOR_DB
END FUNCTION

# PDF file
FUNCTION LoadBrandingConfig()
    # 3.1 Load standardized info for the PDF file. Example branding_config.json:
    """
    {
      "sender_name": "John Doe",
      "sender_title": "AI Solutions Lead",
      "sender_email": "johndoe@ai.io",
      "primary_color": "#007AFF",
      "logo_path": "file://assets/logo.png",
      "calendly_url": "https://calendly.com/ai-15min",
      "email_signature": "\n\nBest Regards,\n{sender_name}\n{sender_title}"
    }
    """

    CONFIG = LOAD_JSON("branding_config.json")

    RETURN {
        "logo_path": CONFIG.logo_path,
        "primary_color": CONFIG.primary_color,
        "calendly_base_url": CONFIG.calendly_url,
        "sender_name": CONFIG.sender_name
    }
END FUNCTION

# Phase 1 - Main Execution
FUNCTION OrchestratorStartup(company_input)
    LLM, EMBEDDING_MODEL = InitializeEnvironment()
    CHROMA_RETRIEVER, SEARCH_TOOL, VECTOR_DB = SetupTools(EMBEDDING_MODEL)
    BRANDING = LoadBrandingConfig()

    context = {
        "LLM": LLM,
        "EMBEDDING_MODEL": EMBEDDING_MODEL,
        "CHROMA_RETRIEVER": CHROMA_RETRIEVER,
        "SEARCH_TOOL": SEARCH_TOOL,
        "VECTOR_DB": VECTOR_DB,
        "BRANDING": BRANDING,
        "company_input": company_input
    }

    RETURN context
END FUNCTION
