import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-regular-svg-icons";
import React from "react";

const Avatar = () => {
  return (
    <>
      <div className="flex flex-row items-center mb-0 bg-secondary pl-7 h-36">
        <div className="bg-white h-10 w-10 rounded-full border-2 border-black flex items-center justify-center text-xl">
          <FontAwesomeIcon icon={faUser} style={{ color: "#000000" }} />
        </div>
        <h3 className="text-white drop-shadow-md ml-3">UserName</h3>
      </div>
    </>
  );
};

export default Avatar;
