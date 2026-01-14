/**
 * Svelte Stores for Game State Management
 *
 * Stores in Svelte are like React's state, but they can be shared
 * across multiple components easily. Any component can subscribe to
 * a store and automatically re-render when the store's value changes.
 *
 * Think of a store as a container for data that multiple parts of
 * your app might need to access or modify.
 */

import { writable } from 'svelte/store';
import type { Game } from '$lib/types/game';

/**
 * Store containing all the games currently loaded.
 *
 * This starts as an empty array and gets filled as we fetch
 * games from the API. When infinite scroll loads more games,
 * they get appended to this array.
 *
 * @example
 * ```typescript
 * // In a Svelte component:
 * import { games } from '$lib/stores/games';
 *
 * // Read the current value
 * games.subscribe(value => console.log(value));
 *
 * // Update the value
 * games.set([...newGames]);
 * ```
 */
export const games = writable<Game[]>([]);

/**
 * Store tracking whether we're currently loading data.
 *
 * This is useful for showing loading spinners or disabling
 * buttons while an API request is in progress.
 *
 * Starts as `true` because we load games immediately when
 * the app starts.
 */
export const loading = writable<boolean>(true);

/**
 * Store containing any error that occurred.
 *
 * If an API request fails, we store the error message here
 * so we can display it to the user.
 *
 * `null` means no error has occurred.
 */
export const error = writable<string | null>(null);

/**
 * Store tracking the current page number for pagination.
 *
 * The API returns games in pages (10 games per page).
 * This store keeps track of which page we're currently on.
 *
 * When the user scrolls to the bottom, we increment this
 * to fetch the next page.
 */
export const currentPage = writable<number>(1);

/**
 * Store tracking whether there are more games to load.
 *
 * When we've loaded all available games, this becomes `false`
 * and we stop trying to fetch more pages.
 */
export const hasMoreGames = writable<boolean>(true);
