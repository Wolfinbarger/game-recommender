import Image from "next/image";
import logo from "../assets/img/logo.jpg";

const Header = () => {
  return (
    <>
      <Image src={logo}></Image>
      <h1>I am a header</h1>
    </>
  );
};

export default Header;
