# [Eventero.org](https://eventero.org)
Every 5 minutes, the server checks for updates to the main branch. If there are any, it will pull them and make them available immediately after.

## Documentation
This shared folder contains the documentation for the project. In it are the instructions and template for writing documentation.

👉  [Documentation](https://sistemaupr-my.sharepoint.com/:f:/g/personal/ojani_figueroa_upr_edu/Eqlo9P4D4UZHg4bHjCxJs90BfMWxwdf-nHmwlT38ll9_Vw?e=xrcjdD)

## Setting up the development environment

### Node.js
If you don't already have Node.js on your machine, [download it here](https://nodejs.org/en) before continuing with the next steps. You can check if you already have it by running `node --version` On your terminal.

### Cloning Repository
If you haven't already, clone this repository, or make sure to do a `git pull` if you have it cloned already

### Installing Node.js modules
While inside the repository folder, run `npm install`. This will install all necessary dependencies.

### Running the frontend development server
Now you can run `npm run dev-svelte`. This will spin up a local development server which serves
the web page in the URL shown in the terminal after running the command. From here, any changes you make will automatically reload the web page. For certain types of changes, it may not do so automatically, in which case you can do a manual refresh of the page.

### Python
If you don't already have python, [download it here](https://www.python.org/downloads/). Also [install
Python's package manager](https://pip.pypa.io/en/stable/installation/) if you don't already have it.

### Setting up Python environment and installing packages
**macOS/Linux instructions**
```
$ cd ./api
$ python3 -m venv .venv
$ . .venv/bin/activate

$ pip install Flask
```

**Windows Instructions**
```
> cd .\api
> py -3 -m venv .venv
> .venv\Scripts\activate

> pip install Flask
```

### Running the backend development server
By running `npm run dev-api`, you can get the python server up and running and you can now access
the example page on the fontend and the **Get Data From Server** button should now work.

## Running the frontend and backend development servers simultaneously
To run them both at the same time, run the command `npm run devall`

---
---
---
---
---
---
---
---
---

## 1. Problem Background

Students and staff at the university encounter significant challenges when it comes to locating and utilizing campus resources, such as study spaces, computer labs, and faculty offices. The current system for discovering and managing campus events is fragmented, leading to missed opportunities and low engagement. The absence of a centralized platform for accessing both resources and events results in frustration, underutilization, and a disconnected campus experience.

## 2. Target

The goal is to develop a Campus Resource and Event Management App that increases resource utilization by 25% and boosts student event participation by 30% within the first semester. The app aims to provide a one-stop solution for booking campus facilities and staying updated on events, ultimately enhancing student engagement and satisfaction.

## 3. Causes

- **Disjointed Information Sources**: Information about campus resources and events is scattered across multiple platforms, causing confusion and inefficiency.
- **Lack of Real-time Updates**: Students and staff struggle to find real-time availability of resources like study spaces or computer labs.
- **Poor Communication Channels**: Event organizers lack an effective way to reach students and provide timely updates or changes, leading to reduced event attendance.
- **Underutilization of Campus Resources**: The difficulty in locating and booking resources results in many facilities remaining underused.

## 4. Countermeasures

- **Centralized Platform**: Develop an app that consolidates information about campus resources and events, making it easily accessible to students and staff.
- **Real-time Availability and Booking**: Implement a feature that displays the real-time availability of campus resources and allows users to book them directly through the app.
- **Event Management Tools**: Provide event organizers with tools to create, promote, and manage events, including RSVP tracking and notifications.
- **Navigation and Assistance**: Incorporate a map and navigation feature to help users quickly find resources and event locations on campus.

## 5. Evaluation

The success of the app will be evaluated by tracking key metrics such as:

- Resource booking rates
- Event attendance figures
- User satisfaction through surveys and app usage data

These metrics will help assess whether the app meets the target increases in resource utilization and event participation. Feedback from users will be gathered to identify areas for improvement.

## 6. Action/Standardization

If the app achieves its goals, it will be established as the university's standard platform for managing campus resources and events. Guidelines for continuous improvement will be created based on user feedback. The possibility of integrating additional features, such as academic calendars or campus news, will be explored to further enhance the app's functionality and user engagement.
