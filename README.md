# StudyBuddy

## Project Overview
StudyBuddy is a group software engineering project designed to support university students in organising their study activities, connecting with peers, and improving collaboration and wellbeing.

## Project Status
This project is currently in **Sprint 1**, focusing on planning, analysis, and development environment setup.

## Technologies
- Node.js
- Express.js
- MySQL
- Docker
- PhpMyAdmin

## Development Environment
The project uses Docker to provide a consistent cross-platform development environment.
All group members are able to run the application locally using Docker.

## Repository
This repository is used for group collaboration, version control, and sprint-based development.

---

## Sprint 1 – Ethical Considerations (Individual Contribution)
During Sprint 1, my individual responsibility was to identify and analyse the key ethical issues relevant to the StudyBuddy project.

The ethical considerations addressed include:

- **Data privacy and protection:**  
  Ensuring that personal and academic data is handled securely, stored responsibly, and processed in compliance with GDPR principles such as data minimisation, purpose limitation, and user rights.

- **Informed consent and transparency:**  
  Providing clear and accessible information to users regarding what data is collected, how it is used, and how long it is retained, enabling informed decision-making.

- **Accessibility and inclusivity:**  
  Designing the system to be usable by students with diverse needs, including consideration of accessibility standards and avoidance of exclusionary design practices.

- **Fairness and bias:**  
  Reducing the risk of bias in system design and future algorithmic features, particularly in recommendation or prioritisation mechanisms.

- **Ethical collaboration and wellbeing:**  
  Promoting respectful communication, shared responsibility, and support within the development team, recognising the pressures of academic workloads and personal circumstances.

This ethical analysis was informed by academic literature, professional ethical guidelines, and relevant legal frameworks.  
The full ethical discussion, including IEEE-formatted references, has been shared with the team member responsible for compiling and submitting the final Sprint 1 PDF deliverable.

## Sprint 2 — Design & Requirements Pack (Submission Evidence)

Sprint 2 focuses on refining requirements and producing design artefacts to prepare for implementation in Sprint 3.  
All Sprint 2 deliverables are stored in the repository under `docs/sprint2/` to support review and demonstration.

### Sprint 2 Artefacts (Links)
- **Project Summary (refined):** `docs/sprint2/project-summary.md`
- **Prioritised User Stories:** `docs/sprint2/user-stories.md`
- **Use Case Diagram (UML):** `docs/sprint2/use-case-diagram.png`
- **Wireframes:** `docs/sprint2/wireframes/`
- **Activity Diagrams / Flowcharts:** `docs/sprint2/activity-diagrams/`
- **Meeting Minutes:** `docs/sprint2/meeting-minutes/`
- **Kanban Screenshot (Sprint evidence):** `docs/sprint2/screenshots/kanban-sprint2.png`

### Project Management
- **GitHub Project / Kanban Board:** (paste your GitHub Projects link here)
- **Repository Link:** (paste repo link here)

---

## Scope (Sprint 2 → Sprint 3 Implementation Plan)

### MVP (Sprint 3 target)
The Minimum Viable Product (MVP) will enable:
1. Student registration and login
2. Creation of a basic study profile (subject, availability, study preferences)
3. Searching for study buddies based on compatibility criteria
4. Sending and responding to study requests (accept/reject)

### Out of Scope (for now)
To maintain quality over quantity in early sprints, the following are intentionally out of scope until core features are stable:
- Real-time chat and messaging
- Notifications and email verification
- Advanced matching algorithms (ML-based recommendations)
- Admin dashboard and moderation tooling

### Non-Functional Requirements (NFRs)
- **Security:** passwords are never stored in plain text; follow best practices for authentication and access control.
- **Privacy:** user profile data is minimised and processed only for matching and collaboration.
- **Reliability:** the system must run consistently across team members’ machines via Docker.
- **Usability:** core flows (register/login/search/request) should require minimal steps and be easy to understand.

---

## Repository Structure (Key Folders)

```text
docs/
  sprint1/
  sprint2/
    project-summary.md
    user-stories.md
    use-case-diagram.png
    wireframes/
    activity-diagrams/
    meeting-minutes/
    screenshots/
src/
app/
docker-compose.yml
README.md

