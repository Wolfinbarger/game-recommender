import "./global.scss";
import styles from "./home.module.scss";
import Footer from "./components/footer/Footer";
import Nav from "./components/nav/Nav";
import Cards from "./components/cards/Cards";

function App() {
  return (
    <>
      <Nav />
      <Cards />
      <Footer />
    </>
  );
}

export default App;
