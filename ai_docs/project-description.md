# Initial Project Feature Description

## Key Use Cases

- As a PVARKI Onborading Team, I want to receive message to spefic Discord channel when new applicant sends Google Form based recruitment form.
- As a PVARKI Onborading Team, I want a new Onboarding GitHub Issue to be created per new applicant.
- As a PVARKI Onborading Team, I want that Onboarding Github Issue labels are updated based on the Issue status change.
- As a PVARKI Onborading Team, I want to receive message to a specific Discord channel if Onboarding GitHub Issue status hasn't changed in specified days.
- As a PVARKI Onborading Team member, I want to receive message to a specific Discord channel and as a DM when Onboarding GitHub Issue status is changed to a specified status.

## Key Features

- create GitHub Issue based on onboarding Google Form info.
- update Github Issue labels to be aligned with Issue status.
- track Github Issues and send Discord message to onbording responsibles linked to specific GitHUb Project board status.
- track Github Issues and send Discord message if Issue status hasn't changed in specified time (time must be configurable).
- assign onboarding issue to specific project board swimlane based on team label
- create weekly onboarding report to GitHub Project status update section

## Target User

PVARKI recruitment team who wants to make Open Source project onboarding flow fluent, consistent, transparent to the rest of the project.

## Performance Requirements

- 

## User Experience

- **Interface**: GitHub Project board showing onboarding flow and status per new project member
- **Functionality**: 
- **Feedback**: Progress indicators for long-running data updates
- **Error Handling**: Inform users when API unavailable or update failures occur
- **Offline Mode**: Provide data from local database with last update timestamp when API unavailable

## Scope & Boundaries

- 

## GitHub setup and configuration

### GitHub Project board issue statuses and corresponding GitHub labels

Format: "GitHub Project Issue status" : "GitHub label"
''' JSON
{
    "New":"ob:new",
    "1st-Intro":"ob:1st-intro",
    "2nd-Intro":"ob:2nd-intro",
    "In-Dev":"ob:in-dev",
    "In-Review":"ob:in-review",
    "Done":"ob:done"
} 
'''

### Project teams and corresponding GitHub labels

- Project teams have names and corresponding GitHub labels. For onboarding flow, each team has named persons to handle onboarding and thus receive onboarding notifications/reminders.
- List of Teams and their named responsible persons are defined in a separatetely. This list is upudated periodically. List contains person Discord name and GitHub handle.
- When team label is assigned to an onbording issue, named team members receive Discord message as a notification.
- Teams should have their own swimlanes on Onbording board and onbording issues should be assigned on each swimlane based on the team label.

Format: "Team" : "GitHub Label"
''' JSON
{
    "OnboardingCore":"team:onboarding-core"
    "TAK":"team:tak",
    "DeployApp":"team:deploy-app",
    "Infra+DevOps":"team:infra-devops",
    "Battlelog":"team:battlelog",
    "StaffTools":"team:staf-tools",
    "Community":"team:community",
    "Kraftwerk":"team:kraftwerk",
    "OrderApp":"team:kraftwerk",
    "InstantMessaging":"team:instant-messaging",
    "PTT":"team:ptt",
    "Drone+Video":"team:drone-video",
}
'''

### GitHub status changes vs Discord messages

- Change-1: "New" (new issue) - send Discord message to specified persons responsible for 1st-Intro
- Change-2: "1st-Intro" -> "2nd-Intro" - send Discord message to another group of people based on 