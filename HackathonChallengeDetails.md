# How to Code a Job Board
Buiild your own job board to help job seekers and recruiters connect. Implementation will involve a full stack of your choice, involve multiple user roles, support file uploads, and send emails to your users.

**SUBMISSION DATE: THURSDAY AT 12PM EST**

Getting Started:
- [Hitch Hacker's Guide to the Mint-a-Verse](https://sites.google.com/mintbean.io/mintbean-hackathon-guide/mintbean-guidebook?authuser=0)

### How to Submit
[Click here for instructions](https://sites.google.com/mintbean.io/mintbean-hackathon-guide/how-to-submit?authuser=0)
1. Mintbean Platform
2. LinkedIn
3. Discord

#### Step 1 - Mintbean (Mandatory)
-Click on "Submit A Project", only 1 person needs to submit on behalf of team

#### Step 2 - LinkedIn (Mandatory)
[Post Requirements: Example](https://www.linkedin.com/posts/andrewlloyd01_careerhack-reactjs-create-activity-6735011995625644032-uG7A/)
- Blurb about the challenge
- What technologies you used to build it
- What you learned from building this project
- Include project link (Recommend Mintbean Submission Link)
- Tag @Mintbean
- Use relevant hashtags (mintbean, technologies, key word searches)
- 1-3 mins video demoning (screen capture) your project with audio explanation
- If you are in a group, each team member will need to post as well!

#### Step 3 - Discord (Mandatory)

## Schedule (EST)
- **FRIDAY** 1:00 PM - Orientation & Challenge Walkthrough
- **FRIDAY** 4:00 PM - Coffee and Code Mentor Session with Hector Clara
- **MONDAY** 6:00 PM - Coffee and Code Mentor Session with Chung-Ho Lee
- **WEDNESDAY** 12:00 PM - Coffee and Code Mentor Session with Darsh Shah
- **THURSDAY** 12:00 PM - Submission Deadline
- **THURSDAY** 12:15 PM - Demo & Feedback Day
- **MONDAY** 12:00 PM - Winner Announcement

## Homepage
- Storytelling cards contain instructions for how to sell your application. 
  
### Above The Fold
- The title of your application
- An attractive screenshot of your application
- A prominent button with a clear message (ex: "Click here to start") that links to your core app.

### Explainer Section
- What the application does
- How the application works
- Instructions on how to use it to guide the user through the process of using your application

### Team Section
- List the team members
- List the technology used (with icons, for bonus points!)
- Shoutout and link to Mintbean's homepage **helps us grow the community**


## The Employer
a job board users are either a company or a candidate. Therefore, you'll have two distinct kind of "user" entities in your application. Both have different set of actions they can take.

### Examples of What Employer Sees
- Login page for employers
- Form to add a new job with details such as (location, experience level, salary, remote-friendliness, etc).
- list of all jobs I've created
- List of active jobs
- List of past jobs which are now expired
- List of all candidates that have applied to a job
- Way to see candidates' resume and personal details
- Way to mark a candidate as "Pending review", "Rejected", "Contacted", or "Hired"


## Candidates
Employees are looking to find a job. They vary in skillset. They could have multiple versions of resumes they're using to appeal to different types of companies. Many of them have portfoliios that are relevant to their job search. Hardest part for employees' is to find positions that fit their profiles. Various criteria that they consider include: (location, industry, experience level, salary level, etc.). Successful job boards make it easy for employees to be matched to employers quickly and conveniently

### Examples of What Candidates Sees
- Login page for candidates
- Search page for jobs
- Way to filter searched jobs by details such as (location, experience level, salary, remote-friendliness, etc).
- Page which lets me save my resume to the server
- Way to apply for a job with either a newly uploaded resume OR a saved resume
- Way to see whether I've been rejected by a company


## How to Differentiate Between Users and Candidates
DO NOT implement a complex authorization mechanism for this hackathon

Building an application with multiple users, might SEEM like a complex problem at first, but it's actually rather easy. ALl you need is a boolean property on your database's "user" record called user.IsEmployer.

```JavaScript
const user = {
    firstName: "John",
    lastName: "Doe",
    isEmployer: false
}
```

Based on this flag, you can then decide which buttons to show the user, which views to allow the user to access, and which backend endpoints to allow access to.