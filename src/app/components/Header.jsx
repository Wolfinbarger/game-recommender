import Image from "next/image";
import logo from "../assets/img/logo.jpg";
import Avatar from "./Avatar";

const Header = () => {
  return (
    <>
      <header>
        <Image src={logo} alt="logo" />
        <h1>I am a header</h1>
        <Avatar />
      </header>
    </>
  );
};

export default Header;
