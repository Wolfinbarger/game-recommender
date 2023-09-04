import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-regular-svg-icons";

const Avatar = () => {
  return (
    <div className="bg-white h-10 w-10 rounded-full border-2 border-black flex items-center justify-center text-xl ">
      <FontAwesomeIcon icon={faUser} style={{ color: "#000000" }} />
    </div>
  );
};

export default Avatar;
