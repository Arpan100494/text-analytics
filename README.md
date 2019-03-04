# text-analytics

## Downloads
- [Google pre-trained word2vec](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)
- In Jupyter notebook, run
```
import nltk
nltk.dowload()
```
- 

settings_md = """
language: "en"
pipeline:
- name: "nlp_spacy"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_crf"
- name: "ner_spacy"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
"""

%store settings_md > settings.md
