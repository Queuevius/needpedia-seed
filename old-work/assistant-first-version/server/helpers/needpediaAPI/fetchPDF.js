import axios from "axios";
import { WebPDFLoader } from "langchain/document_loaders/web/pdf";

export const fetchPDFS = async (vectorStore) => {
  try {
    const { data } = await axios.get(
      "https://staging.needpedia.org//pdf_links"
    );
    const links = data?.links?.map((pdf) => {
      return `https${pdf?.url?.split("https")?.[1]}`;
    });
    for (const url of links) {
      const response = await fetch(url);
      const data = await response.blob();
      const loader = new WebPDFLoader(data);
      const docs = await loader.load();
      await vectorStore.addDocuments(docs);
    }
    vectorStore.save("./vectors/needpedia");
  } catch (e) {
    console.log(e);
  }
};
