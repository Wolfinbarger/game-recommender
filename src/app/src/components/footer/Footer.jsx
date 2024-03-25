import "./footer.scss";
const Footer = () => {
  return (
    <footer className="flex flex-row justify-between px-5">
      <p className="text-xs">Copyright @ 2023 Clever Penguin Design</p>
      <p className="text-xs ">Contact Us</p>
    </footer>
  );
};

// TODO: Render footer if the browser is loading the next set of games
// https://github.com/Wolfinbarger/game-recommender/issues/57
export default Footer;
