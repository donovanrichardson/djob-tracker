# Project Overview

Backend:https://github.com/donovanrichardson/djob-tracker

Frontend:https://github.com/donovanrichardson/djob-tracker-frontend

## Project Schedule


|  Day | Deliverable | Status
|---|---| ---|
|Saturday 12| Complete Auth | Complete
|Sunday 13| Add models | Complete
|Monday 14| Add user restrictions to backend | Complete
|Friday 18| *Debugging* | Complete
|Weekend (19,20)| Auto generation of keyword using text analysis | Incomplete
|Monday 21| Add Sublocations to Location model | Incomplete

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
	- user_id
- Location
	- id 
	- rating 
	- user_id

## Endpoints

### POST /api/job/

#### requires:

- a request body that includes
    - **id** ID of the job
    - **title** title of the job
    - **company** name of the employer
    - **description** job description
    - **url** URL of the job

#### returns:
- a Job, including:
    - **id** ID of the job
    - **title** title of the job
    - **company** name of the employer
    - **description** job description
    - **keywords** for a future feature that will let you search for jobs by keywords
    - **location** location of the job
    - **url** URL of the job
    - **rating** user-given rating for the job

### GET /api/job

#### returns:

- An array of Jobs, having the same fields as the response from the above POST request.

### PATCH /api/job/:id

#### requires:

**id** id of the job

- a request body that includes
    - **rating** the new rating for the job

#### returns:
- A Job, having the same fields as the response from the above POST request.

### DELETE /api/job/:id

#### requires:

**id** id of the job


#### returns:
- **message** if the deletion was successful, this message reads "record deleted"
- **record** the deleted Job, having the same fields as the response from the above POST request.

### GET /api/location

#### returns:

- An array of Locations, having the fields:
    - **name** the name of the location. This is the primary key, and is referenced in the Job objects.
    - **rating** the rating of the location.

### PATCH /api/location/:id

#### requires:

**id** id of the location

- a request body that includes
    - **rating** the new rating for the location

#### returns:
- A Location, having the same fields as the response from the above GET request.

### DELETE /api/location/:id

#### requires:

**id** id of the location

#### returns:
- **message** if the deletion was successful, this message reads "record deleted"
- **record** the deleted Location, having the same fields as the response from the above GET request.


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
