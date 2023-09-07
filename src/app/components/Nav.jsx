import Image from "next/image";
import logo from "../assets/img/logo.jpg";
import Avatar from "./Avatar";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHouse,
  faMagnifyingGlass,
  faGamepad,
  faPen,
} from "@fortawesome/free-solid-svg-icons";

const Nav = () => {
  return (
    <>
      <nav className="h-screen w-60 pt-16 pb-0 flex-col">
        <Image src={logo} alt="logo" className="pl-7" />

        <div className="mt-12 mb-96 pl-7">
          <button className=" border rounded-lg border-white h-12 w-48 items-center flex justify-center align-middle">
            <FontAwesomeIcon icon={faHouse} style={{ color: "#ffffff" }} />
            <p className="ml-1">Home</p>
          </button>
          <button className=" border rounded-lg border-white h-12 w-48 items-center flex justify-center align-middle">
            <FontAwesomeIcon
              icon={faMagnifyingGlass}
              style={{ color: "#ffffff" }}
            />
            <p className="ml-1">Search</p>
          </button>
          <button className="border rounded-lg border-white h-12 w-48 items-center flex justify-center align-middle">
            <FontAwesomeIcon icon={faGamepad} style={{ color: "#ffffff" }} />

            <p className="ml-1">My Games</p>
          </button>
          <button className=" border rounded-lg border-white h-12 w-48 items-center flex justify-center align-middle">
            <FontAwesomeIcon icon={faPen} style={{ color: "#ffffff" }} />
            <p className="ml-1">Wishlist</p>
          </button>
        </div>
        <Avatar />
      </nav>
    </>
  );
};

export default Nav;
