import "./avatar.scss";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-regular-svg-icons";
import React from "react";

const Avatar = () => {
  return (
    <>
      <div className="avatar">
        <div className="avatar-icon">
          <FontAwesomeIcon icon={faUser} style={{ color: "#000000" }} />
        </div>
        <h3>UserName</h3>
      </div>
    </>
  );
};

export default Avatar;
