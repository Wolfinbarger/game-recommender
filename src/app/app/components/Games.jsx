// async function getGames() {
//   const url = "http://127.0.0.1:8000/api/games/";
//   const res = await fetch(url);

//   return res.json();
// }

// export default async function Games() {
//   const games = await getGames();
//   const alphaGames = games.data.sort();
//   return (
//     <>
//       {alphaGames.map((game) => (
//         <div key={game.id}>
//           <h3>{game.title}</h3>
//         </div>
//       ))}
//     </>
//   );
// }
