# 📖 Online Bookstore - Agile Planning Document

## 1. Product Backlog: Prioritized and Justified

### Product Backlog Table:

| **Story ID** | **User Story** | **Priority (MoSCoW)** | **Effort Estimate (1-5)** | **Dependencies** |
|--------------|----------------|-----------------------|--------------------------|------------------|
| **US-001**   | As a customer, I want to search for books by title, author, or genre so that I can easily find books I want to buy. | Must-have | 3 | None |
| **US-002**   | As an admin, I want to add new books to the store so that customers can purchase them. | Should-have | 2 | None |
| **US-003**   | As a customer, I want to borrow books online so that I can read without purchasing. | Must-have | 4 | US-001 |
| **US-004**   | As an admin, I want to generate sales reports so that I can track performance. | Should-have | 3 | US-003 |
| **US-005**   | As a system, I want user data to be encrypted with AES-256 so that security compliance is met. | Must-have | 5 | None |
| **US-006**   | As a customer, I want to receive due date reminders so that I can return borrowed books on time. | Could-have | 2 | US-003 |

### Justification for Prioritization:

- **Must-have Stories**: These are crucial for the core functionality of the Online Bookstore (e.g., searching for books, borrowing books online, and ensuring data security).
- **Should-have Stories**: These stories enhance the system's usability (e.g., adding new books, generating sales reports) but are not essential to the MVP.
- **Could-have Stories**: These are nice-to-have features that improve the user experience (e.g., due date reminders) but are not critical in the initial stages.

## 2. Sprint Plan: Goal, Selected Stories, and Tasks

### **Sprint Goal**:
**"Implement core book search, shopping cart, and checkout functionality to deliver the MVP."**


### **Sprint Backlog Table**:

| **Task ID** | **Task Description**                          | **Assigned To** | **Estimated Hours** | **Status**       |
|-------------|-----------------------------------------------|-----------------|---------------------|------------------|
| **T-001**   | Develop search API endpoint                   | Dev Team        | 8                   | To Do            |
| **T-002**   | Design UI for search results page             | UI Team         | 6                   | To Do            |
| **T-003**   | Implement shopping cart functionality         | Dev Team        | 10                  | To Do            |
| **T-004**   | Design UI for shopping cart page              | UI Team         | 6                   | To Do            |
| **T-005**   | Develop checkout process with simulated payment | Dev Team       | 12                  | To Do            |
| **T-006**   | Design UI for checkout page                   | UI Team         | 6                   | To Do            |
| **T-007**   | Implement review submission functionality     | Dev Team        | 8                   | To Do            |
| **T-008**   | Design UI for review submission form          | UI Team         | 4                   | To Do            |

---

### Traceability to Prior Assignments:

- **Assignment 4 (Functional Requirements)**:
  - **US-001 (Search for books)**: Derived from the requirement to allow customers to search for books based on various criteria (title, author, genre).
  - **US-003 (Borrow books online)**: Reflects the requirement for customers to borrow books online as an alternative to purchasing.
  - **US-002 (Add new books)**: Admin functionality to add books aligns with the requirement for store management.
  - **US-004 (Generate sales reports)**: Reporting functionality helps in tracking the store’s performance.
  
- **Assignment 5 (Use Cases)**:
  - **Use Case: Search for Books** (Mapped to **US-001**)
  - **Use Case: Borrow Books Online** (Mapped to **US-003**)
  - **Use Case: Admin adds new books** (Mapped to **US-002**)
  - **Use Case: Admin generates reports** (Mapped to **US-004**)

---

## 3. 📝 Reflection

### **Challenges in Prioritization**:
- Deciding which features were **Must-have** vs. **Should-have** was difficult. For example, I had to choose between implementing the search functionality (Must-have) and adding reviews (Should-have).
- Balancing user needs (e.g., search functionality) with technical requirements (e.g., encryption) was also challenging.

### **Challenges in Estimation**:
- Estimating effort for tasks with technical complexity (e.g., encryption) was hard because I’m still learning about these technologies.
- Ensuring tasks were small enough to fit into a sprint required breaking down larger tasks into smaller, manageable pieces.

### **Aligning Agile with Stakeholder Needs**:
- Ensuring the MVP delivered value to both customers and bookstore owners was a key focus. For example, the search functionality is critical for customers, while inventory management is important for bookstore owners.
- Managing scope creep was challenging because it’s tempting to add more features, but I had to stay focused on the MVP.

### **Challenges in Understanding the Process**:
When I first started this assignment, I found it difficult to translate system requirements and use cases into user stories. The Agile methodology was new to me, and breaking down tasks into smaller steps felt overwhelming. I spent a lot of time figuring out how to use GitHub effectively, especially since I was working on the browser/beta version, which lacked features like converting notes into issues. This lack of familiarity slowed me down significantly.

### **Lessons Learned**:
Despite the challenges, this assignment taught me a lot about Agile methodology and project management. Here are some key takeaways:
1. **Break Tasks into Smaller Steps:** Breaking down user stories into smaller tasks made them more manageable and easier to estimate.
2. **Ask for Help Sooner:** I spent a lot of time trying to figure things out on my own. In the future, I’ll reach out for help sooner to save time and reduce frustration.
3. **Practice Makes Perfect:** The more I worked with GitHub and Agile tools, the more comfortable I became. I now feel more confident in my ability to manage projects using these methodologies.
4. **Patience is Key:** This assignment required a lot of patience and persistence. I learned that it’s okay to take things one step at a time and not rush through the process.
