from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Please predict the most appropriate arXiv Computer Science (CS) subcategory for the paper. The predicted sub-category should be in the format 'cs.XX'."
    },
    {
      "role": "user",
      "content": "Abstract: We investigate the behaviour of attention in neural models of visually grounded speech trained on two languages: English and Japanese. Experimental results show that attention focuses on nouns and this behaviour holds true for two very typologically different languages. We also draw parallels between artificial neural attention and human attention and show that neural attention focuses on word endings as it has been theorised for human attention. Finally, we investigate how two visually grounded monolingual models can be used to perform cross-lingual speech-to-speech retrieval. For both languages, the enriched bilingual (speech-image) corpora with part-of-speech tags and forced alignments are distributed to the community for reproducible research.\nTitle: models of visually grounded speech signal pay attention to nouns a bilingual experiment on english and japanese\nDo not give any reasoning or logic for your answer."
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
