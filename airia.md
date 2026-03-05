onllaw

## Idea
This is the idea I am thinking of building.  It is a web app called onllaw.  Context: A lot of people in Ontario, Canada are taken advantage of when giving employment contracts or severance.  The goal is to democratize this information and empower employees to ask better questions and know their rights.  It will be built using (agentic AI would be the main tool). The key reference material would be (https://www.ontario.ca/laws/statute/00e41). I will provide a word file of the site as well.  In terms of features, it two core features employment standards Q&A and contract review.  For employment standards Q&A, user would be able to ask a question regarding employment standards.  For the second option, the user would have the ability to upload an employment contract, the app would analyze it and highlight key information, potential key issues as well.  The user can then ask questions as well.  they user would also have the ability to contact employment lawyers in ontario (focus will be on the GTA for now), .  It would also provide an email draft that a succint based on the issue highlighted in the contract.  
Rate it on a scale of 1 to 10 using the judging criteria and provide clear reasoning on why that line of thinking was created. Second provide 2-3 suggestions on how to improve it, if it does not score at least a 9 out of 10.   

Judging criteria
Technological Implementation
Does the project demonstrate quality software development? Does the project thoroughly leverage the required tool? How is the quality of the code?
Design
Is the user experience and design of the project well thought out? Is there a balanced blend of frontend and backend in the software?
Potential Impact
How big of an impact could the project have on the enterprise? How big of an impact could it have in the market?
Quality of Idea
How creative and unique is the project? Does the concept exist already? If so, how much does the project improve on it? *

interesting, can it read a web page like this (https://www.ontario.ca/laws/statute/00e41) and then make inferences from it?

Helvetica, Century Schoolbook, Montserrat, Lato






AIRIA_API_URL
AIRIA_API_KEY
AIRIA_AGENT_ID

how to call it
import requests
import json

url = "https://api.airia.ai/v2/PipelineExecution/aac83aa6-f44e-4075-b38f-907a07783171"

payload = json.dumps({
  "userInput": "Example user input",
  "asyncOutput": false
})
headers = {
  "X-API-KEY": "AIRIA_API_KEY",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

## Role defintion
You are an expert Employment/ Labour Lawyer in Ontario, Canada. You represent the interests of the Employee. 
Your mission is to provide rigorous legal analysis based on the up to date verion of the complete Employment Standards Act (ESA), 2000, ensuring every statutory right—from basic wages to complex termination notice—is upheld.


## KNOWLEDGE_SCOPE
- PRIMARY SOURCE: The Employment Standards Act, 2000 (Full Consolidation as of Jan 1, 2026).
- SCOPE: You must cover all core pillars: 
    1. PAYMENT: Minimum wage, overtime (s. 22), and wage protection.
    2. TIME: Hours of work limits (s. 17), rest periods, and eating periods.
    3. LEAVES: All job-protected leaves (Pregnancy, Parental, Sick, Family Medical, etc.).
    4. TERMINATION: Notice of termination (s. 54), pay in lieu, and severance pay (s. 64).
    5. NEW MANDATES: 2026 updates including salary transparency and AI disclosure.


## LEGAL_DOCTRINES
- THE FLOOR: The ESA is the "absolute minimum." You must identify any attempt to provide less than this floor.
- SECTION 5(1): Always apply the rule that an employee cannot "waive" or "contract out" of their ESA rights. If a contract says "No Overtime," it is illegal and void.
- WILFUL MISCONDUCT: Distinguish between "Just Cause" (common law) and the much higher ESA standard of "Wilful Misconduct" required to deny termination pay.


## RESPONSE_HIERARCHY
1. IDENTIFY THE RIGHT: Pinpoint the exact Part and Section of the ESA that applies to the user's issue.
2. ANALYZE ENFORCEABILITY: Does the employer's action or contract clause follow the Act? 
3. STRATEGIC GUIDANCE: Explain the legal consequence (e.g., "This clause is likely void, meaning you could be entitled to more notice").
4. MANDATORY CITATION: Every factual claim must include a statutory reference [e.g., s. 11 for Payment of Wages].


## TONE_AND_GUARDRAILS
- PERSONA: Sharp, protective, and precise.
- RESTRICTION: No US legal concepts (no "At-Will").
- DISCLAIMER: "This summary is based on the ESA and is for informational purposes. It does not replace formal legal advice."



releveant threshold
max results
neighboring chunks


## Clauses for testing
Clause 1: The "Non-Compete" (The 2021 Prohibition Test)

"RESTRICTIVE COVENANT: The Employee agrees that for a period of twelve (12) months following the Cessation Date, the Employee shall not, directly or indirectly, within the Greater Toronto Area, engage in any business, profession, or activity that competes with the Business of the Employer."

Note: Unless this is a "C-Suite" executive, this is 100% void in Ontario.

Clause 2: The "Averaging Agreement" (Overtime Test)

"OVERTIME AVERAGING: The Employee hereby agrees that for the purposes of calculating overtime pay, their hours of work shall be averaged over a period of four (4) separate and non-overlapping weeks. Overtime (1.5x) will only be paid for hours exceeding 176 hours in that four-week block."

Clause 3: The "Probationary" Clause

"PROBATION: The first six (6) months of employment shall be a probationary period. At any time during this period, the Employer may terminate employment without notice or pay in lieu thereof."

Note: ESA notice kicks in after 3 months. A 6-month "no-pay" probation is illegal.

Reject Case 2: The "Non-Contract" (Validation Test)

Text to paste:

"RECIPE FOR APPLE PIE: 1. Preheat oven to 375. 2. Mix flour and butter. 3. Bake for 45 minutes. WARNING: This pie is hot."