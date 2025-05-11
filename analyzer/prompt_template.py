prompt_template = """
Act as a highly skilled ATS (Applicant Tracking System) for Microsoft Dynamics 365 F&O roles.

Evaluate the resume below against the provided job description. Respond in this format:

"Score": "",
"Will the resume get shortlisted": "",
"Missing Keywords": "",
"Relevance of domain in the era": "",
"Will it survive in the next 10 years": ""

Resume: {resume}
Job Description: {job_desc}
"""
