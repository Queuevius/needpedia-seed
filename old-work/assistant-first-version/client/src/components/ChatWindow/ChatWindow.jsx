import React, { useState } from "react";
import MessageInput from "./MessageInput";
import ChatBody from "./ChatBody";
import Suggestions from "./Suggestions";

const ChatWindow = () => {
  return (
    <div className=" h-screen flex justify-center items-center px-11 py-8 ">
      <div className="bg-white h-full w-full rounded-2xl flex justify-between items-center flex-col p-2 ">
        <div className="bg-slate-200 rounded-2xl  border-gray-500 shadow-md w-full p-4 text-center">
          <h1 className="text-3xl font-semibold text-neutral-700">
            🤖 Need Pedia Chat Bot 🤖
          </h1>
        </div>
        <ChatBody />
        {/* <Chip /> */}
        {/* <Suggestions /> */}
        <MessageInput />
      </div>
    </div>
  );
};
// Give Your Opinion !🫡
export default ChatWindow;
const Chip = ({ message = "Give Your Suggestions About Post 🔗" }) => {
  return (
    <div className="bg-gradient-to-br from-purple-600 to-blue-500 px-8 py-2 rounded-full text-white cursor-pointer hover:scale-105 hover:transform transition-transform duration-300 ease-in-out drop-shadow-md">
      {message}
    </div>
  );
};
