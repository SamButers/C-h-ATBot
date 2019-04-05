![top](https://i.imgur.com/ntraO30.png)

<p align=center>Le Chat, the Chatbot from cats, about cats, to cats!</p>

# How to use
To run the Rasa Core, use the following command:

> python3 -m rasa_core.run -d models/dialogue/ -u models/nlu/default/catnlu/

To train the Rasa Core, use the following command:

> python3 -m rasa_core.train -d domain.yml -s stories.md -c policies.yml -o models/dialogue

To train the Rasa Core interactively, use the following command:

> python3 -m rasa_core.train interactive -d domain.yml -s stories.md -c policies.yml -o models/dialogue

To train the Rasa NLU, use nlu_model.py.
