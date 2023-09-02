import "./globals.css";
import { Inter } from "next/font/google";
import Footer from "../components/Footer";
import Header from "../components/Header";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Game Recommender",
  description: "Find your next favorite game!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}

        <Header />

        <Footer />
      </body>
    </html>
  );
}
