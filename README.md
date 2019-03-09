# text-analytics

## Downloads
- [Google pre-trained word2vec](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)
- In Jupyter notebook, run
```
import nltk
nltk.dowload()
```

```
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

domain_file="domain.yml"
model_path="models/dialogue"
training_data_file="stories.md"    
agent = Agent(
    domain_file,
    policies=[MemoizationPolicy(max_history=3), KerasPolicy()]
    )
training_data = agent.load_data(training_data_file)
agent.train(
    training_data,
    epochs=400,
    batch_size=100,
    validation_split=0.2
    )
agent.persist(model_path)
```

### Under `bot.py`
```
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter, NaturalLanguageInterpreter
import rasa_core
from rasa_core import run

interpreter = RasaNLUInterpreter("models/default/current")
agent = Agent.load("models/dialogue", interpreter=interpreter)

def run_bot(dbug=False):
    if dbug:
        init_debug_logging()
    interpreter = NaturalLanguageInterpreter.create("models/default/current")
    from rasa_core.utils import EndpointConfig
    action_endpoint = EndpointConfig(url="http://localhost:5056/webhook")
    agent = Agent.load("models/dialogue", interpreter=interpreter,action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent,channel='cmdline')
run_bot()
```
