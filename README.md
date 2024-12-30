# No false negatives in a RAG pipeline

At retrieval stage in a Retrieval Augmented Generation (RAG) pipeline, it is crucial extract the most relevant document from a large corpus of texts. A particularly useful question to focus on when designing the retrieval stage is: how to guarantee that, while false positives can be extracted (and manually discarded upon user's inspection), the retrieval stage does not result in false negative, i.e. all information relevant for a given query is successfully extracted from the corpus. While too many false positives are also undesirable, in certain contexts a user can immediately recognize whether a reported answer does not satisfy the demands of the query, while they cannot be sure whether missing information was left unretrieved: this is why "no false negatives" makes for a minimal requirement for the retrieval stage of a RAG pipeline.

Here, I present a custom retriever method and I show that it performs well on the false negative rate. This is based on a custom similarity search, coupled with an (optional) keyword-based search, and an LLM-based reranker.

The custom similarity search is based on the assumption that the number of retrieved chunks as a function of similarity threshold will follow a distribution such as the one in the figure, i.e.: a low number of documents will result similar to a query (similarity equal to or close to 1). When progressively reducing the similarity threshold, there will be a sudden "jump" in the number of retrieved documents (when the documents will stop being relevant for the query), followed by a plateau that gets to the total number of documents when they similarity approaches 0. The "jump"-threshold can then be captured, for example, through the Kneedle algorithm.

<p align="center">
<img width="500" src=https://github.com/alescrnjar/Retrieval_Completeness/blob/main/src/Kneedle.png>
</p>

An LLM-based reranking occurs at answer generation stage (which happens via Chain-of-Thought), since "I DO NOT KNOW" gets printed when the LLM is not able to generate an answer based on the context.

I test this on LLM-generated (and manually inspected) questions for single text splits: for these questions, the text chunk used for generation is marked as ground truth (although the question may inadvertedly refer to other text splits too, resulting in multiple false positives).

# Future Directions
* Improve the retriever so that, together with no false negatives left behind, minimal or no false positives are retrieved.
