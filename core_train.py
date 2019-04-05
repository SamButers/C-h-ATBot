from rasa_core.agent import Agent

def core_train():
	agent = Agent("domain.yml", policies=[MemoizationPolicy(), KerasPolicy()]);
	
	data = agent.load_data('stories.md');
	
	agent.train(data);
	agent.persist('./models/dialogue');
	
if __name__ == '__main__':
	core_train();