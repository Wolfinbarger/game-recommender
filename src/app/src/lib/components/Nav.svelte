<!--
  Navigation Sidebar Component

  This component displays the main navigation sidebar on the left side of the screen.
  It contains:
  - The app logo at the top
  - Navigation menu items (Home, Search, My Games, Wishlist)
  - User avatar at the bottom

  In SvelteKit, we'll use proper routing for each menu item so they
  can navigate to different pages.
-->

<script lang="ts">
  /**
   * Import FontAwesome icons.
   * We only import the specific icons we need to keep the bundle size small.
   *
   * Fa is the Svelte component for rendering FontAwesome icons.
   */
  import Fa from 'svelte-fa';
  import {
    faHouse,
    faMagnifyingGlass,
    faGamepad,
    faPen
  } from '@fortawesome/free-solid-svg-icons';

  /**
   * Import the Avatar component to display at the bottom of the nav.
   */
  import Avatar from './Avatar.svelte';

  /**
   * Import the logo image.
   * In SvelteKit, we use the $lib alias to reference the lib directory.
   */
  import logo from '$lib/assets/img/logo.jpg';

  /**
   * Navigation menu items.
   * Each item has a label, an icon, and a route path.
   * This makes it easy to add or modify menu items in the future.
   */
  const navItems = [
    { label: 'Home', icon: faHouse, path: '/' },
    { label: 'Search', icon: faMagnifyingGlass, path: '/search' },
    { label: 'My Games', icon: faGamepad, path: '/my-games' },
    { label: 'Wishlist', icon: faPen, path: '/wishlist' }
  ];
</script>

<!--
  The main navigation element.
  It's fixed to the left side of the screen and spans the full height.
-->
<nav>
  <!--
    App logo at the top of the nav.
    Alt text is important for accessibility - screen readers will read this
    description to users who can't see the image.
  -->
  <img src={logo} alt="Game Recommender logo" />

  <!--
    Navigation menu list.
    We use an unordered list (ul) because semantically, this is a list of links.
  -->
  <ul>
    <!--
      Loop through each navigation item and create a list item.

      In Svelte, {#each} is used to loop through arrays.
      The (item) after the array gives us a variable name to use in the loop.
    -->
    {#each navItems as item}
      <li>
        <!--
          In a future enhancement, you would wrap this in a SvelteKit <a> tag
          to make it clickable and navigate to the route:

          <a href={item.path}>
            <FontAwesomeIcon ... />
            {item.label}
          </a>

          For now, we're keeping it simple without routing functionality.
        -->

        <!--
          Display the icon for this menu item.
          fw (fixedWidth) ensures all icons take up the same space, keeping alignment clean.
        -->
        <Fa icon={item.icon} class="font-awesome-icon" fw />

        <!-- Display the label for this menu item -->
        {item.label}
      </li>
    {/each}
  </ul>

  <!--
    User avatar at the bottom of the nav.
    This component handles displaying the user profile icon and name.
  -->
  <Avatar />
</nav>

<!--
  Component-specific styles using SCSS.
-->
<style lang="scss">
  /**
   * Import our global color variables.
   */
  @use '$lib/styles/variables';

  /**
   * Style the FontAwesome icons to be white.
   * This is a global class that applies to all icons in this component.
   */
  :global(.font-awesome-icon) {
    color: variables.$white-color;
  }

  /**
   * Main navigation container.
   *
   * This is fixed to the left side of the screen and takes up 15% of the width.
   * It uses flexbox to arrange its children (logo, menu, avatar) vertically.
   */
  nav {
    background-color: variables.$primary-color-accent;
    padding-top: 4rem; /* Space at the top for breathing room */
    display: flex;
    flex-direction: column; /* Stack children vertically */
    align-items: center; /* Center children horizontally */
    border-right: 1px solid variables.$secondary-color-accent; /* Separates nav from main content */
    position: fixed; /* Stays in place when scrolling */
    height: 100vh; /* Full viewport height */
    width: 15%; /* Takes up 15% of screen width */
  }

  /**
   * Style the navigation menu list.
   *
   * The 'margin-bottom: auto' pushes the avatar to the bottom of the nav,
   * creating space between the menu and the avatar.
   */
  nav ul {
    margin-top: 15%; /* Space between logo and menu */
    margin-bottom: auto; /* Pushes avatar to bottom */
    padding-left: 15%; /* Indent the menu items slightly */
  }

  /**
   * Style individual menu items.
   *
   * Each item displays its icon and label horizontally.
   * Hover state provides visual feedback when the user mouses over an item.
   */
  li {
    display: flex;
    gap: 1rem; /* Space between icon and label */
    place-items: center center; /* Center icon and text vertically and horizontally */
    font-size: 1.5em;
    border-radius: 4px; /* Slightly rounded corners */

    /**
     * Hover effect for menu items.
     * Changes background color and cursor to indicate interactivity.
     */
    &:hover {
      background-color: variables.$secondary-color;
      cursor: pointer; /* Shows hand cursor to indicate it's clickable */
    }
  }
</style>
