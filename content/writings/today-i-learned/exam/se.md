+++
date = '2026-04-03T10:12:54+05:30'
title = 'Se'
+++

> ##### !NOTE
>
> This is Slop

---

## 📌 Unit 1: Introduction to Software Engineering

### 1. What is Software Engineering?

- **Definition:** An engineering discipline concerned with **all aspects of software production** (from specification to maintenance) using systematic, organized tools and techniques.
- **CS vs. SE:** Computer Science focuses on _theory/fundamentals_; SE focuses on the _practicalities_ of developing and delivering useful software.
- **System Engg vs. SE:** System engineering covers hardware + software + processes. SE is a subset focusing on software infrastructure and applications.

### 2. Software Characteristics (🔥 _PYQ Favorite_)

- **Software is Logical, not Physical:** It is engineered/developed, not manufactured in the classical sense.
- **Software Doesn't "Wear Out" (Hardware vs. Software):**
  - **Hardware (Bathtub Curve):** Fails early due to defects (infant mortality), stabilizes, then fails late due to physical wear/tear (dust, heat).
  - **Software (Actual Deterioration Curve):** Software theoretically has an ideal flat failure rate after initial debugging. However, **it deteriorates**. Every time patches or new features are added, new bugs are inadvertently introduced. The failure rate spikes, creating a progressively higher baseline. It doesn't wear out physically, its logical structure degrades.

### 3. Professional Ethics (ACM/IEEE Code)

Engineers must uphold public interest, respect confidentiality (even without NDAs), protect intellectual property, and avoid computer misuse.

- **8 Principles:** Public, Client & Employer, Product, Judgment, Management, Profession, Colleagues, Self.

---

## 📌 Unit 2: Software Process Models

### 1. Process vs. Methodology (🔥 _PYQ Focus_)

| Feature         | Software Process                                                 | Methodology                                                         |
| :-------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------ |
| **What is it?** | A framework of activities, actions, and tasks to build software. | The specific systematic approach/rules used to execute the process. |
| **Focus**       | **WHAT** needs to be done (e.g., SDLC: Design, Coding, Testing). | **HOW** it is executed (e.g., Agile, Scrum, Waterfall).             |
| **Analogy**     | The broad roadmap.                                               | The specific vehicle & driving style used on the road.              |

### 2. Generic Process Framework

1.  **Communication:** Gather requirements.
2.  **Planning:** Map out tasks, risks, resources, schedule.
3.  **Modeling:** Architecture and design sketches.
4.  **Construction:** Code generation and testing.
5.  **Deployment:** Delivery, evaluation, and feedback.

- **Umbrella Activities:** Occur throughout the project (e.g., Risk management, Quality assurance, Configuration management, Tracking).

### 3. Agile Development

- **Goal:** Rapid, incremental delivery; highly adaptable to changing requirements.
- **Manifesto Core:** Individuals & interactions > processes/tools; Working software > docs; Customer collaboration > contracts; Responding to change > following plans.
- **Extreme Programming (XP):** Relies on 5 values (Communication, Simplicity, Feedback, Courage, Respect). Uses **user stories**, pair programming, and test-driven development (TDD).
- **Scrum:** Work partitioned into "sprints", driven by a "backlog". Emphasizes short daily meetings.

---

## 📌 Unit 3: Requirement Engineering

> 💡 **Intuition:** If you don't know what to build, you will build the wrong thing perfectly.

### 1. Types of Requirements

- **Functional:** What the software _must do_ (features, inputs, outputs).
- **Non-Functional:** How _well_ it does it (Quality attributes: Usability, Reliability, Performance, Portability).

### 2. Elicitation Techniques (Gathering)

- **Interviews:** Structured or open-ended.
- **Brainstorming:** Group idea generation without immediate vetting.
- **FAST (Facilitated Application Spec Techniques):** Joint team of customers + developers.
- **QFD (Quality Function Deployment):** Translates customer voice into technical specs (Categorizes needs into: Normal, Expected, Exciting).

### 3. SRS (Software Requirements Specification)

The official document/contract between developer and customer.

- **Characteristics of a Good SRS:** Correct, Unambiguous (only one interpretation), Complete, Consistent (no conflicts), Ranked for importance, Verifiable, Modifiable, Traceable.

---

## 📌 Unit 4: System Modeling (DFDs & UML)

### 1. Data Flow Diagrams (DFDs) (🔥 _Guaranteed PYQ_)

Shows how data moves through the system.

- **Symbols:**
  - **External Entity (Rectangle):** Data source or sink (e.g., User, Sensor).
  - **Process (Circle/Bubble):** Action performed on data (Verb phrase).
  - **Data Store (Open Rectangle):** File or database.
  - **Data Flow (Arrow):** The data in transit.
- **Levels:**
  - **Context Diagram (Level 0):** The entire system as **one single bubble**. Shows external entities and major data flows in/out. No internal data stores shown.
  - **Level 1 DFD:** Breaks the Level 0 bubble into major high-level subsystems (3-7 bubbles). Internal data stores appear.
  - **Level 2 DFD:** Zooms into a specific Level 1 bubble to show fine-grained logic.
- **Balancing:** Inputs/Outputs entering a bubble at Level N must exactly match the inputs/outputs of its decomposed diagram at Level N+1.

### 2. Use Case Diagrams (UML)

Shows system behavior from user's perspective.

- **Actors:** Stick figures (Users, legacy systems, external hardware).
- **Use Cases:** Ovals (Actions like `[Login]`, `[Book Ticket]`).
- **Relationships:**
  - **Association:** Solid line between actor and use case.
  - **`<<include>>`:** Mandatory sub-task (e.g., `[Checkout]` strictly includes `[Process Payment]`).
  - **`<<extend>>`:** Optional sub-task (e.g., `[Place Order]` might optionally extend to `[Apply Discount]`).
  - **Generalization:** Parent-child inheritance (e.g., `[Credit Card]` inherits from `[Payment]`).

### 3. Sequence Diagrams (UML)

Shows object interactions chronologically.

- **Lifeline:** Vertical dashed line indicating an object's lifespan.
- **Activation (Execution Occurrence):** Thin rectangle on lifeline showing active processing.
- **Messages:** Arrows between lifelines (Solid = Synchronous call, Dashed = Return/Reply). Time flows vertically downward.

---

## 📌 Unit 5: Project Management & Estimation

### 1. Planning Strategies

- **Sliding Window Planning (Rolling Wave):** (🔥 _PYQ Focus_)
  - **What:** Plan immediate phases in intricate detail, and future phases at a high, abstract level. As the project advances (window slides), the next phase is detailed.
  - **Why:** Prevents wasting time creating rigid plans that will inevitably change.
  - **Where:** Best for Agile, R&D, or projects with high initial uncertainty.

### 2. Size Estimation Metrics

- **Lines of Code (LOC) - Problems:** (🔥 _PYQ Focus_)
  1.  **Language Dependent:** 100 LOC in Python does way more than 100 LOC in Assembly.
  2.  **Hard to Estimate Early:** You can't count code before writing it.
  3.  **Penalizes Efficiency:** A master coder refactors logic into 50 lines; a novice writes 200. LOC falsely claims the novice is more productive.
  4.  **No Standards:** Do comments or blank lines count?
- **Function Point Analysis (FP):** Counts actual functionality (Inputs, Outputs, Inquiries, Internal Files, External Interfaces).
  - **Step 1:** Calculate Unadjusted Function Points (UFP = Sum of Count \* Weight).
  - **Step 2:** Compute Degree of Influence (DI = Sum of 14 factors) (14 factors scaled 0-5).
  - **Step 3:** Calculate Value Adjustment Factor (VAF = 0.65 + 0.01 \* DI).
  - **Step 4:** Final FP = UFP \* VAF.

### 3. Effort Estimation Techniques (🔥 _PYQ Focus_)

- **Delphi Technique:** Expert-consensus method. Coordinator gathers anonymous estimates from experts, summarizes them, and experts revise iteratively until consensus. Eliminates "loudest voice" bias.
- **Analytical Techniques:** Uses math/history (like COCOMO or Halstead). Plugs parameters into equations to output Person-Months.

### 4. Mathematical Estimation Models

- **COCOMO (Constructive Cost Model):**
  - Effort (E) = a \* (KLOC)^b [Person-Months]
  - Time (T) = c \* (E)^d [Months]
  - _Modes:_ Organic (small/simple), Semi-detached (medium/mixed team), Embedded (complex/strict constraints).
  - _Intermediate COCOMO:_ Multiplies Nominal Effort by an Effort Adjustment Factor (EAF) based on cost drivers (e.g., Reliability, Team Experience).
- **Putnam vs. Jensen Models:** (Time Compression Penalties)
  - **Putnam:** Cost is inversely proportional to T^4. Extremely punishing. If you compress schedule slightly, cost explodes dramatically.
  - **Jensen:** Cost is inversely proportional to T^2. More moderate and realistic penalty for schedule compression.

---

## 📌 _APPENDIX: Extra High-Yield Topics (Added from Syllabus & PYQs)_

### A. Extended Software Engineering Concepts

- **Types of Software Applications:**
  1.  **System Software:** OS, compilers, file management.
  2.  **Application Software:** Stand-alone programs for specific user needs.
  3.  **Engineering/Scientific:** "Number crunching" algorithms (e.g., orbital dynamics, stress analysis).
  4.  **Embedded Software:** Resides within a product (e.g., microwave keypad control, car dashboard).
  5.  **Product-line Software:** Generic software addressing a mass market (e.g., MS Word).
  6.  **WebApps:** Network-centric, browser-based applications.
  7.  **AI Software:** Uses non-numerical algorithms (e.g., expert systems, robotics).
- **Attributes of Good Software:**
  - **Maintainability:** Must evolve to meet changing needs.
  - **Dependability/Reliability:** Must be trustworthy and safe.
  - **Efficiency:** Should not waste system resources (memory, CPU).
  - **Acceptability/Usability:** Must be understandable and compatible for the users it was designed for.
- **CASE Tools (Computer-Aided Software Engineering):**
  - **Upper-CASE:** Tools supporting early activities (Requirements, Design).
  - **Lower-CASE:** Tools supporting later activities (Coding, Debugging, Testing).

### B. Deep Dive: Requirement Engineering

- **Feasibility Study:** Focuses on whether the product concept is viable, business model realism, market demand, and realistic cost/schedule assumptions.
- **4 Crucial Steps of Requirement Engineering:**
  1.  **Elicitation:** Gathering requirements (Interviews, Brainstorming, FAST, QFD).
  2.  **Analysis:** Refining and scrutinizing to remove ambiguities (creating models/prototypes).
  3.  **Documentation:** Writing the formal SRS document.
  4.  **Review:** Validating the SRS for correctness and completeness.

### C. Deep Dive: System Modeling Notations

- **Sequence Diagram - Message Types:**
  - **Call Message (Solid arrow):** Target lifeline invoked an operation.
  - **Return Message (Dashed arrow):** Information flowing back to the caller.
  - **Self Message (Arrow looping back):** Object invoking its own operation.
  - **Create Message:** Instantiates a new object/lifeline.
  - **Destroy Message:** Requests to terminate the target's lifecycle.
- **DFD Example Breakdown (from PYQ):**
  - _Context Diagram (Level 0):_ Entire system is `Bubble 0`. Connects directly to external entities (e.g., `Customer`, `Supplier`). _No data stores are shown._
  - _Level 1 DFD:_ Breaks `Bubble 0` into main modules (e.g., `1.0 Sales`, `2.0 Production`). Data stores (`D1: Inventory`) appear here.
  - _Level 2 DFD:_ Breaks down a Level 1 bubble (e.g., `1.0 Sales` becomes `1.1 Receive Order`, `1.2 Validate Request`).

### D. Advanced Estimation Calculations (🔥 _PYQ Heavy_)

- **Function Point (FP) Calculation:**
  - **UFP** = (EI × W) + (EO × W) + (EQ × W) + (ILF × W) + (EIF × W)
    _(Weights vary: Low, Average, High)_
  - **DI** = Sum of all 14 influence factors _(Scale 0-5)_
  - **VAF** = 0.65 + (0.01 × DI)
  - **FP** = UFP × VAF
- **COCOMO Model Modes & Formulas:**
  - **Organic:** Small, simple projects, experienced team (a=2.4, b=1.05).
  - **Semi-Detached:** Medium projects, mixed team experience (a=3.0, b=1.12).
  - **Embedded:** Complex, strict constraints, hardware interfaces (a=3.6, b=1.20).
  - _Formulas:_ Effort (E) = a × (KLOC)^b, Time (T) = c × (E)^d
  - _Intermediate COCOMO:_ Actual Effort = Nominal Effort × EAF
- **Project Planning & SPMP:**
  - **SPMP (Software Project Management Plan):** Document detailing the project estimates, resource plan, schedules (Gantt/PERT), and risk management plan.

---

**💡 Final Exam Tip:** Whenever asked to compare hardware/software, draw the two graphs (Bathtub vs Actual Deterioration). For DFDs, never put logic inside a data flow arrow—logic only goes in bubbles! For Use Cases, clearly mark your system boundary rectangle. Good luck!

---

## 🎯 EXAM MASTERY & PYQ TACTICS: Closing the Gap

### 1. Case-Study Diagram Extraction (DFDs & Use Cases)

**The Exam Gap:** Converting messy narrative paragraphs into structured diagrams.

- **Step 1: Noun-Verb Analysis:** Highlight nouns (Entities/Data Stores) and verbs (Processes).
- **Step 2: Actor Identification (Use Cases):**
  - **Primary Actors:** Humans or triggers initiating the action (e.g., _Customer_, _Student_).
  - **Secondary Actors:** External systems/hardware reacting (e.g., _Payment Gateway_, _Printer_).
- **Step 3: DFD Terminology Mapping:**
  - **Context Diagram (Level 0):** The _entire_ system is 1 bubble. **NO** data stores shown. Only External Entities and data flowing in/out.
  - **Overview Diagram (Level 1):** Break the Level 0 bubble into 3-7 major functional subsystems (e.g., _Sales_, _Production_, _Accounts_). Data Stores (_Inventory_, _Orders_) appear here!
  - **Detail Diagram (Level 2):** Zoom into ONE Level 1 bubble. (e.g., _Sales_ becomes _1.1 Receive Order_, _1.2 Validate_, _1.3 Record_).

### 2. Function Point (FP) Numericals: Classification Precision

**The Exam Gap:** Mapping vague descriptions to correct FP parameters.

- **EI (External Inputs):** Data going _into_ the system to update internal files (e.g., "sensor inputs", "student registration form").
- **EO (External Outputs):** Derived/calculated data pushed _out_ (e.g., "printed reports", "calculated dashboards").
- **EQ (External Inquiries):** Simple fetches/retrievals _without_ calculation (e.g., "search queries", "view results").
- **ILF (Internal Logical Files):** Databases maintained _by_ your system (e.g., "local customer DB").
- **EIF (External Interface Files):** Databases maintained by _another_ system, just referenced by yours (e.g., "airline central DB").
- _Exam Flow:_ Calculate UFP → Calculate DI (sum of 14 factors) → Calculate VAF (0.65 + 0.01 × DI) → FP = UFP × VAF.

### 3. COCOMO Numericals: Mode Selection & EAF

**The Exam Gap:** Choosing the right mode from paragraph clues and applying EAF.

- **Organic:** "Small team", "familiar technology", "in-house". (a=2.4, b=1.05)
- **Semi-Detached:** "Mixed team (experienced + inexperienced)", "medium size". (a=3.0, b=1.12)
- **Embedded:** "Complex hardware interface", "real-time constraints", "strict". (a=3.6, b=1.20)
- **EAF (Effort Adjustment Factor):** Multiply all given cost driver multipliers together (e.g., 1.10 × 1.14 × 1.17).
- _Actual Effort_ = E_nominal × EAF.

### 4. Putnam vs. Jensen: Time Compression Penalty

**The Exam Gap:** Calculating the exact % cost explosion when time is reduced.

- **Putnam Model (Cost ∝ 1/T⁴):** Highly punitive. If time (T) drops by 14%, substitute T_new = 0.86 T_old. The cost becomes C_new = C_old × (1/0.86)⁴. Cost explodes massively!
- **Jensen Model (Cost ∝ 1/T²):** Moderate penalty. C_new = C_old × (1/0.86)².
- _Conclusion for Exam:_ Putnam heavily penalizes schedule compression compared to Jensen.

### 5. Sequence Diagram: Object Interaction Construction

**The Exam Gap:** Going from use case to chronological messages.

1.  **Extract Objects:** Put them horizontally at the top (e.g., `:Customer`, `:ATM`, `:BankServer`). Drop vertical dashed _lifelines_.
2.  **Draw Activations:** Thin rectangles on lifelines when the object is "thinking" or processing.
3.  **Order Messages Top-to-Bottom:**
    - Solid arrow →: Synchronous call (e.g., `insertCard()`).
    - Dashed arrow ←: Return/Reply (e.g., `accountValid()`).

### 6. LOC Metric: Structured Criticism Framing

**The Exam Gap:** Structuring a 5-mark theoretical answer.

- **Intro:** Define LOC as a size-based metric.
- **Point 1 (Language Dependency):** 100 lines of Python ≠ 100 lines of Assembly.
- **Point 2 (Estimation Timing):** Impossible to count accurately before coding begins (during SRS phase).
- **Point 3 (Penalizes Efficiency):** A senior dev refactoring code to be shorter appears _less_ productive than a junior dev writing bloated code.
- **Point 4 (Counting Rules):** No standard on blank lines, comments, or brackets.
- **Conclusion:** FP (Function Points) is superior because it measures functionality, not arbitrary lines.

### 7. "Software Does Not Wear Out" (Graph Expectation)

**The Exam Gap:** A visual graph is mandatory for full marks.
![Hardware vs Software Failure Rate](/hardware_software_failure.png)

- **Hardware (Bathtub Curve):** High infant mortality → stable flat bottom → spikes up at the end due to physical wear (dust, heat, friction).
- **Software (Deterioration Curve):** Initial drop after debugging. Theoretically, it should stay flat forever (Ideal Curve). However, the **Actual Curve** spikes up slightly every time an update/patch is made (introducing new bugs). Over time, the baseline failure rate rises. It deteriorates logically, not physically.
