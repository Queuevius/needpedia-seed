import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getModel, setModel } from "../../redux/slices/dataSlice";

const SelectBot = () => {
  const model = useSelector(getModel);
  const dispatch = useDispatch();
  const handleSelect = (btn) => {
    dispatch(setModel(btn));
  };
  return (
    <div>
      <h1 className="text-2xl text-white text-center pb-6">
        {model === "GEMINI"
          ? "Using Gemini AI"
          : model === "GPT"
          ? "Using Chat gpt"
          : "Select Ai Model"}
      </h1>
      <button
        onClick={() => handleSelect("GEMINI")}
        className="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white"
      >
        <span className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
          Gemini AI
        </span>
      </button>
      <button
        onClick={() => handleSelect("GPT")}
        className="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white dark:text-white "
      >
        <span className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-gray-900 rounded-md group-hover:bg-opacity-0">
          Chat Gpt
        </span>
      </button>
    </div>
  );
};

export default SelectBot;
