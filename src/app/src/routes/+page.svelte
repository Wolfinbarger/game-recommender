<!--
  Home Page

  This is the main landing page of the Game Recommender application.
  It displays the game cards with infinite scroll functionality.
-->

<script lang="ts">
  import Cards from '$lib/components/Cards.svelte';
</script>

<svelte:head>
  <title>Game Recommender - Discover Your Next Favorite Game</title>
  <meta
    name="description"
    content="Find new games to play with friends or solo. Browse our curated collection of games with reviews, ratings, and platform availability."
  />
</svelte:head>

<Cards />
