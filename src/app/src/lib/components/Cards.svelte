<!--
  Cards Container Component with Infinite Scroll

  This is the main component that displays the list of game cards.
  It handles:
  - Fetching initial game data when the component loads
  - Implementing infinite scroll to load more games as you scroll down
  - Managing loading states and errors
  - Displaying the footer when all games are loaded

  How infinite scroll works:
  1. We listen to the window's scroll event
  2. When the user scrolls near the bottom (within 200px), we fetch more games
  3. New games are appended to the existing list
  4. The process repeats until all games are loaded
-->

<script lang="ts">
  import { onMount } from 'svelte';
  import { games, loading, error, currentPage, hasMoreGames } from '$lib/stores/games';
  import { fetchGames } from '$lib/api/games';
  import Card from './Card.svelte';
  import Footer from './Footer.svelte';

  /**
   * Flag to prevent multiple simultaneous fetch requests.
   * Without this, scrolling quickly could trigger multiple API calls at once.
   */
  let isFetching = false;

  /**
   * Fetches initial game data when the component first loads.
   *
   * This function runs once when the component mounts (appears on screen).
   * It fetches the first page of games from the API.
   */
  async function loadInitialGames() {
    try {
      // Set loading to true to show loading indicator
      $loading = true;

      // Fetch the first page of games from the API
      const response = await fetchGames(1);

      // Store the games in our Svelte store
      // The $ prefix is Svelte's shorthand for accessing store values
      $games = response.data;

      // Clear any previous errors
      $error = null;
    } catch (err) {
      // If something goes wrong, store the error message
      $error = err instanceof Error ? err.message : 'An unknown error occurred';
      console.error('Error loading initial games:', err);
    } finally {
      // Whether successful or not, we're done loading
      $loading = false;
    }
  }

  /**
   * Loads the next page of games for infinite scroll.
   *
   * This function is called when the user scrolls near the bottom of the page.
   * It fetches the next page of games and appends them to the existing list.
   */
  async function loadMoreGames() {
    // Prevent multiple simultaneous fetches
    if (isFetching || $loading || !$hasMoreGames) {
      return;
    }

    try {
      isFetching = true;
      $loading = true;

      // Increment the page number to fetch the next page
      $currentPage += 1;

      // Fetch the next page of games
      const response = await fetchGames($currentPage);

      // If we got games back, append them to the existing list
      if (response.data && response.data.length > 0) {
        $games = [...$games, ...response.data];
        console.log($games)

        /**
         * Check if we've loaded all available games.
         * If the API returns fewer games than expected (or provides a total count),
         * we know we've reached the end.
         *
         * For now, we assume there are more games if we got a full page.
         * You might want to check response.num_of_objects to be more precise.
         */
        if (response.data.length < 10) {
          // Less than a full page means we've reached the end
          $hasMoreGames = false;
        }
      } else {
        // No more games to load
        $hasMoreGames = false;
      }

      $error = null;
    } catch (err) {
      $error = err instanceof Error ? err.message : 'An unknown error occurred';
      console.error('Error loading more games:', err);
    } finally {
      $loading = false;
      isFetching = false;
    }
  }

  /**
   * Handles the window scroll event for infinite scroll.
   *
   * This function checks if the user has scrolled near the bottom of the page.
   * If they have, it triggers loading more games.
   *
   * The threshold (200px from bottom) gives a smooth experience by loading
   * new content before the user actually reaches the very bottom.
   */
  function handleScroll() {
    // Calculate how far from the bottom we are
    const scrollHeight = document.documentElement.scrollHeight; // Total page height
    const scrollTop = window.scrollY; // How far down we've scrolled
    const clientHeight = window.innerHeight; // Visible window height

    // Distance from the bottom of the page
    const distanceFromBottom = scrollHeight - (scrollTop + clientHeight);

    /**
     * If we're within 200 pixels of the bottom, load more games.
     * The 200px threshold provides a buffer so loading happens smoothly
     * before the user reaches the actual bottom.
     */
    if (distanceFromBottom < 200 && $hasMoreGames && !isFetching && !$loading) {
      loadMoreGames();
    }
  }

  /**
   * onMount runs when the component is first added to the page.
   * It's similar to useEffect with an empty dependency array in React.
   */
  onMount(() => {
    // Load the initial games
    loadInitialGames();

    /**
     * Return a cleanup function that runs when the component is removed.
     * This removes the scroll event listener to prevent memory leaks.
     */
    return () => {
      // No cleanup needed since we use svelte:window
    };
  });
</script>

<!--
  Listen to the window scroll event.
  svelte:window is a special Svelte element that lets us listen to window events
  without manually adding/removing event listeners.
-->
<svelte:window on:scroll={handleScroll} />

<!--
  Main section containing all the game cards.
-->
<section class="cards">
  <!--
    Display all loaded games.

    The {#each} block loops through the games array and creates a Card for each game.
    The (game.id) after the loop is a "key" - it helps Svelte efficiently update
    the list when games are added or removed.
  -->
  {#each $games as game (game.id)}
    <Card {game} />
  {/each}

  <!--
    Show a loading message while fetching more games.
    The {#if} block only renders its content when the condition is true.
  -->
  {#if $loading}
    <p>Loading...</p>
  {/if}

  <!--
    Show the footer when we've loaded all games.
    This signals to the user that they've reached the end of the list.
  -->
  {#if !$hasMoreGames && !$loading}
    <Footer />
  {/if}

  <!--
    Display any errors that occurred.
    Good user experience means showing clear error messages when things go wrong.
  -->
  {#if $error}
    <p class="error">Error: {$error}</p>
  {/if}
</section>

<!--
  Component-specific styles.
-->
<style lang="scss">
  .cards {
    margin-left: auto; 
    width: 85%; 
    
    /* 1. Remove dots if Card.svelte uses <li> tags */
    display: flex;
    flex-direction: column;
    list-style: none; 
  }

  /* 2. This forces any list items inside the container to hide their dots */
  :global(.cards li) {
    list-style-type: none !important;
  }

  /* 3. This catches any default browser padding that pushes icons to the right */
  :global(.cards ul) {
    padding: 0;
    margin: 0;
    list-style: none;
  }

  .error {
    color: #ff6b6b;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
  }
</style>
