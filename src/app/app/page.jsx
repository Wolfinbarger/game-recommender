import styles from "./home.module.scss";
import Cards from "./components/cards/Cards.jsx";

export default function Home() {
  return (
      <div className={styles.main}>
          <Cards />
      </div>
  );
}
