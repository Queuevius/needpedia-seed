import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import {
  getModel,
  pushMessage,
  setloading,
} from "../../redux/slices/dataSlice";

const useSendMessage = () => {
  const dispatch = useDispatch();
  const model = useSelector(getModel);

  const sendMessage = async (query, general = false, firstMessage = false) => {
    try {
      const localUrl = "http://localhost:5021/query";
      // const liveUrl = "https://needpedia.fineit.io/query";
      const liveUrl = "https://needpedia-server.fineit.io/query";
      dispatch(setloading(true));
      const { data } = await axios.post(localUrl, {
        query,
        general,
        firstMessage,
      });
      dispatch(pushMessage(data));
    } catch (e) {
      console.log(e);
      dispatch(
        pushMessage({
          message: "Some Error Occured, Please Try Again ?",
          type: "error",
        })
      );
    } finally {
      dispatch(setloading(false));
    }
  };
  return { sendMessage };
};

export default useSendMessage;
