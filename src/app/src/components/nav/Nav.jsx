import "./nav.scss";
import Avatar from "../avatar/Avatar";

import logo from "../../assets/img/logo.jpg";
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
        <img src={logo} alt="logo" />
        <ul>
          <li>
            <FontAwesomeIcon
              icon={faHouse}
              className="font-awesome-icon"
              fixedWidth
            />
            Homes
          </li>
          <li>
            <FontAwesomeIcon
              icon={faMagnifyingGlass}
              className="font-awesome-icon"
              fixedWidth
            />
            Search
          </li>
          <li>
            <FontAwesomeIcon
              icon={faGamepad}
              className="font-awesome-icon"
              fixedWidth
            />
            My Games
          </li>
          <li>
            <FontAwesomeIcon
              icon={faPen}
              className="font-awesome-icon"
              fixedWidth
            />
            Wishlist
          </li>
        </ul>

        <Avatar />
      </nav>
    </>
  );
};

export default Nav;
