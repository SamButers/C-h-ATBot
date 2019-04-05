from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests, json

class ActionInformCat(Action):
	def name(self):
		return "action_inform_cat";
		
	def run(self, dispatcher, tracker, domain):
		cat = tracker.get_slot('cat');
		
		cat_url = 'https://api.thecatapi.com/v1/breeds/search?q=' + cat;
		
		response = requests.get(cat_url);
		cat_content = response.content.decode();
		cat_json = json.loads(cat_content);
		
		try:
			answer = 'This is the information about {} I could find for you: {}'.format(cat_json[0]['name'], cat_json[0]['description']);
			
		except:
			answer = "Pawrdon me, human. I haven't been able to find infurrmation about your desired cat.";
			
		dispatcher.utter_message(answer);
		
		return [SlotSet('cat', cat)];