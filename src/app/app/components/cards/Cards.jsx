// Ref link: https://nextjs.org/docs/app/building-your-application/rendering/client-components
"use client";

import React, { useEffect, useState } from "react";
import Card from "@/app/components/card/Card";

import styles from "./cards.module.scss";
import InfiniteScroll from "react-infinite-scroll-component";

async function getGames() {
  const url = "http://127.0.0.1:8000/api/games/";
  const res = await fetch(url, { cache: "no-store" });

  return res.json();
}

const Cards = () => {
  // const games = getGames();

  // There's an issue with infinite scroll where if no cards are defined initially, then it only renders one card,
  // which doesn't enable scrolling in the component. Without scrolling, the infinite scroll component will not call
  // fetchCard.
  // TODO: We should look into a better way to handle this, since this might not be enough cards for a large screen.
  const initialCardState = [
    { id: 1 },
    { id: 2 },
    { id: 3 },
    { id: 4 },
    { id: 5 },
  ];
  const [cards, setCard] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(null);

  // This function is called by infinite scroll when the user is near the bottom of the scrollable area. It
  // mocks fetching a card and updates the state.
  // TODO: Update this function to receive real cards from our database.

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/games/").then((res) => {
      res.json();
      console.log(res.json());
      setCard(res.json());
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div id="scrollableDiv" className={styles.cards}>
        {console.log(cards)}
        <InfiniteScroll
          dataLength={cards.data.length}
          next={fetchCard}
          hasMore={true}
          loader={<p>Loading...</p>}
          endMessage={<p>No more data to load.</p>}
          scrollableTarget="scrollableDiv"
        >
          {cards.map((card) => (
            <div key={card.id}>
              <Card num={card.id} />
            </div>
          ))}
        </InfiniteScroll>
        {error && <p>Error: {error.message}</p>}
      </div>
    </>
  );
};

export default Cards;
