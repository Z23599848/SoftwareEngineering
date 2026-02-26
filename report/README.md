# StudyBuddy: Software Engineering Project Report

## Group Details
**Group Name:** Group 777
**Group Members:**
- Ali Ganji (Z23599848)
- Nilay Oral (Z23607537)
- Leilani Grogan-Mowatt (A00019111)
- Maywon Niazi (Z22525705)
- Tavishi Lamba (A00019627)

---

## 1. Project Description
Study buddies is a group software engineering project designed to support university students in organising their study activities, connecting with peers, and improving collaboration and wellbeing. Users can create an account in order to find other people to study or chat with based on a variety of categories, such as the type of course a user is studying or what kind of person they would like to study with. Users can send chat requests to study together, search for people via different filtering categories, and provide ratings for people they have studied with.

---

## 2. Team Code of Conduct
To support a productive and respectful working environment, our team agrees to follow the principles outlined below.

### Communication Standards
- Communicate clearly, respectfully, and professionally with all team members.
- Ensure that everyone has the chance to share ideas, raise concerns, and give feedback.
- Reply to messages and emails from teammates within a 24 hour period.

### Teamwork and Collaboration
- Contribute fairly to group work and support one another in completing tasks.
- Take responsibility for individual duties while holding each other accountable as a team.
- Show flexibility and understanding toward the different commitments and circumstances of team members.

### Compliance with Rules and Policies
- Follow all project-related rules and expectations outlined in this document and elsewhere.
- Act in accordance with University policies and academic regulations at all times.

### Attendance, Availability & Exceptional Circumstances
- All team members are expected to attend scheduled lectures, labs, sprint reviews, and group presentations.
- The affected team member must inform the group as early as possible (at least 12 hours in advance).
- Notification should be made via WhatsApp.

### Managing Non-Compliance
- Continued absence without prior communication may be reported to the module tutor.
- Ongoing failure to complete assigned tasks will be discussed as a group.

---

## 3. Scrum Practices
1. **Sprint Planning:** Every timetabled lesson or whenever requested, the team will meet to decide which tasks will be completed.
2. **Sprint Review:** At the end of each sprint, the team will review work, gather feedback, and identify improvements.
3. **Daily Stand-ups:** Weekly meetings focusing on completed work and current challenges.

### Roles and Responsibilities
- **Scrum Master:** Coordinate and guide the Scrum process. Regularly check progress and address obstacles.
- **Project Owner:** Manage and prioritize the project backlog. Communicate the project vision and objectives.

---

## 4. Ethical Issues
StudyBuddy is designed to be ethically grounded and aligned with professional standards.

### 4.1 Data Privacy and Protection
- **Data Minimisation:** Collect only what is necessary.
- **Purpose Limitation:** Use data only for stated purposes.
- **Integrity and Confidentiality:** Implement secure storage and transport security.

### 4.2 Informed Consent
- Users must understand what data is collected, how matching works, and how to delete accounts.

### 4.3 Security and Secure Engineering
- Mitigation of SQL injection, unauthorized access, and credential exposure via strong hashing and environment variable management.

### 4.4 User Safety and Moderation
- Incorporation of reporting mechanisms, blocking features, and a clear Code of Conduct to prevent harassment.

---

## 5. User Stories
- **US1 – Create profile:** Create a profile with course, year, and modules.
- **US2 – Login to account:** Secure profile and activity.
- **US3 – Search by module:** Find someone studying the same subject.
- **US4 – View user profiles:** Decide if a student is a good match.
- **US5 – Send study request:** Organise a study session.
- **US6 – Accept or decline requests:** Control who you study with.
- **US7 – Dashboard:** See upcoming sessions and pending requests.
- **US8 – Filter by availability:** Find someone free at similar times.
- **US9 – Ratings and feedback:** Leave feedback after a session.
- **US10 – Report or block a user:** Safety against inappropriate behavior.

---

## 6. Diagrams

### 6.1 Class Diagram (Mermaid)
```mermaid
classDiagram
class User {
  +UUID userId
  +String name
  +String email
  +String passwordHash
  +DateTime createdAt
  +AccountStatus status
  +register()
  +login()
  +updateProfile()
}
class Admin {
  +suspendUser(u: User)
  +restoreUser(u: User)
  +removeProfile(p: StudyProfile)
}
class StudyProfile {
  +UUID profileId
  +String subjectArea
  +String availability
  +String preferredStudyMethod
  +String bio
  +DateTime lastUpdated
  +editDetails()
}
class StudyRequest {
  +UUID requestId
  +String message
  +RequestStatus status
  +DateTime createdAt
  +DateTime respondedAt
  +send()
  +accept()
  +reject()
  +cancel()
}
class Notification {
  +UUID notificationId
  +String content
  +NotificationType type
  +DateTime createdAt
  +DateTime readAt
  +markRead()
}
class SearchCriteria {
  +String subjectArea
  +String availability
  +String preferredStudyMethod
}
class RequestStatus {
  <<enumeration>>
  PENDING
  ACCEPTED
  REJECTED
  CANCELLED
}
class AccountStatus {
  <<enumeration>>
  ACTIVE
  SUSPENDED
}
class NotificationType {
  <<enumeration>>
  REQUEST_RECEIVED
  REQUEST_ACCEPTED
  REQUEST_REJECTED
}
User <|-- Admin
User "1" *-- "0..1" StudyProfile : owns
User "1" --> "0..*" StudyRequest : sends
StudyRequest "0..*" --> "1" User : receiver
User "1" --> "0..*" Notification : receives
StudyRequest ..> Notification : generates
User ..> SearchCriteria : uses
User ..> AccountStatus
StudyRequest ..> RequestStatus
Notification ..> NotificationType
```

### 6.2 Sequence Diagram (Mermaid)
```mermaid
sequenceDiagram
    actor UserA
    actor UserB
    participant Frontend
    participant API
    participant AuthService
    participant UserService
    participant SocialService
    participant AcademicService
    participant MessagingService
    participant Database
    UserA->>Frontend: Sign up request
    Frontend->>API: POST /register
    API->>AuthService: Validate & hash password
    AuthService->>Database: Insert USER
    Database-->>AuthService: Success
    AuthService-->>API: Auth token
    API-->>Frontend: Registration success + token
    UserA->>Frontend: Follow UserB
    Frontend->>API: POST /follow
    API->>SocialService: Create follow relation
    SocialService->>Database: Insert FOLLOW
    Database-->>SocialService: Success
    SocialService-->>API: Follow confirmed
    API-->>Frontend: Update UI
    UserA->>Frontend: Create post
    Frontend->>API: POST /posts
    API->>SocialService: Validate & persist post
    SocialService->>Database: Insert POST
    SocialService->>Database: Insert MEDIA (optional)
    Database-->>SocialService: Success
    SocialService-->>API: Post created
    API-->>Frontend: Display post
    UserA->>Frontend: Join study session
    Frontend->>API: POST /sessions/{id}/join
    API->>AcademicService: Validate capacity
    AcademicService->>Database: Insert SESSION_PARTICIPANT
    Database-->>AcademicService: Success
    AcademicService-->>API: Joined
    API-->>Frontend: Confirmation
    UserA->>Frontend: Send message to UserB
    Frontend->>API: POST /messages
    API->>MessagingService: Route to conversation
    MessagingService->>Database: Insert MESSAGE
    Database-->>MessagingService: Stored
    MessagingService-->>API: Delivered
    API-->>Frontend: Message sent
    MessagingService-->>UserB: Real-time notification (WebSocket)
```

### 6.3 ER Diagram (Mermaid)
```mermaid
erDiagram
    UNIVERSITY ||--o{ DEPARTMENT : has
    UNIVERSITY ||--o{ USER : enrolls
    DEPARTMENT ||--o{ COURSE : offers
    DEPARTMENT ||--o{ USER : belongs_to
    USER ||--o{ ENROLLMENT : registers
    COURSE ||--o{ ENROLLMENT : includes
    USER ||--o{ USER_SKILL : has
    SKILL ||--o{ USER_SKILL : referenced_by
    COURSE ||--o{ PROJECT : contains
    PROJECT ||--o{ PROJECT_MEMBER : has
    USER ||--o{ PROJECT_MEMBER : participates
    USER ||--o{ STUDY_SESSION : creates
    STUDY_SESSION ||--o{ SESSION_PARTICIPANT : includes
    USER ||--o{ SESSION_PARTICIPANT : joins
    USER ||--o{ FOLLOW : follows
    USER ||--o{ FOLLOW : is_followed_by
    USER ||--o{ POST : creates
    POST ||--o{ MEDIA : contains
    POST ||--o{ COMMENT : has
    USER ||--o{ COMMENT : writes
    POST ||--o{ POST_LIKE : receives
    USER ||--o{ POST_LIKE : gives
    USER ||--o{ CONVERSATION_PARTICIPANT : joins
    CONVERSATION ||--o{ CONVERSATION_PARTICIPANT : includes
    CONVERSATION ||--o{ MESSAGE : contains
    USER ||--o{ MESSAGE : sends
    UNIVERSITY {
        int university_id PK
        string name
        string location
    }
    DEPARTMENT {
        int department_id PK
        int university_id FK
        string name
    }
    USER {
        int user_id PK
        int university_id FK
        int department_id FK
        string first_name
        string last_name
        string email
        string password_hash
        string academic_level
        string bio
        datetime created_at
    }
    COURSE {
        int course_id PK
        int department_id FK
        string course_code
        string course_name
    }
    ENROLLMENT {
        int enrollment_id PK
        int user_id FK
        int course_id FK
        string semester
        string year
    }
    SKILL {
        int skill_id PK
        string skill_name
    }
    USER_SKILL {
        int user_id FK
        int skill_id FK
        string proficiency_level
    }
    PROJECT {
        int project_id PK
        int course_id FK
        string title
        string description
        datetime deadline
    }
    PROJECT_MEMBER {
        int project_id FK
        int user_id FK
        string role
    }
    STUDY_SESSION {
        int session_id PK
        int created_by FK
        string topic
        string location
        datetime scheduled_time
        int max_participants
    }
    SESSION_PARTICIPANT {
        int session_id FK
        int user_id FK
        string status
    }
    FOLLOW {
        int follower_id FK
        int following_id FK
        datetime created_at
    }
    POST {
        int post_id PK
        int user_id FK
        string caption
        string visibility
        datetime created_at
    }
    MEDIA {
        int media_id PK
        int post_id FK
        string media_url
        string media_type
    }
    COMMENT {
        int comment_id PK
        int post_id FK
        int user_id FK
        string content
        datetime created_at
    }
    POST_LIKE {
        int user_id FK
        int post_id FK
        datetime created_at
    }
    CONVERSATION {
        int conversation_id PK
        string conversation_type
        datetime created_at
    }
    CONVERSATION_PARTICIPANT {
        int conversation_id FK
        int user_id FK
        datetime joined_at
    }
    MESSAGE {
        int message_id PK
        int conversation_id FK
        int sender_id FK
        string content
        datetime sent_at
        boolean is_read
    }
```

### 6.4 Design Diagrams (Images)
- **Use Case Diagram:** ![Use Case](../design/diagrams/Use%20case%20diagram%20for%20StudyBuddy%20system.png)
- **Activity Diagram:** ![Activity Diagram](../design/diagrams/activitydiagram.png)
- **System Flowchart:** ![Flowchart](../design/flowcharts/flowchrt.png)

---

## 7. Project Links
- **GitHub Repository:** [Z23599848/SoftwareEngineering](https://github.com/Z23599848/SoftwareEngineering)
- **Task Board:** [GitHub Project 2](https://github.com/users/Z23599848/projects/2)
- **Meeting Records:** [Meetings Folder](https://github.com/Z23599848/SoftwareEngineering/tree/main/meetings)
