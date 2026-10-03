import React from "react";

const Message = ({
  text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, porro?Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, porro?",
  type,
}) => {
  const botImg = "https://cdn-icons-png.flaticon.com/512/1484/1484883.png";
  const userImg =
    "https://reputationprotectiononline.com/wp-content/uploads/2022/04/78-786207_user-avatar-png-user-avatar-icon-png-transparent.png";
  const errorImg = "https://cdn-icons-png.flaticon.com/512/1182/1182730.png";
  return (
    <div
      className={`flex  gap-3 items-center p-3 ${
        type === "bot" || type === "error" ? "row" : "flex-row-reverse"
      } `}
    >
      <img
        width={30}
        height={30}
        className="rounded-2xl"
        src={type === "user" ? userImg : type === "error" ? errorImg : botImg}
        alt=""
      />
      <p
        className={`${
          type === "bot" ? "bg-gray-700" : "bg-gray-500"
        } text-stone-100 rounded-lg p-2`}
        dangerouslySetInnerHTML={{
          __html: `${text?.replaceAll("\n\n", " <br/> <br/> ")}`,
        }}
      ></p>
    </div>
  );
};

export default Message;
