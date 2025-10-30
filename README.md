# AI Outreach Agent for Meeting Generation
This project presents a **system architecture and pseudocode** for an **AI Outreach Agent** that automatically generates personalized first-contact emails to potential clients.  

The system is designed to:

- **Research** a target company  
- **Determine** its likely industry and key challenges  
- **Compose** a personalized email explaining how AI could benefit the company  
- **Generate** a short PDF summarizing potential AI solutions

---

## Overview
The architecture uses a combination of agent chaining, memory storage, and automation tools to make the workflow efficient and adaptive.

The overall workflow of the system starts with user input, where the user provides a company name or URL. The branding and configuration module ensures that all emails and reports maintain consistent branding and include standardized elements such as logos, colors, and a meeting link. The CompanyResearchAgent (CRA) collects information from online sources such as company websites, LinkedIn, and Google Search. It also retrieves relevant past outreach results from a Chroma vector memory to provide context and improve personalization. The IndustryAnalystAgent (IHA) classifies the company's industry and identifies potential pain points, while the CopywriterAgent (CWA) generates a personalized email using the analysis results and branding assets. The PDF Report Generator creates a concise, branded document summarizing AI opportunities for the company. Finally, the Output Delivery Module sends the email with the attached PDF through the Gmail API. The system also updates the memory database with the new outreach, enabling continuous learning and future improvements.

---

## Project Architecture

The project is built and executed in three main phases.

![Project Architecture](/diagrams/architecture.png)

### Phase 1: Input & Config

The first phase focuses on setting up the environment and integrating all the necessary tools. It includes initializing the agent framework using LangChain and connecting to an LLM through the OpenAI API. Memory and research tools are set up, including Chroma as the vector database for storing and retrieving past outreach results, and the Google Search API for gathering current company information. This phase also includes creating a branding configuration file to define company assets, templates, and the base URL for scheduling links. By the end of this phase, the environment is fully prepared to support the agent workflow.

![Phase 1](/diagrams/phase_1.png)

### Phase 2: Agent Workflow

The second phase focuses on building the system through agent chaining. The CRA collects raw company data and retrieves relevant context from the vector database, providing a foundation for informed analysis. The IHA uses this data to classify the company’s industry, deduce key challenges, and generate structured AI use cases, guided by past outreach stored in memory. The CWA then creates a personalized, persuasive email, combining the analysis results with branding assets and a meeting link. This phase ensures that the agents work together smoothly, producing consistent and contextually relevant content for each target company.

![Phase 2](/diagrams/phase_2.png) 

### Phase 3: Output & Delivery

The third phase focuses on producing and sending the final outreach materials. The PDF Report Generator converts the structured AI use cases into a short, professional document that maintains brand consistency. The Output Delivery Module automates sending the email with the attached PDF through the Gmail API or an integrated CRM service. Additionally, the system includes a learning loop, where the details of successful outreach campaigns are stored back into the Chroma vector database. This allows the AI Outreach Agent to improve over time, learning from previous interactions and enhancing personalization for future campaigns.

![Phase 3](/diagrams/phase_3.png) 

---

## Technologies Explained

### Memory & Context: **Chroma Vector DB**
Chroma is easy to set up, lightweight, and supports fast semantic searches, allowing the system to quickly find relevant past examples.  
Compared to **FAISS**, Chroma makes it easier to store metadata such as company size, industry, or outreach success — improving learning and decision-making.  
Other vector databases are often more complex or require cloud services, while Chroma offers a simple and efficient local setup.

### Email Automation: **Gmail API**
The **Gmail API** enables the system to send emails programmatically, including attachments like PDFs, without requiring manual intervention. It’s widely used, free for basic accounts, and well-documented for developers. It also supports tracking features such as delivery status. While CRMs like **HubSpot** or **Apollo** offer deeper analytics, they often require paid accounts and complex setup. The Gmail API provides a simpler yet scalable solution for small-scale automated outreach systems.

### Prompt Chaining / Agents: **LangChain**
**LangChain** is used to chain agents for tasks like:
- Research  
- Industry Analysis  
- Copywriting  

It structures the workflow so that each agent focuses on a specific task, while LangChain manages the data flow between them.  
This modular design simplifies debugging, optimization, and integration with other tools (like **Chroma** or **Google Search API**), making the system more intelligent and adaptable.

### Brand Consistency
The system automatically applies **company branding** to generated PDFs and emails — including the logo, color palette, and fonts. Consistent visuals and formatting create a professional, trustworthy appearance and help recipients recognize the brand quickly. This attention to detail increases credibility and improves engagement rates.

### Meeting Link Automation: **Calendly**
A **Calendly link** is embedded automatically in outreach emails, allowing recipients to schedule a meeting instantly. This removes friction in the communication process, improving response and conversion rates. Calendly is a widely trusted scheduling platform that integrates smoothly into automated outreach workflows.
