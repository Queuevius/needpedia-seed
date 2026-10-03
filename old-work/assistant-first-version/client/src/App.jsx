import { useState } from "react";
import "./index.css";
import SelectBot from "./components/Bot/SelectBot";
import ChatWindow from "./components/ChatWindow/ChatWindow";

function App() {
  return (
    // <div className="bg-slate-600 h-[100vh] flex justify-center items-center ">
    //   <div className="w-[50vw] h-[100vh] flex flex-col justify-center  items-center">
    //     <h1 className="font-semibold text-4xl text-white p-20 mt-[-70px]">
    //       Need Pedia Chat Bot
    //     </h1>
    //     <h4 className="bg-gradient-to-br from-purple-600 to-blue-500 px-5 py-2 rounded-lg text-white font-medium">
    //       Utilizing Open Ai Model
    //     </h4>
    //     {/* <SelectBot /> */}
    //   </div>
    // </div>
    <ChatWindow />
    // I frame Code
    // <div className="flex justify-center items-center h-screen">
    //   <iframe
    //     width={700}
    //     height={500}
    //     src="https://needpedia-openai.netlify.app/"
    //     frameborder="0"
    //   ></iframe>
    // </div>
  );
}

export default App;
