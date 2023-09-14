import "./globals.scss";
import { Inter } from "next/font/google";
import Footer from "./components/Footer";
import Nav from "./components/Nav";
import "@fortawesome/fontawesome-svg-core/styles.css";
import { config } from "@fortawesome/fontawesome-svg-core";
import { Roboto } from "next/font/google";
config.autoAddCss = false;

const roboto = Roboto({
  subsets: ["latin"],
  weight: "500",
});

export const metadata = {
  title: "Game Recommender",
  description: "Find your next favorite game!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>
        <Nav />
        {children}
        <Footer />
      </body>
    </html>
  );
}
