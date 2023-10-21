// Ref link: https://nextjs.org/docs/app/building-your-application/rendering/client-components
'use client'

import React, {useEffect, useState} from "react";
import Card from "@/app/components/card/Card";

import styles from "./cards.module.scss";
import InfiniteScroll from "react-infinite-scroll-component";

const Cards = () => {
    // ------- States -------
    const [cards, setCard] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [page, setPage] = useState(1);

    const fetchCard = async () => {
        const result = {id: page};
        try {
            setCard((prev) => [...prev, result]);
            setPage(prevPage => prevPage + 1);
        } catch
            (error) {
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
            <div className={styles.cards}>
                <InfiniteScroll
                    dataLength={cards.length}
                    next={fetchCard}
                    hasMore={true}
                    loader={<p>Loading...</p>}
                    endMessage={<p>No more data to load.</p>}
                >
                    {cards.map(card => (
                        <div key={card.id}> <Card/> </div>
                    ))}
                </InfiniteScroll>
                {error && <p>Error: {error.message}</p>}
            </div>
        </>
    );
};

export default Cards
