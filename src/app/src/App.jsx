import React from "react";
import Layout from "./components/Layout/Layout";
import Nav from "./components/nav/Nav";
import Cards from "./components/cards/Cards";
import { faDisplay } from "@fortawesome/free-solid-svg-icons";

function App() {
  return (
    <>
      <Nav />
      <Cards />
    </>
  );
}

export default App;
