## Inspiration

- In the first time learning about Command Line tool, we found it completely bizzare and complicated. Documentations on this topic are often too detailed and hard to navigate to the essential information, which are somewhat not suitable to first-time users. Acknowledging that, our team started to build a bot that could return a brief and concise manual with sample use along with potentially visualization.

- Why a discord bot you ask? We believe it is always better to have a study buddy to help us than search through the internet! Does it feel great to have friends? Besides, discord is a popular platform that the majority of us is visiting at least once a day.

## What it does

- Our bot will be available 24/7 on discord to answer questions related to command line tools.

- Users do not have follow a certain syntax. That means queries can be made in casual languages. This feature allows more flexibility for many people who are new to command lines. 

- The results will be a embed with organized sections (i.e. Description, Example, and potentially visualization).

## How I built it

- We started by setting up a simple discord client with [discord.py](https://discordpy.readthedocs.io/en/latest/) that can receive and responed with messages. 

- Next, it is connected to the database (i.e. [MongoDB](https://www.mongodb.com/1)) using its wrapper [pymongo](https://pymongo.readthedocs.io/en/stable/) for retrieving data on command line topics. Each topic (e.g., bash, or commands) is organized in documents in name, brief description and sample use. 

- In order to read and analyse casual languages and select the keywords for quuerying, we applied Google's [Diagflow API](https://cloud.google.com/dialogflow/docs). The API agent (think of it as someone to judge users's question) returns the data containing which topic is about.

## Challenges I ran into

- At first, we couldn't think of a good idea to kick start. It took us around 2 hours to pick the idea that we both satisfied. After that, the process of setting up Google Cloud for Dialogflow agent to operate was rather confusing. However, by doing research and trials, we are able to solve it. Additionally, we had some difficulties of reading the Json file.

## Accomplishments that I'm proud of

- We are proud to be able to finish the project in time. The connection between discord and mongodb, dialogflow APIs was new to us at first but we could finally do it.

## What I learned

- We have learnt how to use Dialgoflow and Mongodb. It was also a memorable experience for us to collaborate as a team and work with time constraint.

## What's next for Command line help bot

- We intend to expand the database for more commands. Moreover, together with the terminal commands, the chatbot will be able to assist with command prompt on Windows. Through the time of operation, we will have more data to train our Dialogflow agent to produce more correct response.