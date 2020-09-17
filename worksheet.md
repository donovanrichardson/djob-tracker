# Project Overview

Backend:https://github.com/donovanrichardson/djob-tracker

Frontend:https://github.com/donovanrichardson/djob-tracker-frontend

## Project Schedule

This schedule will be used to keep track of your progress throughout the week and align with our expectations.  

You are **responsible** for scheduling time with your squad to seek approval for each deliverable by the end of the corresponding day, excluding `Saturday` and `Sunday`.

|  Day | Deliverable | Status
|---|---| ---|
|Saturday 12| Complete Auth | Complete
|Sunday 13| Add models | Complete
|Monday 14| Add user restrictions to backend | Complete
|Friday 18| *Debugging* | Incomplete
|Weekend (19,20)| Auto generation of keyword using text analysis | Incomplete
|Monday 21| Add Sublocations to Location model | Incomplete

## Project Description

A Job Tracker app that allows users to login, add jobs listings (including job title, description, URL, and location), and filter by location. The backend is a Django API handles CRUD, data validation, authorization, and in the post-MVP will auto-generate keywords.

## Time/Priority Matrix 

[Google Doc](https://docs.google.com/presentation/d/1rycwZD5kk4BVoueygvBN-j5h12f4KutEqMEDGxAW0eE/edit?usp=sharing)

## MVP/PostMVP - 5min


### Functional Components

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional components, and by that we mean functions.  Try and capture what logic would need to be defined if the game was broken down into the following categories.

Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
|Complete Auth|H|5hr| 5hr | -hr|
|Add models|H|5hr| 5hr | -hr|
|Add User restrictions to Job and Location|H|4hr| 2hr | -hr|
|Filter Jobs by Location (Backend)|M|1hr| -hr | -hr|
|Rate Locations|M|1hr| -hr | -hr|
|Debugging|M|6hr| 2hr | -hr|

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
|Sublocations|L|3hr| -hr | -hr|
|Keyword generation based on documents|L|4hr| -hr | -hr|

## Additional Libraries

django-environ to use environment variables

django-heroku== to connect app to Heroku

djangorestframework the main library to create a REST API using Django

djangorestframework-jwt allows authentication

If I do the auto-generated keyword part of the Post-MVP, I will find a library to do a text analysis on job descriptions.

## Models
- User
	- username
	- email
	- password
- Job
	- title 
	- company
	- description 
	- keywords 
	- url
	- location_id 
	- user_id (incomplete)
- Location
	- id 
	- rating 
	- user_id (incomplete)

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

## Previous Project Worksheet
 - [Readme's](https://github.com/jkeohan/fewd-class-repo/tree/master/final-project-worksheet/project-worksheet-examples)
 - [Best of class readme](https://github.com/jkeohan/fewd-class-repo/blob/master/final-project-worksheet/project-worksheet-examples/portfolio-gracie.md)
