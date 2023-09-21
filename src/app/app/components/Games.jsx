import Card from "./card/Card.jsx";
async function getGames() {
  const url = "http://127.0.0.1:8000/api/games/";
  const res = await fetch(url, { cache: "no-store" });

  return res.json();
}

export default async function Games() {
  const games = await getGames();
  const alphaGames = games.data.sort();
  return (
    <>
      {alphaGames.map((game) => (
        <Card key={game.id} value={game} />
      ))}
    </>
  );
}
