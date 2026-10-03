import { ChatOpenAI } from "@langchain/openai";

export const generalQA = async (query) => {
  try {
    const chatModel = new ChatOpenAI({
      openAIApiKey: process.env.OPENAI_API_KEY,
    });
    const answer = await chatModel.invoke(query);
    return answer?.lc_kwargs?.content;
  } catch (e) {
    console.log(e);
    throw new Error(e);
  }
};
