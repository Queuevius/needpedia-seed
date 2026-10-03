import React from "react";
import Message from "../Message/Message";
import { useSelector } from "react-redux";
import { getMessages } from "../../redux/slices/dataSlice";
import useGetLoading from "../../redux/hooks/useGetLoading";
import GeneralChatBtn from "../Buttons/GeneralChatBtn";

const ChatBody = () => {
  const messages = useSelector(getMessages);
  const loading = useGetLoading();

  return (
    <div className="w-full p-5 flex flex-col-reverse border-black  overflow-y-scroll h-full  scr">
      {loading && <Message type={"bot"} text="Generating Message..." />}
      {messages?.[0]?.noAnswer && (
        <GeneralChatBtn message={messages?.[1]?.message} />
      )}

      {messages?.map((item, index) => (
        <Message key={index} text={item.message} type={item.type} />
      ))}
    </div>
  );
};

export default ChatBody;
