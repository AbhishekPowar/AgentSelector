# Agent Selector 

You are given the following data for agents
agent
- is_available
- available_since (the time since the agent is available)
- roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.)
When an issue comes in we need to present the issue to 1 or many agents based on an agent
selection mode. An agent selection mode can be all available, least busy or random. In “all
available mode” the issue is presented to all agents so they pick the issue if they want. In least
busy the issue is presented to the agent that has been available for the longest. In random
mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.).
Issues are presented to agents only with matching roles.
Please write a function that takes an input the list of agents with their data, agent selection
mode and returns a list of agents the issue should be presented to.



### Prerequisites

Things you need to install 

```
Python
Django 
```

## Getting Started

Navigate to agentFinder > manage.py

```
    python manage.py runserver
```


## Built With

* Django - web Framework
* sqlite3  Filebased Database

## Author

* **Abhishek Powar** 



## Disclaimer

* Why did I use sqlite?

sqlite is used as a database as it will be easy to copy during evaluation as sqlite is filebased.Any other Database can be used with this Project. All we need  to do  change database configuration in setting.py. Migrate data into new database



