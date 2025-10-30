# PHASE 2: Agent Workflow

FUNCTION AgentWorkflow(COMPANY_NAME_OR_URL):

    # --- CompanyResearchAgent (CRA)
    CRA = CompanyResearchAgent()

    # Retrieve info from memory (Chroma DB) if there is any
    context = CRA.RetrieveContextFromChroma(COMPANY_NAME_OR_URL)

    # Collect raw company data
    RAW_DATA = CRA.collect_data(
        query=COMPANY_NAME_OR_URL
    )

    # --- IndustryAnalysisAgent (IAA)
    IAA = IndustryAnalystAgent(CRA)

    INDUSTRY = IAA.ClassifyIndustry(RAW_DATA, context)
    PAIN_POINTS = IAA.DeducePainPoints(INDUSTRY, RAW_DATA)
    AI_USE_CASES = IAA.GenerateAIUseCases(INDUSTRY, PAIN_POINTS)

    # --- CopywriterAgent (CWA)
    CWA = CopywriterAgent(IAA)

    # Create personalized email content using analysis and branding info
    EMAIL_SUBJECT, EMAIL_BODY = CWA.CreateEmail(
        industry=IAA.INDUSTRY,
        pain_points=IAA.PAIN_POINTS,
        ai_use_cases=IAA.AI_USE_CASES
    )

    # Add branding (logo, colors) and meeting link
    FINAL_EMAIL = CWA.embed_branding_and_meeting_link(
        subject=EMAIL_SUBJECT,
        body=EMAIL_BODY,
        BRANDING_CONFIG=LoadBrandingConfig(), # FROM PHASE 1
    )

    # Return structured result
    RETURN information {
        "company": COMPANY_NAME_OR_URL,
        "industry": INDUSTRY,
        "email_subject": EMAIL_SUBJECT,
        "email_body": EMAIL_BODY,
        "ai_use_cases": AI_USE_CASES,
        "final_email": FINAL_EMAIL
    }
