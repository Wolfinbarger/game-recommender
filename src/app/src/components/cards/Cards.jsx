// Ref link: https://nextjs.org/docs/app/building-your-application/rendering/client-components

import React, { useEffect, useState } from "react";
import Card from "../card/Card";

import styles from "./cards.module.scss";
import InfiniteScroll from "react-infinite-scroll-component";

const Cards = () => {
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
  const [cards, setCard] = useState(initialCardState);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(initialCardState.length);

  // This function is called by infinite scroll when the user is near the bottom of the scrollable area. It
  // mocks fetching a card and updates the state.
  // TODO: Update this function to receive real cards from our database.
  const fetchCard = () => {
    const result = { id: page };
    try {
      setCard((prev) => [...prev, result]);
      setPage((prevPage) => prevPage + 1);
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchCard();
  }, []);

  return (
    <>
      <section className={styles.cards}>
        <InfiniteScroll
          dataLength={cards.length}
          next={fetchCard}
          hasMore={true}
          loader={<p>Loading...</p>}
          endMessage={<p>No more data to load.</p>}
          style={{ overflow: "hidden" }}
        >
          {cards.map((card) => (
            <div key={card.id}>
              <Card num={card.id} />
            </div>
          ))}
        </InfiniteScroll>
        {error && <p>Error: {error.message}</p>}
      </section>
    </>
  );
};

export default Cards;
