**Course**

IST-303 Software Development (Claremont Graduate University)

**Team Name:** Quiz Masters

**Team Members:**

Annie Ho

Davinder Ghotra

Francis Asomaning

Olalekan David-Banjo  

Kasia Tuszynska

# Installation
### clone this repo
$ git clone https://github.com/eclatealba/QuizMasters.git

**go to the directory**
$ cd QuizMasters

### use virtual env
$ virtualenv ENV && source ENV/bin/activate

### generate static project
$ pip install -r requirements.txt

### export flask app and run
$ set FLASK_APP=app.py (For Windows)
$ export FLASK_APP=app.py (For Mac)

$ flask run


# Project Goal

Over time, there has been an increase in the number of students requesting course waivers at CISAT.

CISAT has mandated the course facilitators to produce a Quiz app to serve as an evaluation for the waiver. If the student passes the quiz, they are eligible for a waiver.

So, the experiment will begin with the IST303 course, and therefore, Professor Wallace has contracted this project to Quiz Masters to develop an app to suit this purpose.

In the stakeholder's deliberation, they realized the quiz app could also serve as an assessment for students enrolled in the IST303 class.

If this experiment succeeds, CISAT will replicate the quiz app for all other courses offered in CISAT.


# Stakeholders

**Course Facilitator**

Professor Wallace is the project sponsor, and he has contracted the IST303 quiz app development to Quiz Masters to fulfill one of CISAT’s requirements for assessing how much understanding the student have in software development. This app would serve as an evaluation for those seeking to waive the IST303 class and an assessment tool for enrolled students.

**Center for Information Systems and Technology (CISAT)**

Our client operates under the directives of CISAT, making CISAT the investor in the IST303 quiz development. Should the quiz app become successful, CISAT intends to replicate this development in other core courses offered in the department.

**Students (End Users)**

Students from the IST303 class and others considering a course waiver will be the end-users who will rely on the app as an assessment and evaluation tool. They will take and complete the quizzes and perform other tasks that Professor Wallace requires. In addition, IST 303 students can seek help from the quizmaster’s help desk when there are issues or confusion.

**Program Coordinator (Secondary Users)**

These stakeholders fall under secondary users as they will be interacting with the products created by the software. Quiz Masters will ensure the IST303 quiz app produces outputs that fit into the workflow of the secondary users. Secondary users could generate reports from the app.

**Team members**

The team members include the product owner, scrum master, and developers.

While it is essential to have a product owner take accountability for the project, so will the scrum master ensure that the agile methodology adheres through collaboration and transparency. Finally, the developers will write the codes and build app interfaces.


# USER STORIES


**Create wireframe for quiz app {Priority 10: 1 Day}**

As a developer, I want to visualize the quiz app architecture prior to development

So that I can reduce the risk of building unnecessary software.

As a course facilitator, I want to see the feasibility of the app prior to development

So that I can be rest assured that the initial requirements are captured in the design.


**Formulate 20 quiz questions {Priority 10: 2 Days}**

As a course facilitator, I want the questions to reflect all topics in the curriculum

So that student’s assessment can be thorough.

As a user, I want the quiz questions to be indicative of what has been learned

So that I can prepare adequately.


**Structure questions for data store {Priority 10: 1 Day}**

As a course facilitator, I want the questions to reside in a data store

So that I access the data easily.

As a developer, I want the questions to be in a dictionary format

So that my codes can work optimally without impacting the app performance.


**Create logic for asking quiz {Priority 10: 1 Day}**

As a course facilitator, I want the question progression to be seamless

So that the quiz is well coordinated without manual intervention.


**Create logic for answering quiz {Priority 10: 2 Days}**

As a course facilitator, I want the students when using the app respond to questions in a True or False format

So that the app can be fun and engaging.


**Translate quiz logic into model {Priority 20: 5 Days}**

As a user, I want the app to be interactive and responsive

So that I can have an itch-free experience when attempting the quiz.


**Test model usability {Priority 20: 2 Days}**

As a developer, I want the app to be evaluated as development progresses

So that I can inspect and adapt my codes to prevent technical debt.

As a course facilitator, I want to be sure that the app will be usable

So that I can keep abreast of its feasibility.


**Build Quiz User Interface {Priority 10: 5 Days}**

As a user, I want the quiz interface to be enticing

So that I can be motivated to practice more quizzes.

As a stakeholder, I want the quiz interface to be appealing

So that I can be motivated to present it to the department.


**Display student scores on screen {Priority 20: 1 Day}**

As a user, I want the scores to be displayed on the screen while the quiz is ongoing

So that I have firsthand information on how I am doing in the quiz.

As a course facilitator, I want the students to see their scores as they progress in the quiz

So that the app provides transparency and a mode for evaluation.


**Populate student's result {Priority 20: 2 Days}**

As a user, I want to know the quiz outcome

So that I know the areas in the IST303 course to improve upon.


**Insert result into Scores table {Priority 20: 2 Days}**

As a course facilitator, I want to keep records of individual student’s score

So that I run quarterly reports to determine how the students are performing.


**Send results to students' email {Priority 30: 2 Days}**

As a course facilitator, I want the quiz result to be sent as email to the student immediately after the quiz

So that the students have a copy of their results for reference.


**Run usability test {Priority 20: 2 Days}**

As a course facilitator, I want to be rest assured that we are moving in the right direction by consistently testing the quiz app

So that we can keep the investor interested in the project.


**Build registration form {Priority 10: 2 Days}**

As a course facilitator, I want students to register prior to taking a quiz

So that the department can monitor students’ operations concerning the quiz usage.


**Create database schema {Priority 10: 2 Day}**

As a developer, I want a maintained database of current users

So that we can constantly be aware of the app usage.


**Registration form validation code {Priority 20: 3 Days}**

As a developer, I want to ensure that students enter the right information when registering for the quiz

So that I can have a reliable database.


**Build User login screen {Priority 10: 2 Days}**

As a course facilitator, I want students to have access to their profiles

So that the students can update their information accordingly.


**Login screen validation code {Priority 20: 3 Days}**

As a developer, I want to ensure that adequate security checks are put in place prior to the student logging in

So that their profiles are secured.


# Project Part B

https://user-images.githubusercontent.com/113940939/193473294-a7fd3be5-05e1-4629-9db2-c40a910b40ea.mp4



# Project Outline

**Milestone 1** 11/1

Iteration 1 - Setup Development Environment (Completed)
 * Calculate Velocity (Kasia, Annie)
 * Identify tasks, based on user stories (Kasia)
 * Define Milestones and Iterations (Kasia)
 * Setup Enviornment (David)
  - Install Virtual Environment
  - Install Python
  - Install Pytest
  - Install Flask
 * Create a "Hello" Page to test the environment (David)
 * Write usage instructions (David)
 
Iteration 2 - Build Quiz Model (In progress - Estimate: 20 days)
 * Setup the RDBMS environment (Kasia) - 3 days
 * RDBMS issues: 10,1
 * Test question issues: 2, 12
 * Create test questions (David, Kasia) - 1 day
 * Define the Minimum Viable Product (David) - 1 day
 * Create CSS templates (David) - 3 days
 * Create HTML styles (David) - 4 days
 * Issues satisfied: 25, 19, 18
 * Issue 15- Build Quiz Engine  (Annie, Davinder, Francis, Kasia, David) - 5 days
 * Issue 26 - Test the build of the quiz engine - 1 day

 

**Milestone 2** 12/6

Iteration 1  - Improve User Experience
  * Work on Quiz Taking experience (Annie, Davinder, Francis) - 5 days 
  * Work on Registration experience (Annie, Davinder, Kasia) - 2 days
  * Work on Login experience (Annie, Davinder, Francis) - 2 days
  * Create quiz scores

Iteration 2 Work on Quiz Taking experience
 * Consolidate the Registration, Login and Test Taking experience
 * Test and Validate the holistic, combined experience


# Velocity

Team Members: 5

Each team member has competing professional and educational responsibiliteis, therfore the velocity for this effort is mitigated by other responsibilities. 

Starting Velocity for the group: .25

 * Milestone 1, Iteration 1 (9/19 - 10/4, 17 days) - 8/8 tasks completed
 * Milestone 1, Iteration 2 (10/5 - 11/1, 26 days with Midterm) - 6 tasks assigned
 * Milestone 2, Iteration 1 (11/2 -11/15, 13 days)
 * Milestone 2, Iteration 2 (11/16 - 12/6, 20 with Thanksgiving)


# Burn Down Chart
Click [here](https://github.com/eclatealba/QuizMasters/blob/main/IST303_QuizMasters_Burndown_chart.xlsx) to see the burndown rate and chart.

# Meeting Record
 * 9/20 -Met in person, discuss approach to part B
 * 9/23 – Met on Zoom
 * 9/27 – Met in person, before class to discuss tasks and velocities
 * 9/27 – Met in person, after class to discuss setup and Part B requirements
 * 9/28 – part of the group met to deploy the python portion of the solution 
 * 9/30 – Email communication with the group regarding status
 * 10/1 – Met on Zoom
 * 10/2 – Final meeting before submitting Plan B to Canvas 
 * 10/2 – Email project status 


# Project Status
![Project status](https://user-images.githubusercontent.com/113940939/193574222-504d7cd9-a0a0-40b1-ad91-1c0241280939.JPG)

Click [here](https://github.com/users/eclatealba/projects/1) to see project progress. 
