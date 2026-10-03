import "cheerio";
import { ConversationalRetrievalQAChain } from "langchain/chains";
import { BufferMemory } from "langchain/memory";
import { PromptTemplate } from "@langchain/core/prompts";
import { FaissStore } from "@langchain/community/vectorstores/faiss";
import { OpenAIEmbeddings, ChatOpenAI } from "@langchain/openai";
// Memory Instance
const memory = new BufferMemory({
  memoryKey: "chat_history",
  returnMessages: true,
  inputKey: "question",
});

// Using OPENAI
export const QAfromTxtGPT = async (query, firstMessage) => {
  try {
    if (firstMessage) {
      await memory.clear();
    }
    const model = new ChatOpenAI({
      openAIApiKey: process.env.OPENAI_API_KEY,
    });
    const embeddings = new OpenAIEmbeddings({
      openAIApiKey: process.env.OPENAI_API_KEY,
    });
    const vector = await FaissStore.load("./vectors/needpedia", embeddings);

    const prompt3 = `Handle greetings and answer general questions in a professional and friendly manner.
    For greetings:
    Respond with greetings like "Hi!", "Hello there!", or "Good [morning/afternoon/evening]!".
    If the greeting includes the user's name, personalize your response (e.g., "Hi, how can I help you today?").
    For general questions:
    If the answer is directly available in the provided context or chat history, use it to answer concisely within three sentences. If the answer is not available in the context but you have general knowledge about it, provide a brief and informative response, mentioning that the information is not directly from the given context.
    If you cannot answer the question due to lack of information, be honest and say "I can't find the answer to that in the provided information. Handle greetings and answer general questions in a professional and friendly manner.
    Remember:
    Maintain a professional yet friendly tone. Focus on providing factual and helpful information.
    Use three sentences maximum and keep the answer as concise as possible.

    If the user wants to get idea about some Post also send the Post ID of the post but put Post ID at first of the the message. You must Give me the ID of the Post in the following pattern, with square brackets arround like this, [ID]

    {context}
    {chat_history}
    Human: {input} Current conversation:
    AI:
    
    `;
    const prompt = PromptTemplate.fromTemplate(prompt3);
    /* Create the chain */
    const chain = ConversationalRetrievalQAChain.fromLLM(
      model,
      vector.asRetriever(),
      {
        memory,
        prompt,
      }
    );
    const res = await chain.invoke({ question: query });
    return res?.text;
  } catch (e) {
    console.log(e);
    throw new Error(e);
  }
};
export const checkResponse = (str) => {
  const check = `I don't know`;
  const check1 = `I don't have`;
  const check2 = `I'm sorry`;
  return str.includes(check) || str.includes(check1) || str.includes(check2);
};
