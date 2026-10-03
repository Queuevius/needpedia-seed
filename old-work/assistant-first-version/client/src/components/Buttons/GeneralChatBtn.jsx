import React from "react";
import { useDispatch } from "react-redux";
import { pushMessage } from "../../redux/slices/dataSlice";
import useSendMessage from "../../api/message/useSendMessage";

const GeneralChatBtn = ({ message }) => {
  const { sendMessage } = useSendMessage();

  const dispatch = useDispatch();
  const handleMessage = (e) => {
    dispatch(pushMessage({ message, type: "user" }));
    sendMessage(message, true);
  };
  return (
    <div className="flex justify-center items-center">
      <button
        onClick={handleMessage}
        className="cursor-pointer disabled:opacity-35 bg-gradient-to-br from-purple-600 to-blue-500 px-5 p-2 rounded-3xl text-white hover:opacity-75 "
      >
        Answer Generally
      </button>
    </div>
  );
};

export default GeneralChatBtn;
