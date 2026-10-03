import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  getLoading,
  getMessages,
  getModel,
  pushMessage,
} from "../../redux/slices/dataSlice";
import useSendMessage from "../../api/message/useSendMessage";

const MessageInput = () => {
  const { sendMessage } = useSendMessage();
  const [message, setmessage] = useState("");
  const model = useSelector(getModel);
  const loading = useSelector(getLoading);
  const dispatch = useDispatch();
  const messages = useSelector(getMessages);
  console.log(messages?.length, "TOTAL MESSAGES");
  const firstMessage = messages?.length > 0 ? false : true;
  const handleMessage = (e) => {
    e.preventDefault();
    dispatch(pushMessage({ message, type: "user" }));
    sendMessage(message, false, firstMessage);
    setmessage("");
  };
  return (
    <div className="py-3 p-3 w-full ">
      <form
        onSubmit={handleMessage}
        className="w-full flex justify-between gap-3"
      >
        <input
          value={message}
          onChange={(e) => setmessage(e.target.value)}
          type="text"
          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-neutral-500 focus:border-1  w-full p-2.5"
          placeholder="Ask Questions About Need Pedia"
        />
        <button
          disabled={message?.length === 0 || loading}
          className="cursor-pointer disabled:opacity-35 bg-gradient-to-br from-purple-600 to-blue-500 px-5 p-2 rounded-xl text-white hover:opacity-75"
          type="submit"
        >
          Ask
        </button>
      </form>
    </div>
  );
};

export default MessageInput;
