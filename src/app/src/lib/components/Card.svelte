<!--
  Game Card Component

  This component displays information about a single game.
  It shows:
  - Game cover image
  - Title and ID
  - Action icons (share, add to list, more info)
  - Number of players
  - Review score
  - Short description
  - Platform availability icons

  Props:
  - game: The game object containing all the game's information
-->

<script lang="ts">
  /**
   * Import FontAwesome icons for the card UI.
   */
  import Fa from 'svelte-fa';
  import { faPaperPlane, faUser } from '@fortawesome/free-regular-svg-icons';
  import { faPlus, faCircleInfo, faChartSimple } from '@fortawesome/free-solid-svg-icons';
  import { faSteam } from '@fortawesome/free-brands-svg-icons';

  /**
   * Import the Game type to ensure type safety.
   */
  import type { Game } from '$lib/types/game';

  /**
   * Props for this component.
   *
   * In Svelte 5, we use $props() to declare props that can be passed from a parent component.
   * The parent component will pass game data like this: <Card game={gameObject} />
   */
  let { game }: { game: Game } = $props();

  /**
   * Placeholder image for games.
   * In the future, this should be replaced with the actual game cover image.
   * You could get this from:
   * - Your database
   * - The IGDB API
   * - A CDN with game images
   */
  const placeholderImage =
    'https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80';
</script>

<!--
  Main card container.
  This holds the game image and all the game information.
-->
<div class="card">
  <!--
    Game cover image.
    Alt text describes the image for accessibility and SEO.
  -->
  <img src={placeholderImage} alt="Cover art for {game.title}" />

  <!--
    Content section holds all the text and icons.
    It's organized into sections: header, info, description, platforms.
  -->
  <div class="content">
    <!--
      Header section with game title and action icons.
    -->
    <header>
      <!--
        Game title with ID number.
        The ID is shown for debugging/reference purposes.
      -->
      <h2>
        {game.title} #{game.id}
      </h2>

      <!--
        Action icons (share, add to wishlist, more info).
        These are placeholders - they would need click handlers to be functional.
      -->
      <ul class="card-header-icons">
        <li>
          <!-- Share icon - could open a share dialog -->
          <Fa icon={faPaperPlane} style="color: #fafafa" />
        </li>
        <li>
          <!-- Add to wishlist icon - could add game to user's wishlist -->
          <Fa icon={faPlus} />
        </li>
        <li>
          <!-- More info icon - could open a detailed game page -->
          <Fa icon={faCircleInfo} />
        </li>
      </ul>
    </header>

    <!--
      Info section with player count and review score.
    -->
    <div class="info">
      <!--
        Number of players supported.
        Currently hardcoded - should come from game.multiplayer data.
      -->
      <div class="number-players">
        <Fa icon={faUser} />
        <p>1-4 Players</p>
      </div>

      <!--
        Review score.
        Currently hardcoded - should display game.review_score.
      -->
      <div class="review-score">
        <Fa icon={faChartSimple} />
        <p>Review Score {game.review_score || 'N/A'}</p>
      </div>
    </div>

    <!--
      Game description.
      Currently shows placeholder text - should display game.description.
      You might want to truncate long descriptions with ellipsis (...).
    -->
    <div class="description">
      {game.description ||
        'Satisfactory is a first person open-world factory building game with a dash of exploration and combat. Play...'}
    </div>

    <!--
      Platform availability icons.
      Shows which platforms the game is available on (Steam, PlayStation, etc.).
      Currently only shows Steam - should be dynamic based on game.platforms data.
    -->
    <div class="platforms">
      <ul>
        <li>
          <!-- Steam icon - should conditionally show based on game.platforms.steam -->
          <Fa icon={faSteam} />
        </li>
        <!--
          In the future, you would add more platform icons here based on the data:
          {#if game.platforms?.playstation}
            <li><Fa icon={faPlaystation} /></li>
          {/if}
        -->
      </ul>
    </div>
  </div>
</div>

<!--
  Component-specific styles using SCSS.
-->
<style lang="scss">
  /**
   * Import our global color variables.
   */
  @use '$lib/styles/variables';

  /**
   * Remove default borders from content header.
   * Also prevents horizontal overflow.
   */
  .content > header {
    border: none;
    overflow-x: hidden;
  }

  /**
   * Main card container.
   * Displays game image on the left and content on the right.
   */
  .card {
    background-color: variables.$secondary-color;
    height: 30%;
    width: 90%;
    display: flex; /* Arrange image and content side by side */
    justify-content: left;
    border: none;
    margin: 20px 30px; /* Space between cards */
  }

  /**
   * Game cover image styling.
   * Takes up 30% of the card width.
   */
  .card > img {
    width: 30%;
    left: 0;
    border: none;
  }

  /**
   * Content area (everything except the image).
   * Uses flexbox column layout to stack sections vertically.
   */
  .content {
    width: auto;
    display: flex;
    flex-direction: column; /* Stack sections vertically */
    justify-content: space-between; /* Distribute space evenly */
    background-color: variables.$secondary-color;
    border: none;
  }

  /**
   * Header section styling.
   * Displays title on left and action icons on right.
   */
  .content > header {
    display: flex;
    justify-content: space-between; /* Push title left and icons right */
    width: 100%;
    align-items: center; /* Vertically center */
    border: none;
  }

  /**
   * Game title styling.
   */
  .content header h2 {
    font-size: 1.8rem;
    border: none;
    padding-left: 1rem;
  }

  /**
   * Action icons in the header.
   * Arranged horizontally with small gaps between them.
   */
  .card-header-icons {
    display: flex;
    gap: 8px; /* Space between icons */
    padding-right: 24px;
    border: none;
  }

  /**
   * Platform icons section at the bottom of the card.
   * Aligned to the right side.
   */
  .platforms {
    background-color: variables.$secondary-color;
    border: none;
    display: flex;
    justify-content: end; /* Align to right */
    padding-right: 16px;
    padding-bottom: 16px;
    font-size: 1.3rem;
  }

  /**
   * Info section containing player count and review score.
   * Arranged horizontally.
   */
  .info {
    display: flex;
    justify-content: start; /* Align to left */
    background-color: variables.$secondary-color;
    border: none;
    font-size: 1rem;
    padding-left: 1rem;
  }

  /**
   * Player count display.
   * Shows icon and text horizontally.
   */
  .number-players {
    display: flex;
    align-items: center; /* Vertically center icon and text */
    border: none;
    background-color: variables.$secondary-color;
    gap: 0.5rem; /* Space between icon and text */
    padding-right: 2.5rem; /* Space before review score */
    justify-content: start;
  }

  /**
   * Review score display.
   * Shows icon and text horizontally.
   */
  .review-score {
    display: flex;
    align-items: center; /* Vertically center icon and text */
    height: 30px;
    background-color: variables.$secondary-color;
    border: none;
    gap: 0.5rem; /* Space between icon and text */
    width: 300px;
    justify-content: start;
  }

  /**
   * Game description text.
   * Limited width to prevent overly long lines.
   */
  .description {
    background-color: variables.$secondary-color;
    border: none;
    font-size: 1rem;
    padding-left: 1rem;
    width: 88%;
    align-self: start;
  }
</style>
