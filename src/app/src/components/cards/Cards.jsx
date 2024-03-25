// Ref link: https://nextjs.org/docs/app/building-your-application/rendering/client-components

import { useEffect, useState } from "react";
import Card from "../card/Card";
import Footer from "../footer/Footer";

import "./cards.scss";
import InfiniteScroll from "react-infinite-scroll-component";


const BASE_URL = "http://127.0.0.1:8000/api/games?page";


export default function Cards() {
  const [cards, setCards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);

  const fetchData = async (url) => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error: The status is ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (err) {
      throw new Error(`Error fetching data: ${err.message}`);
    }
  };

  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        setLoading(true);
        const initialData = await fetchData(`${BASE_URL}=${page}`);
        setCards(initialData.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchInitialData();
  }, [page]);

  const fetchMoreData = async () => {
    try {
      setLoading(true);
      const newData = await fetchData(`${BASE_URL}=${page + 1}`);
      setCards((prevCards) => [...prevCards, ...newData.data]);
      setPage((prevPage) => prevPage + 1);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="cards">
      <InfiniteScroll
        dataLength={cards.length}
        next={fetchMoreData}
        hasMore={!loading && cards.length < (cards.num_of_objects || Infinity)}
        loader={<p> Loading... </p>}
        endMessage={<Footer />}
        style={{ overflow: "hidden" }}
      >
        {cards.map((card) => (
          <Card key={`card_${card.id}`} game={card} />
        ))}
      </InfiniteScroll>

      {error && <p>Error: {error.message}</p>}
    </section>
  );
}
