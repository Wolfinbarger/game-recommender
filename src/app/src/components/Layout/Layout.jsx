import React from "react";
import "../../global.scss";

// Importing components...
import Nav from "../nav/Nav";
import Cards from "../cards/Cards";

export default function Layout({ children }) {
  return (
    <>
      <Nav />

      {children}
    </>
  );
}
