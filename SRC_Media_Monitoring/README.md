  SRC Sentiment Monitoring Project - README.md
Singapore Red Cross (SRC) Media & Social Monitoring Dashboard
Detailed Phases 1-3 Workflow: Evaluate(Jan) → Launch(Feb) → Monitor(Mar)

 Navigation
Team & Roles | Full Timeline | Setup | Structure | Standards

 Team & Detailed Roles {#team}
Project Lead

Overall coordination, Timeline management

Telegram: @Priy0n

Technical Lead

Web scraping pipeline, AI/NLP model development, GitHub rganisatino

Telegram: @kekwmegalulxd,@manickamgayathri

Data Analyst 1

Sentiment analysis, topic modeling, transcription analysis

Telegram: @yanquix
Email: hlew003@gmail.com


Data Analyst 2

Data preprocessing, metadata enrichment, validarion 

Telegram: @viccc, @Ryan312006
Email: victcwl@gmail.com, Ryanlinan4@gmail.com

Visualisation Lead

Streamlit dashboard, interactive visualization, reporting

Telegram: @geryllll
Email: geryllai@gmail.com


QA & Documentation Lead

Data validation ,process documentation, final reporting  and slides

Telegram: @jodhashivam, @jschewy
Email: shivam21jodha@gmail.com, cheujs@gmail.com





 Complete Timeline {#timeline}
Meeting Schedule
Bi-weekly w/ SRC (Google Meet - stakeholder demos):
12-Jan-2026 (Project kickoff) [DONE]
26-Jan-2026 (Phase 1 demo - TODAY) [IN PROGRESS]
9-Feb-2026 (Phase 1 complete) [IN PROGRESS]
23-Feb-2026 (Phase 2 progress) [IN PROGRESS]
9-Mar-2026 (Final before deadline) [IN PROGRESS]
16-17 Mar-2026 (Final submission) [IN PROGRESS]

Weekly Team Sync (Fridays 6PM Google Meet):
 23-Jan (Week 1-2 update) [DONE]
 30-Jan | 6-Feb | 13-Feb | 20-Feb [IN PROGRESS]
 27-Feb | 6-Mar | 13-Mar (Final prep) [IN PROGRESS]

Phase Breakdown
Phase 1: Evaluate (January) - Infrastructure
Weeks 1–2 (Now):

Project Lead: Finalize scope with SRC

Tech Leads: Selenium pipeline + GitHub org setup

Hezhan: Research HuggingFace multi-language NLP models

Ryan/Victoria: Design data validation checks + SQL schema

Weeks 3–4:

Project Lead: Stakeholder alignment

Tech Leads: Full-scale data collection (Web/Social/Audio)

Hezhan: Setup video→text transcription tools

Ryan/Victoria: Early validation on test extractions

Phase 2: Launch (February) - AI + Dashboard
Weeks 5–6:

Project Lead: Monitor progress, resolve bottlenecks

Tech Leads: Refine scraping efficiency

Hezhan: Sentiment Analysis + LDA topic modeling

Ryan/Victoria: Data cleaning + metadata enrichment

Weeks 7–8:

Project Lead: Validate insights with SRC

Tech Leads: Deploy AI/NLP models

Hezhan: Refine model accuracy

Ryan/Victoria: Ensure data integrity

Week 9:

Project Lead: Dashboard feedback

Tech Leads: Final data→UI integration

Hezhan: Assist Geryl with trend charts

Ryan/Victoria: Validate final dataset

Phase 3: Monitor (March) - Polish + Submit
Weeks 10–11:

Project Lead: Finalize strategic insights

Tech Leads: Production code + documentation

Geryl: Polish Streamlit UI + interactive visuals

Shivam: Conduct final quality checks

Weeks 11–12:

Project Lead: Manage final submission (16-17 Mar)

Tech Leads: Technical handoff

Geryl: Deliver visualization suite

Shivam: Prepare final slides + reports

 Quick Start Guide {#setup}
Prerequisites: Python 3.9+, 16GB RAM, Chrome + Selenium WebDriver

bash
# 1. Clone the repository
git clone https://github.com/[your-org]/src-sentiment-dashboard.git
cd src-sentiment-dashboard

# 2. Install dependencies
pip install -r requirements.txt
# Includes: Selenium, Scrapy, Whisper, Streamlit, pandas, HuggingFace transformers

# 3. Add SRC-provided keyword CSVs
mkdir -p data/keywords
cp ~/Downloads/Company.csv data/keywords/
cp ~/Downloads/Industry.csv data/keywords/
cp ~/Downloads/Partner.csv data/keywords/

# 4. Run full pipeline
python scrapers/run_full_pipeline.py    # Scrapes → data/raw/
python analysis/nlp_pipeline.py         # Analyzes → data/processed/
streamlit run dashboard/app.py          # Launch UI: http://localhost:8501
 Project Structure {#structure}
text
src-sentiment-dashboard/
├── scrapers/                    # Gabrielle & Gayathri
│   ├── news/                    # Straits Times, CNA, 8world, etc.
│   ├── social/                  # Facebook, X, TikTok
│   └── run_full_pipeline.py
├── analysis/                    # Hezhan, Ryan, Victoria
│   ├── sentiment/               # VADER/BERT multilingual
│   ├── topics/                  # LDA topic modeling
│   └── nlp_pipeline.py
├── dashboard/                   # Geryl
│   ├── app.py
│   ├── pages/                   # Sentiment, Topics, Languages
│   └── components/              # Charts + filters
├── data/                        # All project data
│   ├── keywords/                # Company.csv, Industry.csv, Partner.csv
│   ├── raw/                     # Scraped content
│   ├── processed/               # Cleaned + sentiment/topics
│   └── schema.md                # Data dictionary
├── tests/                       # Shivam & Chewy QA
│   ├── qa_checklist.py
│   └── qa_log.md
├── docs/                        # Detailed documentation
│   ├── qa_test_plan.md
│   └── ethics.md
├── requirements.txt
├── README.md ← You are here
└── .gitignore
Data Schema: Title | Date | Author | Source | Content | Keyword_Category | Language | Sentiment | Topics

⚙️ Git Workflow Standards {#standards}
Branch Naming (Mandatory - all branches must follow):

text
feat/scraper-straits-times        # New scrapers/features
feat/dashboard-language-filter    # New UI features
fix/selenium-timeout              # Bug fixes
fix/whisper-audio-encoding        # Technical issues
docs/qa-test-plan-update          # Documentation changes
test/data-validation-script       # QA/test scripts
hotfix/prod-data-corruption       # Emergency production fixes
Commit Messages:

text
feat(scrapers): add TikTok hashtag scraper with rate limiting
fix(analysis): correct Mandarin sentiment scoring bias
docs(test-plan): add Phase 2 validation checklist
Pull Request Checklist:

Branch follows naming convention

Tests pass (python tests/qa_checklist.py)

1 peer review approval

QA checklist updated (data changes)

No merge conflicts

QA Test Plan {#qa}
6 Critical Weekly Checks (before analysis/dashboard):

Source Quality

100% reputable: CNA, Straits Times, verified social accounts

Owner: Hezhan | Frequency: Weekly

Schema Completeness

Zero empty fields: Title, Date, Source, Language

Owner: Shivam | Frequency: Per batch

Deduplication

No duplicate URLs or titles

Owner: Gabrielle | Frequency: Per batch

Keyword Relevance

≥90% records contain SRC keywords from CSVs

Owner: Ryan/Victoria | Frequency: Weekly

Language Accuracy

Auto-detection matches declared language (EN/ZH/MS/TA)

Owner: Shivam | Frequency: Weekly

Data Freshness

≥90% records <7 days old

Owner: Chewy | Frequency: Weekly

Full details: docs/qa_test_plan.md
Log issues: tests/qa_log.md

 Ethics & Compliance {#ethics}
Singapore Legal Requirements:
 PDPA: No personal data collection/storage
 Copyright: Source attribution + original links only
 robots.txt: Checked before every scraper

Technical Safeguards:

Rate Limiting: 1 request/second per domain (Tech Leads)

User-Agent: SRC-Monitor/1.0 (contact@src-project.sg)

Data Retention: Raw data kept 6 months max, then deleted

Access: Private repo, encrypted data folder

Full policy: docs/ethics.md

Week 2 Actions (Due 30-Jan)
Gabrielle/Gayathri: Deploy Selenium scrapers for news sites

Hezhan: Finalize keyword CSVs (4 languages)

Shivam/Chewy: Run first QA validation tests on sample data

All team: Prepare for 26-Jan SRC bi-weekly demo (4PM)

 Phase 1 Infrastructure Ready
Shivam & Chewy (QA Lead)| Updated: 26-Jan-2026
 Next: 30-Jan weekly sync

