import Image from "next/image";
import logo from "../assets/img/logo.jpg";

const Header = () => {
  return (
    <>
      <header>
        <Image src={logo} alt="logo" />
        <h1>I am a header</h1>
      </header>
    </>
  );
};

export default Header;
