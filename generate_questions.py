def question_about_timestamp_split(splits, model="gpt-4o-mini", seed=41):
    print("Generating questions about single text splits with LLM (with associated ground truth metadata)...")
    llm = ChatOpenAI(model=model, temperature=0.0,seed=seed)
    chosen_split=random.choice(splits)
    chosen_splitcontent=chosen_split.page_content
    chosen_time=chosen_split.metadata['timestamp']
    prompt = ChatPromptTemplate.from_messages([("system", "Write a question about the following text chunk, without referring to the speaker or the text:\\n\\n{context}")])
    chain = prompt | llm #| StrOutputParser()
    generation = chain.invoke({"context": chosen_splitcontent})
    return generation.content,[chosen_split.metadata],'generated'

def generic_experiment(splits,chosen_seed=42):
    experiments=[question_about_timestamp_split([random.choice(splits)], seed=chosen_seed) for _ in range(20)]
    return experiments 

