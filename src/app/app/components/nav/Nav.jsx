import "./nav.scss";
import Avatar from "../avatar/Avatar";

import Image from "next/image";
import logo from "../../../assets/img/logo.jpg";
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
      <nav>
        <Image src={logo} alt="logo" className="pl-7" />

        <ul>
          <li>
            <FontAwesomeIcon
              icon={faHouse}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p>Home</p>
          </li>
          <li>
            <FontAwesomeIcon
              icon={faMagnifyingGlass}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p className="">Search</p>
          </li>
          <li>
            <FontAwesomeIcon
              icon={faGamepad}
              style={{ color: "#ffffff" }}
              fixedWidth
            />
            <p className="">My Games</p>
          </li>
          <li>
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
