import { generalQA } from "../helpers/QAhelpers/generalQA.js";
import {
  QAfromTxtGPT,
  checkResponse,
} from "../helpers/QAhelpers/queryLangchain.js";

export const question = async (req, res) => {
  const query = req.body.query;
  const general = req.body.general;
  const firstMessage = req.body.firstMessage;
  try {
    let message = "";
    let noAnswer = false;
    if (general) {
      message = await generalQA(query);
    }
    if (!general) {
      message = await QAfromTxtGPT(query, firstMessage);
    }

    if (message && checkResponse(message)) {
      noAnswer = true;
      message =
        "I can't find the answer for it in needpedia, Would you like to Get General Answer ?";
    }
    console.log(message);
    res.status(200).json({ message, type: "bot", noAnswer });
  } catch (e) {
    console.log(e);
    res.status(500).json({ message: e.message });
  }
};
