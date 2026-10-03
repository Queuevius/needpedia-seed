import React, { useRef, useState } from "react";

const Suggestions = () => {
  let arr = Array.from({ length: 100 }, (_, index) => index + 1);
  console.log(arr?.length);

  return (
    <div className="flex justify-start items-center gap-5 overflow-x-scroll scr w-full p-3 overflow-y-hidden ">
      <ChipsList>
        {arr.map((item) => (
          <Chip key={item} />
        ))}
      </ChipsList>
    </div>
  );
};

export default Suggestions;

export const Chip = () => {
  return (
    <div className="bg-slate-400 px-8 py-1 rounded-full text-white bg-gradient-to-br from-purple-600 to-blue-500 cursor-pointer hover:scale-105 hover:transform transition-transform duration-300 ease-in-out drop-shadow-md">
      Check
    </div>
  );
};

const ChipsList = ({ children }) => {
  const chipsRef = useRef(null);
  const [isDragging, setIsDragging] = useState(false);
  const [startX, setStartX] = useState(null);
  const [scrollLeft, setScrollLeft] = useState(null);

  const handleMouseDown = (e) => {
    setIsDragging(true);
    setStartX(e.pageX - chipsRef.current.offsetLeft);
    setScrollLeft(chipsRef.current.scrollLeft);
  };

  const handleMouseLeave = () => {
    setIsDragging(false);
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const handleMouseMove = (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - chipsRef.current.offsetLeft;
    const walk = (x - startX) * 2;
    chipsRef.current.scrollLeft = scrollLeft - walk;
  };

  return (
    <div
      ref={chipsRef}
      className="flex justify-start items-center gap-5 overflow-x-scroll w-full p-3 overflow-y-hidden scr"
      onMouseDown={handleMouseDown}
      onMouseLeave={handleMouseLeave}
      onMouseUp={handleMouseUp}
      onMouseMove={handleMouseMove}
      style={{ scrollBehavior: "auto" }}
    >
      {children}
    </div>
  );
};
