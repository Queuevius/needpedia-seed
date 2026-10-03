import * as fs from "fs/promises";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { FaissStore } from "@langchain/community/vectorstores/faiss";
import { OpenAIEmbeddings } from "@langchain/openai";
import { fetchPDFS } from "./fetchPDF.js";

export const createVectorPedia = async () => {
  try {
    const trainingText = await fs.readFile("./data/txt/qa.txt", "utf8");
    const textSplitter = new RecursiveCharacterTextSplitter({
      chunkSize: 100000,
    });
    const docs = await textSplitter.createDocuments([trainingText]);

    const vectorStore = await FaissStore.fromDocuments(
      docs,
      new OpenAIEmbeddings({ openAIApiKey: process.env.OPENAI_API_KEY })
    );
    await fetchPDFS(vectorStore);
  } catch (e) {
    console.log(e);
    throw new Error(e);
  }
};
