import styles from "./home.module.scss";
import Card from "./components/card/Card.jsx";

export default function Home() {
  return (
      <div className={styles.main}>
          <Card />
      </div>
  );
}
