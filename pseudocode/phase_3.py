# PHASE 3: Output & Delivery

FUNCTION OutputGeneration(information, BRANDING_CONFIG, recipient_email):
    # 1. Initialize PDF report generator
    pdf_generator = PDFReportGenerator()

    # 2. Convert structured AI use cases into PDF
    PDF_CONTENT = FormatAIUseCases(information.AI_USE_CASES)
    PDF_FILE = PDFGenerator.create_pdf(PDF_CONTENT)

    # 3. Apply brand consistency (logo, colors, fonts)
    BRANDED_PDF = ApplyBranding(PDF_FILE, BRANDING_CONFIG)

    # 4. Initialize output object
    OUTPUT_MODULE = OutputDelivery()

    # 5. Prepare the email with the PDF
    EMAIL_MESSAGE = OUTPUT_MODULE.ComposeEmail(
        recipient=recipient_email,
        subject="AI Opportunities for Your Business",
        body=information.EMAIL_BODY,
        attachment=BRANDED_PDF
    )

    # Step C6: Send the email using Gmail API
    GMAIL_CLIENT = GmailAPI()
    SEND_STATUS = GmailClient.send(information.EMAIL_MESSAGE)

    # 7. Check if the email was successfully sent
    IF SEND_STATUS == "Success":
        # 8. Store data in Chroma DB
        SAVE_TO_DB = {
            "email": recipient_email,
            "ai_use_cases": information.AI_USE_CASES,
            "branding": BRANDING_CONFIG,
            "timestamp": current_time(),
            "status": "sent"
        }
        CHROMA_DB.store(SAVE_TO_DB)

    ELSE:
        log_error("Email delivery failed for:", recipient_email)

    RETURN send_status
