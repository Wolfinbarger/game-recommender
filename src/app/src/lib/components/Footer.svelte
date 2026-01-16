<!--
  Footer Component

  This component displays the footer at the bottom of the page
  when all games have been loaded (end of infinite scroll).

  It shows copyright information and a contact link.
-->

<script lang="ts">
  // No script needed for this simple component
  // In the future, you could add:
  // - Current year calculation: const year = new Date().getFullYear()
  // - Contact form functionality
  // - Links to social media
</script>

<!--
  The footer is displayed with flexbox layout to space items evenly.
  In the original React code, this used Tailwind classes, but we've
  converted them to SCSS for consistency.
-->
<footer>
  <!--
    Copyright notice.
    The "text-xs" class in the original has been moved to the CSS below.
  -->
  <p class="text-xs">Copyright @ 2023 Clever Penguin Design</p>

  <!--
    Contact link.
    In the future, this could be an actual link: <a href="/contact">Contact Us</a>
  -->
  <p class="text-xs">Contact Us</p>
</footer>

<!--
  Component-specific styles using SCSS.
-->
<style lang="scss">
  /**
   * Import our global color variables.
   */
  @use '$lib/styles/variables';

  /**
   * Style the footer container.
   *
   * This appears at the end of the game list when all games are loaded.
   */
  footer {
    height: 300%; /* Large height to create visual separation */
    display: flex; /* Arrange children in a row */
    flex-direction: row; /* Horizontal layout */
    justify-content: space-between; /* Space items evenly */
    padding: 0 1.25rem; /* Horizontal padding (converted from px-5) */
    align-items: center; /* Vertically center the text */
    border-top: 0.1em solid white; /* Top border to separate from content */
    background-color: variables.$grey-color;
    margin-top: auto; /* Pushes footer to bottom */
  }

  /**
   * Small text size for copyright and contact info.
   * This replaces the Tailwind "text-xs" class.
   */
  .text-xs {
    font-size: 0.75rem; /* 12px */
    line-height: 1rem; /* 16px */
  }
</style>
