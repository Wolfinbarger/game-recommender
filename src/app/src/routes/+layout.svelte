<!--
  Main Layout Component

  This layout wraps all pages in the application.
  Whatever we put here will appear on every page.
-->

<script lang="ts">
  import '../app.scss';
  import Nav from '$lib/components/Nav.svelte';
  import favicon from '$lib/assets/favicon.svg';

  let { children } = $props();
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div class="app-container">
  <Nav />
  <main>
    {@render children()}
  </main>
</div>

<style>
  .app-container {
    display: flex;
    min-height: 100vh;
  }

  main {
    flex: 1;
    overflow-y: auto;
  }
</style>
