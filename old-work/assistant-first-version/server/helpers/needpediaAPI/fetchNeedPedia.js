import axios from "axios";
import * as fs from "fs/promises";
import { createVectorPedia } from "./handleVectors.js";

const filePath = "./data/txt/qa.txt";

export const fetchSaveTXT = async () => {
  const url = "https://staging.needpedia.org/api/v1/faqs";
  const url2 = "https://staging.needpedia.org/api/v1/how_to";
  try {
    await fs.writeFile("./data/txt/qa.txt", " ");
    await getDataQA(url);
    await getDataQA(url2);
    await getPostData();
    await createVectorPedia();
  } catch (e) {
    console.log(e);
  }
};
export const getPostData = async () => {
  try {
    const url = "https://staging.needpedia.org/api/v1/posts";
    const { data } = await axios.get(url);
    const prevData = await fs.readFile(filePath, "utf8");
    const arr = [...data];
    let content;
    arr?.forEach((item) => {
      const post = item?.subject;
      const id = post?.id;
      const title = post?.title;
      const description = post?.content;
      const NoIdeaTxt = "No Ideas Available For this problem";
      const ideaTxt = post?.problems?.map((obj) => {
        const idea = obj?.problem;
        const ideaTitle = idea?.title;
        const ideaDescription = idea?.content;
        const ideas = idea?.ideas?.map((ideass) => {
          const solution = ideass?.idea;
          const solutionTitle = solution?.title;
          const solutionDescription = solution?.content;
          return `
          Solution Title: ${solutionTitle}.
          Solution Description: ${solutionDescription}\n
          `;
        });

        return `
        Idea Title: ${ideaTitle}
        Idea Description: ${ideaDescription}
        Solutions About Idea: ${ideas}
        `;
      });
      let str = `
        Post ID:  ${id}.
        Post Title:  ${title}.
        Post Description: ${description}
        Ideas About the Post Problem:  ${
          ideaTxt?.length === 0 ? ideaTxt : NoIdeaTxt
        }
        `;
      content += str;
    });
    const updatedData = `${prevData}
    ${content}
    \n`;
    await fs.writeFile("./data/txt/qa.txt", updatedData);
  } catch (e) {
    console.log(e);
    throw new Error(e);
  }
};
export const getDataQA = async (url) => {
  try {
    const { data } = await axios.get(url);
    const prevData = await fs.readFile(filePath, "utf8");

    let content = "";
    data?.forEach((item) => {
      content += `Question: ${item.question}\n

        Answer: ${item.answer}\n`;
    });
    const updatedData = `${prevData}
    ${content}
    \n`;
    await fs.writeFile("./data/txt/qa.txt", updatedData);
  } catch (e) {
    console.log(e);
    throw new Error(e);
  }
};
