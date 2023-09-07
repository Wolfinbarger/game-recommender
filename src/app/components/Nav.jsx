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
      <nav className="h-screen w-60 pt-16 pb-0 flex-col bg-secondary border-r border-black shadow-black">
        <Image src={logo} alt="logo" className="pl-7" />

        <ul className="w-48 mt-12 mb-96 pl-7">
          <li className=" hover:bg-primary rounded-lg h-12 w-48 items-center flex space-x-4 pl-6">
            <FontAwesomeIcon
              icon={faHouse}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p>Home</p>
          </li>
          <li className=" hover:bg-primary rounded-lg h-12 w-48 items-center flex space-x-4 pl-6">
            <FontAwesomeIcon
              icon={faMagnifyingGlass}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p className="">Search</p>
          </li>
          <li className=" hover:bg-primary rounded-lg h-12 w-48 items-center flex space-x-4 pl-6">
            <FontAwesomeIcon
              icon={faGamepad}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p className="">My Games</p>
          </li>
          <li className=" hover:bg-primary rounded-lg h-12 w-48 items-center flex space-x-4 pl-6">
            <FontAwesomeIcon
              icon={faPen}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p className="">Wishlist</p>
          </li>
        </ul>

        <Avatar />
      </nav>
    </>
  );
};

export default Nav;
