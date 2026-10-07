# PyFlow

A Python data and automation toolkit for collecting, processing, analyzing, and transforming structured information.

## Project Goal

Build a practical Python project that demonstrates API usage, JSON/data processing, automation, error handling, testing, and clean reusable code.

**Primary:** Python  
**Supporting:** REST APIs, JSON, data processing, testing, Git

---

## Core Features

- Read structured data
- Consume data from APIs
- Process and transform information
- Handle JSON
- Handle errors safely
- Automate repetitive data-processing tasks
- Generate structured results
- Test reusable components

---

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python main.py`
6. Run tests: `python -m pytest`

GitHub Actions runs those same tests on every push and pull request (`.github/workflows/ci.yml`).

---

# Progression System

> **Rule:** Build the foundation first. Automation and integrations come after reliable data processing.

### Status Legend

- `[ ]` Not started
- `[~]` In progress
- `[x]` Complete
- `[!]` Blocked / needs investigation

---

## Milestone 0 — Python Foundation

### T0.1 — Repository
- [x] Create GitHub repository
- [x] Add README
- [x] Add `.gitignore`
- [x] Create project structure

### T0.2 — Environment
- [x] Create virtual environment
- [x] Create dependency file
- [x] Document setup instructions

**Done when:** A new environment can install dependencies and run the project.

---

# Milestone 1 — Data Input

### T1.1 — File Input
- [x] Read a structured file
- [x] Handle missing files
- [x] Validate input

### T1.2 — JSON
- [x] Read JSON
- [x] Write JSON
- [x] Validate expected fields
- [x] Handle malformed JSON

---

# Milestone 2 — Data Processing

### T2.1 — Transformation
- [ ] Create reusable processing functions
- [ ] Transform raw data into useful structures
- [ ] Handle missing values

### T2.2 — Analysis
- [ ] Calculate useful statistics
- [ ] Filter records
- [ ] Sort records
- [ ] Generate a summary

**Done when:** Raw data can become useful information through repeatable Python code.

---

# Milestone 3 — API Integration

### T3.1 — API Client
- [ ] Select a public API
- [ ] Send requests
- [ ] Handle successful responses
- [ ] Handle HTTP failures

### T3.2 — API Data Processing
- [ ] Parse response data
- [ ] Validate expected fields
- [ ] Transform API data
- [ ] Save useful results

---

# Milestone 4 — Automation

### T4.1 — Automated Workflow
- [ ] Combine input → processing → output
- [ ] Create a repeatable command/workflow
- [ ] Add configuration options

### T4.2 — Useful Output
- [ ] Generate structured output
- [ ] Produce readable summaries
- [ ] Log important operations

**Done when:** A repetitive data-processing task can be completed automatically.

---

# Milestone 5 — Error Handling

### T5.1 — Failure Cases
- [ ] Handle missing files
- [ ] Handle malformed data
- [ ] Handle API failures
- [ ] Handle unexpected fields

### T5.2 — Reliability
- [ ] Add useful error messages
- [ ] Prevent crashes where appropriate
- [ ] Document known limitations

---

# Milestone 6 — Testing

### T6.1 — Unit Tests
- [ ] Test processing functions
- [ ] Test transformations
- [ ] Test validation

### T6.2 — Integration Tests
- [ ] Test important workflows
- [ ] Test API-related behavior where practical
- [ ] Test failure cases

**Done when:** Core reusable logic is covered by automated tests.

---

# Milestone 7 — Code Quality

- [ ] Refactor duplicated code
- [ ] Improve naming
- [ ] Separate responsibilities
- [ ] Add useful documentation/comments
- [ ] Review dependency usage
- [ ] Review error handling

---

# Milestone 8 — Optional Extension

Only begin after the core toolkit works.

### T8.1 — AI/Data Assistance
- [ ] Choose one narrow AI-assisted workflow
- [ ] Define expected input/output
- [ ] Integrate the service
- [ ] Handle API failures
- [ ] Document limitations

AI should enhance the project rather than replace the core Python engineering.

---

## Definition of Done

A ticket is complete when the feature works, tests pass where applicable, the change is committed, and documentation is updated when necessary.

---

## Final Project Outcome

PyFlow should demonstrate:

- Python programming
- REST API integration
- JSON/data processing
- Automation
- Error handling
- Testing
- Reusable code
- Git/GitHub workflow
