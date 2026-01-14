<!--
  Avatar Component

  This component displays a user avatar with an icon and username.
  It's shown at the bottom of the navigation sidebar.

  In the future, this could be enhanced to:
  - Show the actual user's profile picture
  - Display the real username from authentication
  - Allow clicking to open a user menu
-->

<script lang="ts">
  /**
   * FontAwesome icon for the user avatar.
   * We import just the specific icon we need to keep bundle size small.
   */
  import Fa from 'svelte-fa';
  import { faUser } from '@fortawesome/free-regular-svg-icons';

  /**
   * The username to display.
   * For now this is hardcoded, but could be passed as a prop
   * or fetched from a user authentication system.
   */
  const username = 'UserName';
</script>

<!--
  The avatar container holds both the icon and the username.
  It's styled to appear at the bottom of the navigation bar.
-->
<div class="avatar">
  <!--
    The avatar icon is a circular container with a white background
    that holds the user icon inside.
  -->
  <div class="avatar-icon">
    <!-- FontAwesome user icon, displayed in black -->
    <Fa icon={faUser} style="color: #000000" />
  </div>

  <!-- Display the username next to the icon -->
  <h3>{username}</h3>
</div>

<!--
  Component-specific styles using SCSS.

  In Svelte, styles in a <style> block are automatically scoped to this component.
  This means these styles won't affect other components, preventing style conflicts.

  The "lang='scss'" tells Svelte to process this as SCSS instead of plain CSS.
-->
<style lang="scss">
  /**
   * Import our global color variables so we can use them here.
   * The '@use' syntax is the modern SCSS way to import modules.
   */
  @use '$lib/styles/variables';

  /**
   * Style the main avatar container.
   * This creates a horizontal layout with the icon and username.
   */
  .avatar {
    display: flex; /* Arrange children horizontally */
    gap: 4%; /* Space between icon and username */
    align-items: center; /* Vertically center icon and text */
    justify-content: center; /* Horizontally center content */
    background-color: variables.$primary-color;
    border-top: 1px solid black; /* Separates from nav items above */
    width: 100%;
    height: 10%; /* Takes up 10% of the nav bar height */
  }

  /**
   * Style the circular icon container.
   * The 50% border-radius creates a perfect circle.
   */
  .avatar-icon {
    display: flex;
    justify-content: center; /* Center the icon horizontally */
    align-items: center; /* Center the icon vertically */
    background-color: white;
    height: 2em; /* Fixed size for the circle */
    width: 2em;
    border-radius: 50%; /* Makes it circular */
  }
</style>
